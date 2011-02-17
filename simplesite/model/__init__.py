"""The application's model objects"""
from simplesite.model.meta import Session, Base
from simplesite.model import meta

import sqlalchemy as sa
from sqlalchemy import orm


# Add these two imports:
import datetime
from sqlalchemy import schema, types


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    # autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    # We are using SQLAlchemy 0.5 so transactional=True is replaced by
    # autocommit=False
    sm = orm.sessionmaker(autoflush=True, autocommit=False, bind=engine)
    meta.Base.engine = engine
    meta.Session = orm.scoped_session(sm)

def now():
    return datetime.datetime.now()

nav_table = schema.Table('nav', meta.Base.metadata,
    schema.Column('id', types.Integer(), schema.Sequence('nav_id_seq', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(255), default=u'Untitled Node'),
    schema.Column('path', types.Unicode(255), default=u''),
    schema.Column('section', types.Integer(), schema.ForeignKey('nav.id')),
    schema.Column('before', types.Integer(), default=None),
    schema.Column('type', types.String(30), nullable=False)
)

section_table = sa.Table('section', meta.Base.metadata,
    schema.Column('id', types.Integer, schema.ForeignKey('nav.id'), primary_key=True),
)

page_table = schema.Table('page', meta.Base.metadata,
    schema.Column('id', types.Integer, schema.ForeignKey('nav.id'), primary_key=True),
    schema.Column('content', types.Unicode(255), nullable=False),
    schema.Column('posted', types.DateTime(), default=now),
    schema.Column('title', types.Unicode(255), default=u'Untitled Page'),
    schema.Column('heading', types.Unicode(255)),
)

comment_table = schema.Table('comment', meta.Base.metadata,
    schema.Column('id', types.Integer, schema.Sequence('comment_seq_id', optional=True), primary_key=True),
    schema.Column('pageid', types.Integer, schema.ForeignKey('page.id'), nullable=False),
    schema.Column('content', types.Unicode(255), default=u''),
    schema.Column('name', types.Unicode(255)),
    schema.Column('email', types.Unicode(255), nullable=False),
    schema.Column('created', types.TIMESTAMP(), default=now()),
)

pagetag_table = schema.Table('pagetag', meta.Base.metadata,
    schema.Column('id', types.Integer, schema.Sequence('pagetag_seq_id', optional=True), primary_key=True),
    schema.Column('pageid', types.Integer, schema.ForeignKey('page.id')),
    schema.Column('tagid', types.Integer, schema.ForeignKey('tag.id')),
)
    
tag_table = schema.Table('tag', meta.Base.metadata,
    schema.Column('id', types.Integer, schema.Sequence('tag_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(20), nullable=False, unique=True),
)

class Nav(object):
    @staticmethod
    def add_navigation_node(nav, section, before):
        nav_q = meta.Session.query(Nav)
        new_before = nav_q.filter_by(section=section, before=before).first()
        if new_before is not None and new_before.id != nav.id:
            new_before.before = nav.id
            
    @staticmethod
    def remove_navigation_node(nav):
        nav_q = meta.Session.query(Nav)
        old_before = nav_q.filter_by(section=nav.section, before=nav.id).first()
        if old_before is not None:
            old_before.before = nav.before
            
    @staticmethod
    def nav_to_path(id):
        nav_q = meta.Session.query(Nav)
        nav = nav_q.filter_by(id=id).one()
        path = nav.path
        if nav.type=='section':
            path += '/'
        while nav.section is not None:
            nav = nav_q.filter_by(type='section', id=nav.section).one()
            path = nav.path+'/'+path
        return path
    
    @staticmethod
    def get_before_options(section, exclude=None):
        nav_q = meta.Session.query(Nav)
        query = nav_q.filter_by(section=section)
        if exclude is not None:
            query = query.filter(Nav.id != exclude)
        return [(nav.id, nav.name) for nav in query.all()]

class Page(Nav):
    pass

class Section(Nav):
    pass

class Comment(Nav):
    pass

class Tag(Nav):
    pass

orm.mapper(Comment, comment_table)
orm.mapper(Tag, tag_table)
orm.mapper(Nav, nav_table, polymorphic_on=nav_table.c.type, polymorphic_identity='nav')
orm.mapper(Section, section_table, inherits=Nav, polymorphic_identity='section')
orm.mapper(Page, page_table, inherits=Nav, polymorphic_identity='page', properties={
    'comments':orm.relation(Comment, backref='page', cascade='all'),
    'tags':orm.relation(Tag, secondary=pagetag_table)
})
    