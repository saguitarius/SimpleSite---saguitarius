# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1298045612.8770001
_template_filename='D:\\PyProjects\\SimpleSite\\simplesite\\templates/derived/account/register.html'
_template_uri='/derived/account/register.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['user_exists_print', 'user_exists', 'heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace(u'fields', context._clean_inheritance_tokens(), templateuri=u'fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'fields')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        fields = _mako_get_namespace(context, 'fields')
        def user_exists():
            return render_user_exists(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n')
        # SOURCE LINE 2
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n')
        # SOURCE LINE 5
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 7
        __M_writer(escape(user_exists()))
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 9
        __M_writer(escape(h.form_start(h.url(controller='account', action='register'), method="post")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 10
        __M_writer(escape(fields.body()))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 11
        __M_writer(escape(h.field(field=h.submit(value="Submit", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 12
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n    \r\n')
        # SOURCE LINE 16
        __M_writer(u'    \r\n    \r\n')
        # SOURCE LINE 26
        __M_writer(u'    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_exists_print(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\r\n    <p>Username <b>')
        # SOURCE LINE 15
        __M_writer(escape(c.username))
        __M_writer(u'</b> already exists.</p>    \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_user_exists(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        def user_exists_print():
            return render_user_exists_print(context)
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\r\n    ')
        # SOURCE LINE 19

        try:
            c.username
            user_exists_print()
        except:
            pass
            
        
        # SOURCE LINE 25
        __M_writer(u'     \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'<h1>Registration</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'Registration')
        return ''
    finally:
        context.caller_stack._pop_frame()


