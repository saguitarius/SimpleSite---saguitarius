import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from simplesite.lib.base import BaseController, render

import simplesite.lib.helpers as h

from authkit.authorize.pylons_adaptors import authorize
from authkit.users.sqlalchemy_driver import UsersFromDatabase
from simplesite.model import meta
from pylons import request
import formencode
from formencode import htmlfill
from pylons.decorators import validate

log = logging.getLogger(__name__)

class RegistrationForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    username = formencode.validators.String(not_empty=True)
    password = formencode.validators.String(not_empty=True)

class AccountController(BaseController):

    def signin(self):
        if not request.environ.get('REMOTE_USER'):
            # This triggers the AuthKit middleware into displaying the sign-in form
            abort(401)
        else:
            return render('/derived/account/signedin.html')

    def signout(self):
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        return render('/derived/account/signedout.html')
    
    def signinagain(self):
        request.environ['paste.auth_tkt.logout_user']()
        return render('/derived/account/signin.html').replace('%s', h.url('signin'))
    
    @authorize(h.auth.has_delete_role)
    def register_form(self):
        return render('/derived/account/register.html')
    
    def custom_formatter(error):
        return '<span class="error-message">%s</span><br />\n' % (
            htmlfill.html_quote(error)
        )
    
    @validate(schema=RegistrationForm(), form='register_form', auto_error_formatter=custom_formatter)
    def register(self):
        users = request.environ['authkit.users']
        users.user_create(self.form_result['username'], password=self.form_result['password'])
        meta.Session.commit()
        return render('/derived/account/register.html')
