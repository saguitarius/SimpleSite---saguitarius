# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297710350.812
_template_filename=u'D:\\PyProjects\\SimpleSite\\simplesite\\templates/base/index.html'
_template_uri=u'/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'flash', 'title', 'tabs', 'menu', 'footer', 'js', 'header', 'breadcrumbs', 'heading']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace(u'navigation', context._clean_inheritance_tokens(), templateuri=u'/component/navigation.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'navigation')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        next = _import_ns.get('next', context.get('next', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\r\n"http://www.w3.org/TR/html4/strict.dtd">\r\n<html>\r\n<head>\r\n    <title>')
        # SOURCE LINE 8
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\r\n    ')
        # SOURCE LINE 9
        __M_writer(escape(self.head()))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 10
        __M_writer(escape(self.js()))
        __M_writer(u'\r\n</head>\r\n<body>\r\n    <div id="doc3" class="yui-t5">\r\n        <div id="hd">\r\n             <div class="yui-gc">\r\n                 <div class="yui-u first">')
        # SOURCE LINE 16
        __M_writer(escape(self.heading()))
        __M_writer(u'</div>\r\n                 <div class="yui-u"></div>\r\n             </div>\r\n            ')
        # SOURCE LINE 19
        __M_writer(escape(self.header()))
        __M_writer(u'\r\n            ')
        # SOURCE LINE 20
        __M_writer(escape(self.tabs()))
        __M_writer(u'\r\n        </div>\r\n        <div id="bd">\r\n            <div id="yui-main">\r\n                <div class="yui-b">\r\n                    ')
        # SOURCE LINE 25
        __M_writer(escape(self.breadcrumbs()))
        __M_writer(u'\r\n                    ')
        # SOURCE LINE 26
        __M_writer(escape(self.flash()))
        __M_writer(u'\r\n                    ')
        # SOURCE LINE 27
        __M_writer(escape(next.body()))
        __M_writer(u'\r\n                </div>\r\n            </div>\r\n            <div class="yui-b">\r\n                 ')
        # SOURCE LINE 31
        __M_writer(escape(self.menu()))
        __M_writer(u'\r\n            </div>\r\n        </div>\r\n        <div id="ft">\r\n            ')
        # SOURCE LINE 35
        __M_writer(escape(self.footer()))
        __M_writer(u'\r\n        </div>\r\n   </div>\r\n</body>\r\n</html>\r\n\r\n')
        # SOURCE LINE 43
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 48
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 52
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 56
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 60
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 64
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 68
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 72
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 82
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 45
        __M_writer(u'\r\n    ')
        # SOURCE LINE 46
        __M_writer(escape(h.stylesheet_link(h.url('/yui/2.8.2/reset-fonts-grids/reset-fonts-grids.css'))))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 47
        __M_writer(escape(h.stylesheet_link(h.url('/css/main.css'))))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flash(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        session = _import_ns.get('session', context.get('session', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 74
        __M_writer(u'\r\n')
        # SOURCE LINE 75
        if session.has_key('flash'):
            # SOURCE LINE 76
            __M_writer(u'        <div id="flash"><p>')
            __M_writer(escape(session.get('flash')))
            __M_writer(u'</p></div>\r\n        ')
            # SOURCE LINE 77

            del session['flash']
            session.save()
                    
            
            # SOURCE LINE 80
            __M_writer(u'\r\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 41
        __M_writer(u'\r\n    SimpleSite\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabs(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        navigation = _mako_get_namespace(context, 'navigation')
        __M_writer = context.writer()
        # SOURCE LINE 54
        __M_writer(u'\r\n    ')
        # SOURCE LINE 55
        __M_writer(escape(navigation.tabs()))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        navigation = _mako_get_namespace(context, 'navigation')
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\r\n    ')
        # SOURCE LINE 59
        __M_writer(escape(navigation.menu()))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 70
        __M_writer(u'\r\n    <p><a href="#top">Top ^</a></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 84
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\r\n    <a name="top"></a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        navigation = _mako_get_namespace(context, 'navigation')
        __M_writer = context.writer()
        # SOURCE LINE 66
        __M_writer(u'\r\n    ')
        # SOURCE LINE 67
        __M_writer(escape(navigation.breadcrumbs()))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 62
        __M_writer(u'\r\n    <h1>')
        # SOURCE LINE 63
        __M_writer(escape(c.heading or 'No Title'))
        __M_writer(u'</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


