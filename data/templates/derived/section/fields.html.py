# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297623897.569
_template_filename=u'D:\\PyProjects\\SimpleSite\\simplesite\\templates/derived/section/fields.html'
_template_uri=u'/derived/section/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace(u'fields', context._clean_inheritance_tokens(), templateuri=u'/derived/nav/fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'fields')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        fields = _mako_get_namespace(context, 'fields')
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        # SOURCE LINE 3
        __M_writer(escape(fields.body()))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


