# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297710350.7920001
_template_filename='D:\\PyProjects\\SimpleSite\\simplesite\\templates/derived/page/view.html'
_template_uri='/derived/page/view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['footer', 'menu', 'tags', 'js', 'title', 'heading']


# SOURCE LINE 16

from formencode import htmlfill
from webhelpers.html import literal


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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 3
        __M_writer(u'\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 6
        __M_writer(escape(c.page.content))
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 14
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 19
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 26
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 55
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\r\n')
        # SOURCE LINE 30
        __M_writer(u'<p>\r\n  <a href="')
        # SOURCE LINE 31
        __M_writer(escape(h.url(controller='page', action='list')))
        __M_writer(u'">All Pages</a>\r\n| <a href="')
        # SOURCE LINE 32
        __M_writer(escape(h.url(controller='page', action='new')))
        __M_writer(u'">New Page</a>\r\n| <a href="')
        # SOURCE LINE 33
        __M_writer(escape(h.url(controller='page', action='edit', id=c.page.id)))
        __M_writer(u'">Edit Page</a>\r\n| <a href="')
        # SOURCE LINE 34
        __M_writer(escape(h.url(controller='page', action='delete', id=c.page.id)))
        __M_writer(u'">Delete Page</a>\r\n</p>\r\n')
        # SOURCE LINE 37
        __M_writer(u'<p>\r\n  <a href="')
        # SOURCE LINE 38
        __M_writer(escape(h.url(pageid=c.page.id, controller='comment',
action='list')))
        # SOURCE LINE 39
        __M_writer(u'">Comments (')
        __M_writer(escape(str(c.comment_count)))
        __M_writer(u')</a>\r\n| <a href="')
        # SOURCE LINE 40
        __M_writer(escape(h.url(pageid=c.page.id, controller='comment',
action='new')))
        # SOURCE LINE 41
        __M_writer(u'">Add Comment</a>\r\n</p>\r\n')
        # SOURCE LINE 44
        __M_writer(u'<p>\r\n  <a href="')
        # SOURCE LINE 45
        __M_writer(escape(h.url(controller='section', action='new', section=c.page.section, before=c.page.before)))
        __M_writer(u'">New Section</a>\r\n| <a href="')
        # SOURCE LINE 46
        __M_writer(escape(h.url(controller='section', action='edit', id=c.page.section)))
        __M_writer(u'">Edit Section</a>\r\n| <a href="')
        # SOURCE LINE 47
        __M_writer(escape(h.url(controller='section', action='delete', id=c.page.section)))
        __M_writer(u'">Delete Section and Index Page</a>\r\n</p>\r\n\r\n')
        # SOURCE LINE 51
        __M_writer(u'<p><a href="')
        __M_writer(escape(h.url(controller='tag', action='list')))
        __M_writer(u'">All Tags</a>\r\n| <a href="')
        # SOURCE LINE 52
        __M_writer(escape(h.url(controller='tag', action='new')))
        __M_writer(u'">Add Tag</a></p>\r\n')
        # SOURCE LINE 54
        __M_writer(escape(parent.footer()))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        capture = context.get('capture', UNDEFINED)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\r\n')
        # SOURCE LINE 22
        __M_writer(escape(parent.menu()))
        __M_writer(u'\r\n')
        # SOURCE LINE 23
        if c.available_tags:
            # SOURCE LINE 24
            __M_writer(escape(literal(htmlfill.render(capture(self.tags, c.available_tags), c.selected_tags))))
            __M_writer(u'\r\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tags(context,available_tags):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'\r\n    <h2>Tags</h2>\r\n    ')
        # SOURCE LINE 10
        __M_writer(escape(h.form_start(h.url(controller='page', action='update_tags', id=c.page.id), method='post')))
        __M_writer(u'\r\n        ')
        # SOURCE LINE 11
        __M_writer(escape(h.checkbox_group(name='tags', selected_values=None, align="vert", options=available_tags)))
        __M_writer(u'\r\n        ')
        # SOURCE LINE 12
        __M_writer(escape(h.submit(value="Save Tags", name='submit')))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 13
        __M_writer(escape(h.form_end()))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        session = context.get('session', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\r\n    <script src="/yui/2.8.2/yahoo-dom-event/yahoo-dom-event.js" type="text/javascript"></script>\r\n    <script src="/yui/2.8.2/animation/animation-min.js" type="text/javascript"></script>\r\n')
        # SOURCE LINE 60
        if session.has_key('flash'):
            # SOURCE LINE 61
            __M_writer(u'    <script type="text/javascript">\r\n    YAHOO.util.Event.onAvailable(\r\n        \'flash\',\r\n        function() {\r\n            var a = new YAHOO.util.Anim(\r\n                YAHOO.util.Dom.get(\'flash\'), {\r\n                    height: {\r\n                        to: 16\r\n                    }\r\n                },\r\n                0.4,\r\n                YAHOO.util.Easing.easeIn\r\n            );\r\n            a.animate();\r\n            YAHOO.util.Event.on(\'flash\', \'click\', function() {\r\n                    var b = new YAHOO.util.Anim(\r\n                        YAHOO.util.Dom.get(\'flash\'), {\r\n                            opacity: {\r\n                                to: 0\r\n                            },\r\n                        },\r\n                        0.4\r\n                    );\r\n                    b.onComplete.subscribe(function(){\r\n                        YAHOO.util.Dom.setStyle(\'flash\', \'display\', \'none\');\r\n                    });\r\n                    b.animate();\r\n                }\r\n            )\r\n        }\r\n    );\r\n    </script>\r\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(escape(c.page.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>')
        __M_writer(escape(c.page.heading or c.page.title))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


