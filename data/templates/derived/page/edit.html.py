# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297970130.7539999
_template_filename='D:\\PyProjects\\SimpleSite\\simplesite\\templates/derived/page/edit.html'
_template_uri='/derived/page/edit.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'heading', 'js']


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

    # SOURCE LINE 16
    ns = runtime.Namespace(u'navfields', context._clean_inheritance_tokens(), templateuri=u'/derived/nav/fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'navfields')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'navfields')._populate(_import_ns, [u'js'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        request = _import_ns.get('request', context.get('request', UNDEFINED))
        fields = _mako_get_namespace(context, 'fields')
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n')
        # SOURCE LINE 2
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 6
        __M_writer(u'\r\n\r\n<p>Editing the source code for the ')
        # SOURCE LINE 8
        __M_writer(escape(c.page.title))
        __M_writer(u' page:</p>\r\n\r\n')
        # SOURCE LINE 10
        __M_writer(escape(h.form_start(h.url(controller='page', action='save',
    id=request.urlvars['id']), method="post")))
        # SOURCE LINE 11
        __M_writer(u'\r\n    ')
        # SOURCE LINE 12
        __M_writer(escape(fields.body()))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 13
        __M_writer(escape(h.field(field=h.submit(value="Save Changes", name='submit'))))
        __M_writer(u'\r\n')
        # SOURCE LINE 14
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 16
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 52
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'navfields')._populate(_import_ns, [u'js'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 54
        __M_writer(u'\r\n    ')
        # SOURCE LINE 55
        __M_writer(escape(parent.head()))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 56
        __M_writer(escape(h.stylesheet_link(h.url('/yui/2.8.2/assets/skins/sam/skin.css'))))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'navfields')._populate(_import_ns, [u'js'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\r\n    <h1 class="main">Editing ')
        # SOURCE LINE 5
        __M_writer(escape(c.page.title))
        __M_writer(u'</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'fields')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'navfields')._populate(_import_ns, [u'js'])
        navfields = _mako_get_namespace(context, 'navfields')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\r\n    ')
        # SOURCE LINE 19
        __M_writer(escape(parent.js()))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 20
        __M_writer(escape(navfields.js()))
        __M_writer(u'\r\n\r\n    <script type="text/javascript"\r\n        src="/yui/2.8.2/element/element-min.js"></script>\r\n    <script type="text/javascript"\r\n        src="/yui/2.8.2/container/container_core-min.js"></script>\r\n    <script type="text/javascript"\r\n        src="/yui/2.8.2/editor/simpleeditor-min.js"></script>\r\n\r\n    <script type="text/javascript">\r\n    (function() {\r\n        // Set up some private variables\r\n        var Dom = YAHOO.util.Dom;\r\n        var Event = YAHOO.util.Event;\r\n\r\n        // The SimpleEditor config\r\n        var myConfig = {\r\n            height: \'200px\',\r\n            width: \'630px\',\r\n            dompath: true,\r\n            focusAtStart: true,\r\n            handleSubmit: true\r\n        };\r\n\r\n        // Now let\'s load the SimpleEditor..\r\n        var myEditor = new YAHOO.widget.SimpleEditor(\'editor\', myConfig);\r\n        myEditor._defaultToolbar.buttonType = \'advanced\';\r\n        document.e = myEditor;\r\n        myEditor._defaultToolbar.titlebar = \'Rich Text Editor\';\r\n        myEditor.render();\r\n    })();\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


