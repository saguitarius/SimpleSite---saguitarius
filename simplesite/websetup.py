"""Setup the SimpleSite application"""
import logging
import os.path

import pylons.test

from simplesite.config.environment import load_environment
from simplesite.model.meta import Session, Base
from simplesite import model
from simplesite.model import meta

from authkit.users.sqlalchemy_driver import UsersFromDatabase

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup simplesite here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    Base.metadata.bind = Base.engine
    Base.metadata.create_all(bind=Session.bind)
    
    log.info("Adding the AuthKit model...")
    users = UsersFromDatabase(model)
    meta.metadata.create_all(checkfirst=True)
    
    log.info("Adding roles and uses...")
    users.role_create("delete")
    users.user_create("foo", password="bar")
    users.user_create("admin", password="opensesame")
    users.user_add_role("admin", role="delete")
    
    log.info("Adding homepage...")
    section_home = model.Section()
    section_home.path=u''
    section_home.name=u'Home Section'
    meta.Session.add(section_home)
    meta.Session.flush()
    
    page_contact = model.Page()
    page_contact.title=u'Contact Us'
    page_contact.path=u'contact'
    page_contact.name=u'Contact Us Page'
    page_contact.content = u'Contact us page'
    page_contact.section=section_home.id
    meta.Session.add(page_contact)
    meta.Session.flush()
    
    section_dev = model.Section()
    section_dev.path=u'dev'
    section_dev.name=u'Development Section'
    section_dev.section=section_home.id
    section_dev.before=page_contact.id
    meta.Session.add(section_dev)
    meta.Session.flush()
    
    page_svn = model.Page()
    page_svn.title=u'SVN Page'
    page_svn.path=u'svn'
    page_svn.name=u'SVN Page'
    page_svn.content = u'This is the SVN page.'
    page_svn.section=section_dev.id
    meta.Session.add(page_svn)
    meta.Session.flush()
    
    page_dev = model.Page()
    page_dev.title=u'Development Home'
    page_dev.path=u'index'
    page_dev.name=u'Development Page'
    page_dev.content=u'This is the development home page.'
    page_dev.section=section_dev.id
    page_dev.before=page_svn.id
    meta.Session.add(page_dev)
    meta.Session.flush()
    
    page_home = model.Page()
    page_home.title=u'Home'
    page_home.path=u'index'
    page_home.name=u'Home'
    page_home.content=u'Welcome to the SimpleSite home page.'
    page_home.section=section_home.id
    page_home.before=section_dev.id
    meta.Session.add(page_home)
    meta.Session.flush()
    
    log.info("Adding tags...")

    tag1 = model.Tag()
    tag1.name = u'Pylons'
    meta.Session.add(tag1)
    
    tag2 = model.Tag()
    tag2.name = u'Paste'
    meta.Session.add(tag2)
    
    tag3 = model.Tag()
    tag3.name = u'Tutorial'
    meta.Session.add(tag3)
    
    tag4 = model.Tag()
    tag4.name = u'Database'
    meta.Session.add(tag4)
    
    tag5 = model.Tag()
    tag5.name = u'Recipe'
    meta.Session.add(tag5)
    meta.Session.flush()
    
    meta.Session.commit()
    log.info("Successfully set up.")