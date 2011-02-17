import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from simplesite.lib.base import BaseController, render

import simplesite.model as model
import simplesite.model.meta as meta
import simplesite.lib.helpers as h

import formencode
from formencode import htmlfill
from pylons.decorators import validate
from pylons.decorators.rest import restrict
import webhelpers.paginate as paginate

log = logging.getLogger(__name__)

class NewCommentForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(not_empty=True)
    email = formencode.validators.Email(not_empty=True)
    content = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':'Please enter a comment.'
        }
    )

class CommentController(BaseController):

    def __before__(self, action, pageid=None):
        page_q = meta.Session.query(model.Page)
        c.page = pageid and page_q.filter_by(id=int(pageid)).first() or None
        if c.page is None:
            abort(404)   

    def index(self):
        h.redirect(url(controller='comment', action='view', id=1))
    
    def view(self, id=None):
        if id is None:
            abort(404)
        comment_q = model.meta.Session.query(model.Comment)
        c.comment = comment_q.filter_by(pageid=c.page.id, id=int(id)).first()
        if c.comment is None:
            abort(404)
        return render('/derived/comment/view.html')
    
    def new(self):
        return render('/derived/comment/new.html')
    
    @restrict('POST')
    @validate(schema=NewCommentForm(), form='new')
    def create(self):
        # Add the new comment to the database
        comment = model.Comment()
        comment.pageid = c.page.id
        for k, v in self.form_result.items():
            setattr(comment, k, v)
        meta.Session.add(comment)
        meta.Session.commit()
        # Issue an HTTP redirect
        return redirect(url(pageid=c.page.id, controller='comment', action='view', id=comment.id))
    
    def edit(self, id=None):
        if id is None:
            abort(404)
        comment_q = meta.Session.query(model.Comment)
        comment = comment_q.filter_by(pageid=c.page.id, id=id).first()
        if comment is None:
            abort(404)
        c.comment = comment_q.get(int(id))
        values = {
            'name': comment.name,
            'email': comment.email,
            'content': comment.content
        }
        return htmlfill.render(render('/derived/comment/edit.html'), values)
    
    @restrict('POST')
    @validate(schema=NewCommentForm(), form='edit')
    def save(self, id=None):
        comment_q = meta.Session.query(model.Comment)
        comment = comment_q.filter_by(pageid=c.page.id, id=id).first()
        if comment is None:
            abort(404)
        for k, v in self.form_result.items():
            if getattr(comment, k) != v:
                setattr(comment, k, v)
        meta.Session.commit()
        session['flash'] = 'Comment successfully updated.'
        session.save()
        # Issue an HTTP redirect
        return h.redirect(url(pageid=c.page.id, controller='comment', action='view', id=comment.id))
    
    def list(self):
        comments_q = meta.Session.query(model.Comment).filter_by(pageid=c.page.id)
        comments_q = comments_q.order_by(model.comment_table.c.created.asc())
        c.paginator = paginate.Page(
            comments_q,
            page=int(request.params.get('page', 1)),
            items_per_page=10,
            pageid=c.page.id,
            controller='comment',
            action='list'
        )
        return render('/derived/comment/list.html')
    
    def delete(self, id=None):
        if id is None:
            abort(404)
        comment_q = meta.Session.query(model.Comment)
        comment = comment_q.filter_by(pageid=c.page.id, id=id).first()
        if comment is None:
            abort(404)
        meta.Session.delete(comment)
        meta.Session.commit()
        return render('/derived/comment/deleted.html')