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

from simplesite.controllers.nav import NewNavForm, ValidBefore

log = logging.getLogger(__name__)

class UniqueSectionPath(formencode.validators.FancyValidator):
    "Checks that there isn't already an existing section with the same path"
    def _to_python(self, values, state):
        nav_q = meta.Session.query(model.Nav)
        query = nav_q.filter_by(section=values['section'],
            type='section', path=values['path'])
        if request.urlvars['action'] == 'save':
            # Ignore the existing ID when performing the check
            query = query.filter(model.Nav.id != int(request.urlvars['id']))
        existing = query.first()
        if existing is not None:
            raise formencode.Invalid("There is already a section in this "
                "section with this path", values, state)
        return values

class NewSectionForm(NewNavForm):
    chained_validators = [ValidBefore(), UniqueSectionPath()]
    
class ValidSectionPosition(formencode.FancyValidator):
    def _to_python(self, values, state):
        nav_q = meta.Session.query(model.Nav)
        if values.get('type', 'section') == 'section':
            # Make sure the section we are moving to is not already
            # a subsection of the current section
            section = nav_q.filter_by(id=int(values['section'])).one()
            current_section = nav_q.filter_by(id=request.urlvars['id']).one()
            while section:
                if section.section == current_section.id:
                    raise formencode.Invalid("You cannot move a section to "
                        "one of its subsections", values, state)
                if section.section == 1:
                    break
                section = nav_q.filter_by(id=section.section).first()
        return values

class EditSectionForm(NewNavForm):
    chained_validators = [
        ValidBefore(),
        UniqueSectionPath(),
        ValidSectionPosition()
    ]

class SectionController(BaseController):
    
    def __before__(self, id=None):
        nav_q = meta.Session.query(model.Nav)
        if id:
            nav_q=nav_q.filter_by(type='section').filter(model.nav_table.c.id!=int(id))
        else:
            nav_q = nav_q.filter_by(type='section')
        c.available_sections = [(nav.id, nav.name) for nav in nav_q]

    def index(self):
        h.redirect(url('path', id=section.id))
    
    def new(self):
        values = {}
        values.update(request.params)
        if values.has_key('before') and values['before'] == u'None':
            values['before'] = ''
        c.before_options = model.Nav.get_before_options(values.get('section', 0))
        c.before_options.append(['', '[At the end]'])
        return htmlfill.render(render('/derived/section/new.html'), values)

    
    @restrict('POST')
    @validate(schema=NewSectionForm(), form='new')
    def create(self):
        # Add the new section to the database
        section = model.Section()
        for k, v in self.form_result.items():
            setattr(section, k, v)
        meta.Session.add(section)
        model.Nav.add_navigation_node(section, self.form_result['section'], self.form_result['before'])
        # Flush the data to get the session ID.
        meta.Session.flush()
        index_page = model.Page()
        index_page.section = section.id
        index_page.path = 'index'
        index_page.title = 'Section Index'
        index_page.name = 'Section Index'
        index_page.content = 'This is the index page for this section.'
        meta.Session.add(index_page)
        meta.Session.commit()
        # Issue an HTTP redirect
        return h.redirect(url('path', id=section.id))
    
    def edit(self, id=None):
        if id is None:
            abort(404)
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=id).first()
        if section is None:
            abort(404)
        c.section = section_q.get(int(id))
        values = {
            'name': section.name,
            'path': section.path,
            'section': section.section,
            'before': section.before,
        }
        c.before_options = model.Nav.get_before_options(section.section, section.id)
        c.before_options.append(['', '[At the end]'])
        return htmlfill.render(render('/derived/section/edit.html'), values)
    
    @restrict('POST')
    @validate(schema=EditSectionForm(), form='edit')
    def save(self, id=None):
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=id).first()
        if section is None:
            abort(404)
        if not(section.section == self.form_result['section'] and \
            section.before == self.form_result['before']):
            model.Nav.remove_navigation_node(section)
            model.Nav.add_navigation_node(section, self.form_result['section'],
                self.form_result['before'])
        for k, v in self.form_result.items():
            if getattr(section, k) != v:
                setattr(section, k, v)
        meta.Session.commit()
        session['flash'] = 'Section successfully updated.'
        session.save()
        # Issue an HTTP redirect
        return h.redirect(url('path', id=section.id))
    
    def list(self):
        records = meta.Session.query(model.Section)
        c.paginator = paginate.Section(
            records,
            section=int(request.params.get('section', 1)),
            items_per_section = 4,
            controller='section',
            action='list',
        )
        return render('/derived/section/list.html')
    
    def delete(self, id=None):
        if id is None:
            abort(404)
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=id).first()
        if section is None:
            abort(404)
        nav_q = meta.Session.query(model.Nav)
        existing = nav_q.filter_by(section=id, type='section').filter(model.Page.path != 'index').first()
        if existing is not None:
            return render('/derived/section/cannot_delete.html')
        index_page = nav_q.filter_by(section=id, path='index', type='page').first()
        if index_page is not None:
            model.Nav.remove_navigation_node(index_page)
            meta.Session.delete(index_page)
        model.Nav.remove_navigation_node(section)
        meta.Session.delete(section)
        meta.Session.commit()
        return render('/derived/section/deleted.html')