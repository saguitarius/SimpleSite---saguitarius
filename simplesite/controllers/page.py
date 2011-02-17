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
from sqlalchemy import delete
from simplesite.controllers.nav import NewNavForm, ValidBefore

from authkit.authorize.pylons_adaptors import authorize

log = logging.getLogger(__name__)

class ValidTags(formencode.FancyValidator):
    def _to_python(self, values, state):
        # Because this is a chained validator, values will contain
        # a dictionary with a tags key associated with a list of
        # integer values representing the selected tags.
        all_tag_ids = [tag.id for tag in meta.Session.query(model.Tag)]
        for tag_id in values['tags']:
            if tag_id not in all_tag_ids:
                raise formencode.Invalid(
                    "One or more selected tags could not be found in the database",
                    values,
                    state
                )
        return values

class ValidTagsForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    tags = formencode.foreach.ForEach(formencode.validators.Int())
    chained_validators = [ValidTags()]

class UniquePagePath(formencode.validators.FancyValidator):
    def _to_python(self, values, state):
        nav_q = meta.Session.query(model.Nav)
        query = nav_q.filter_by(section=values['section'],
            type='page', path=values['path'])
        if request.urlvars['action'] == 'save':
            # Ignore the existing id when performing the check
            query = query.filter(model.Nav.id != int(request.urlvars['id']))
        existing = query.first()
        if existing is not None:
            raise formencode.Invalid("There is already a page in this "
                "section with this path", values, state)
        return values

class NewPageForm(NewNavForm):
    allow_extra_fields = True
    filter_extra_fields = True
    content = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':'Please enter some content for the page. '
        }
    )
    heading = formencode.validators.String()
    title = formencode.validators.String(not_empty=True)
    chained_validators = [ValidBefore(), UniquePagePath()]


class PageController(BaseController):
    
    def __before__(self):
        nav_q = meta.Session.query(model.Nav)
        c.available_sections = [(nav.id, nav.name) for nav in nav_q.filter_by(type='section')]

    def index(self):
        h.redirect(url('path', id=page.id))
    
    def view(self, id=None):
        if id is None:
            abort(404)
        page_q = meta.Session.query(model.Page)
        c.page = page_q.filter_by(id=int(id)).first()
        if c.page is None:
            abort(404)
        c.comment_count = meta.Session.query(model.Comment).filter_by(pageid=id).count()
        tag_q = meta.Session.query(model.Tag)
        c.available_tags = [(str(tag.id), tag.name) for tag in tag_q]
        c.selected_tags = {'tags':[tag.id for tag in c.page.tags]}
        c.menu = request.environ['simplesite.navigation']['menu']
        c.tabs = request.environ['simplesite.navigation']['tabs']
        c.breadcrumbs = request.environ['simplesite.navigation']['breadcrumbs']
        return render('/derived/page/view.html')

    def new(self):
        values = {}
        values.update(request.params)
        if values.has_key('before') and values['before'] == u'None':
            values['before'] = ''
        c.before_options = model.Nav.get_before_options(values.get('section', 0))
        c.before_options.append(['', '[At the end]'])
        return htmlfill.render(render('/derived/page/new.html'), values)
    
    @restrict('POST')
    @validate(schema=NewPageForm(), form='new')
    def create(self):
        # Add the new page to the database
        page = model.Page()
        for k, v in self.form_result.items():
            setattr(page, k, v)
        meta.Session.add(page)
        model.Nav.add_navigation_node(page, self.form_result['section'],
                                      self.form_result['before'])
        meta.Session.commit()
        # Issue an HTTP redirect
        return h.redirect(url('path', id=page.id))
    
    @authorize(h.auth.is_valid_user)
    def edit(self, id=None):
        if id is None:
            abort(404)
        page_q = meta.Session.query(model.Page)
        page = page_q.filter_by(id=id).first()
        if page is None:
            abort(404)
        c.page = page_q.get(int(id))
        values = {
            'name': page.name,
            'path': page.path,
            'section': page.section,
            'before': page.before,
            'title': page.title,
            'heading': page.heading,
            'content': page.content,

        }
        c.before_options = model.Nav.get_before_options(page.section, page.id)
        c.before_options.append(['', '[At the end]'])
        return htmlfill.render(render('/derived/page/edit.html'), values)
    
    @authorize(h.auth.is_valid_user)
    @restrict('POST')
    @validate(schema=NewPageForm(), form='edit')
    def save(self, id=None):
        page_q = meta.Session.query(model.Page)
        page = page_q.filter_by(id=id).first()
        if page is None:
            abort(404)
        if not(page.section == self.form_result['section'] and \
            page.before == self.form_result['before']):
            model.Nav.remove_navigation_node(page)
            model.Nav.add_navigation_node(page, self.form_result['section'],
                self.form_result['before'])
        for k, v in self.form_result.items():
            if getattr(page, k) != v:
                setattr(page, k, v)
        meta.Session.commit()
        session['flash'] = 'Page successfully updated.'
        session.save()
        # Issue an HTTP redirect
        return h.redirect(url('path', id=page.id))
    
    @authorize(h.auth.has_delete_role)
    def list(self):
        records = meta.Session.query(model.Page)
        c.paginator = paginate.Page(
            records,
            page=int(request.params.get('page', 1)),
            items_per_page = 4,
            controller='page',
            action='list',
        )
        return render('/derived/page/list.html')
    
    @authorize(h.auth.has_delete_role)
    def delete(self, id=None):
        if id is None:
            abort(404)
        page_q = meta.Session.query(model.Page)
        page = page_q.filter_by(id=id).first()
        if page is None:
            abort(404)
        meta.Session.execute(delete(model.pagetag_table, 
            model.pagetag_table.c.pageid==page.id))
        model.Nav.remove_navigation_node(page)
        meta.Session.delete(page)
        meta.Session.commit()
        return render('/derived/page/deleted.html')
    
    @restrict('POST')
    @validate(schema=ValidTagsForm(), form='view')
    def update_tags(self, id=None):
        if id is None:
            abort(404)
        page_q = meta.Session.query(model.Page)
        page = page_q.filter_by(id=id).first()
        if page is None:
            abort(404)
        tags_to_add = []
        for i, tag in enumerate(page.tags):
            if tag.id not in self.form_result['tags']:
                del page.tags[i]
        tagids = [tag.id for tag in page.tags]
        for tag in self.form_result['tags']:
            if tag not in tagids:
                t = meta.Session.query(model.Tag).get(tag)
                page.tags.append(t)
        meta.Session.commit()
        session['flash'] = 'Tags successfully updated.'
        session.save()
        return redirect(url('path', id=page.id))