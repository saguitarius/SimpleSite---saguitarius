# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297450267.645
_template_filename=u'D:\\PyProjects\\SimpleSite\\simplesite\\templates/derived/comment/fields.html'
_template_uri=u'/derived/comment/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(escape(h.field(
    "Name",
    h.text(name='name'),
    required=False,
)))
        # SOURCE LINE 5
        __M_writer(u'\r\n')
        # SOURCE LINE 6
        __M_writer(escape(h.field(
    "Email",
    h.text(name='email'),
    required=True,
    field_desc = 'Use to help prevent spam but will not be published'
)))
        # SOURCE LINE 11
        __M_writer(u'\r\n')
        # SOURCE LINE 12
        __M_writer(escape(h.field(
    "Comment",
    h.textarea(name='content', rows=7, cols=40),
    required=True,
)))
        return ''
    finally:
        context.caller_stack._pop_frame()


