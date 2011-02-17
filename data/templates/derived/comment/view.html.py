# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297697312.8269999
_template_filename='D:\\PyProjects\\SimpleSite\\simplesite\\templates/derived/comment/view.html'
_template_uri='/derived/comment/view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['footer', 'heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 6
        __M_writer(escape(c.comment.content))
        __M_writer(u'\r\n\r\n<p><em>Posted by ')
        # SOURCE LINE 8
        __M_writer(escape(c.comment.name))
        __M_writer(u' on ')
        __M_writer(escape(c.comment.created.strftime('%c')))
        __M_writer(u'.</em></p>\r\n\r\n<p><a href="')
        # SOURCE LINE 10
        __M_writer(escape(h.url('path',
id=c.comment.pageid)))
        # SOURCE LINE 11
        __M_writer(u'">Visit the page this comment was posted on.</a></p>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\r\n')
        # SOURCE LINE 15
        __M_writer(u'<p>\r\n<a href="')
        # SOURCE LINE 16
        __M_writer(escape(h.url(pageid=c.page.id, controller='comment', action='edit',
id=c.comment.id)))
        # SOURCE LINE 17
        __M_writer(u'">Edit Comment</a>\r\n| <a href="')
        # SOURCE LINE 18
        __M_writer(escape(h.url(pageid=c.page.id, controller='comment', action='delete',
id=c.comment.id)))
        # SOURCE LINE 19
        __M_writer(u'">Delete Comment</a>\r\n</p>\r\n')
        # SOURCE LINE 22
        __M_writer(escape(parent.footer()))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>Comment</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Comment')
        return ''
    finally:
        context.caller_stack._pop_frame()


