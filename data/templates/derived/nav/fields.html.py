# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297711924.8239999
_template_filename=u'D:\\PyProjects\\SimpleSite\\simplesite\\templates/derived/nav/fields.html'
_template_uri=u'/derived/nav/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['js']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(escape(h.field(
    "Name",
    h.text(name='name'),
    required=True,
)))
        # SOURCE LINE 5
        __M_writer(u'\r\n')
        # SOURCE LINE 6
        __M_writer(escape(h.field(
    "Path",
    h.text(name='path'),
    required=True,
)))
        # SOURCE LINE 10
        __M_writer(u'\r\n')
        # SOURCE LINE 11
        __M_writer(escape(h.field(
    'Section',
    h.select(
        "section",
        id='section',
        selected_values=[],
        options=c.available_sections,
        onchange="callAjax('%s', 'section', 'before'); return false;"%(
            h.url(controller="nav", action="before_field_json")
        ),
    ),
    required=True
)))
        # SOURCE LINE 23
        __M_writer(u'\r\n')
        # SOURCE LINE 24
        __M_writer(escape(h.field(
    "Before",
    h.select(
        "before",
        id='before',
        options = c.before_options,
        selected_values=[],
    ),
)))
        # SOURCE LINE 32
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\r\n    <script src="/yui/2.8.2/yahoo-dom-event/yahoo-dom-event.js" type="text/javascript"></script>\r\n    <script src="/yui/2.8.2/connection/connection-min.js" type="text/javascript"></script>\r\n    <script src="/yui/2.8.2/json/json-min.js" type="text/javascript"></script>\r\n\r\n    <script type="text/javascript">\r\n    function callAjax(url, field, replace){\r\n        var callback = {\r\n            success: function(o) {\r\n                var parsed_options = YAHOO.lang.JSON.parse(o.responseText);\r\n                var before = document.getElementById(replace);\r\n                // Remove current options\r\n                while(before.hasChildNodes() === true)\r\n                {\r\n                    before.removeChild(before.childNodes[0]);\r\n                }\r\n                // Add new options\r\n                for (var i=0; i<parsed_options.options.length; i++) {\r\n                    var new_option = document.createElement(\'option\');\r\n                    new_option.text = parsed_options.options[i].id;\r\n                    new_option.value =  parsed_options.options[i].value;\r\n                    before.appendChild(new_option);\r\n                }\r\n            },\r\n            failure: function(o) {\r\n                alert("Failed to retrieve required information.");\r\n            }\r\n        }\r\n        url = url +\'?selected=\'+YAHOO.util.Dom.get(field).value;\r\n        var transaction = YAHOO.util.Connect.asyncRequest(\'GET\', url, callback, null);\r\n    }\r\n    </script>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


