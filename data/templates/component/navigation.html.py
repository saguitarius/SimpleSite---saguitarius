# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1297688404.181
_template_filename=u'D:\\PyProjects\\SimpleSite\\simplesite\\templates/component/navigation.html'
_template_uri=u'/component/navigation.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['breadcrumbs_body', 'tabs_body', 'render_breadcrumbs', 'tabs', 'menu', 'render_list', 'menu_body', 'breadcrumbs']


# SOURCE LINE 1

import simplesite.model as model
import sys


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\r\n')
        # SOURCE LINE 9
        __M_writer(u'\r\n')
        # SOURCE LINE 18
        __M_writer(u'\r\n\r\n\r\n')
        # SOURCE LINE 28
        __M_writer(u'\r\n')
        # SOURCE LINE 37
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 49
        __M_writer(u'\r\n')
        # SOURCE LINE 58
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 71
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs_body(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        def render_breadcrumbs(breadcrumbs):
            return render_render_breadcrumbs(context,breadcrumbs)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\r\n')
        # SOURCE LINE 6
        if c.page and c.page.id != 1:
            # SOURCE LINE 7
            __M_writer(u'    <div id="breadcrumbs"><p>')
            __M_writer(escape(render_breadcrumbs(c.breadcrumbs)))
            __M_writer(u'</p></div>\r\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabs_body(context):
    context.caller_stack._push_frame()
    try:
        def render_list(items,current,type_,id,class_):
            return render_render_list(context,items,current,type_,id,class_)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\r\n    <div id="maintabs">\r\n        <ul class="draglist">\r\n            ')
        # SOURCE LINE 24
        __M_writer(escape(render_list(c.tabs, c.breadcrumbs[1].path,
                type_=c.breadcrumbs[1].type, id='li1_', class_='list2')))
        # SOURCE LINE 25
        __M_writer(u'\r\n        </ul>\r\n    </div>    \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_breadcrumbs(context,breadcrumbs):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(u'\r\n')
        # SOURCE LINE 74
        for i, item in enumerate(breadcrumbs):
            # SOURCE LINE 75
            if i < len(breadcrumbs) - 1:
                # SOURCE LINE 76
                __M_writer(u'        <a href="')
                __M_writer(escape(item.path_info))
                __M_writer(u'">')
                __M_writer(escape(item.name))
                __M_writer(u'</a> &gt;\r\n')
                # SOURCE LINE 77
            elif isinstance(c.breadcrumbs[-1], model.Section):
                # SOURCE LINE 78
                __M_writer(u'        ')
                __M_writer(escape(item.name))
                __M_writer(u' &gt;\r\n')
                # SOURCE LINE 79
            else:
                # SOURCE LINE 80
                __M_writer(u'        ')
                __M_writer(escape(item.name))
                __M_writer(u'\r\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabs(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        def tabs_body():
            return render_tabs_body(context)
        __M_writer = context.writer()
        # SOURCE LINE 29
        __M_writer(u'\r\n    ')
        # SOURCE LINE 30

        try:
            c.tabs
            tabs_body()
        except:
            pass
            
        
        # SOURCE LINE 36
        __M_writer(u'     \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        def menu_body():
            return render_menu_body(context)
        __M_writer = context.writer()
        # SOURCE LINE 50
        __M_writer(u'\r\n    ')
        # SOURCE LINE 51

        try:
            c.breadcrumbs
            menu_body()
        except:
            pass
            
        
        # SOURCE LINE 57
        __M_writer(u'     \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_list(context,items,current,type_,id,class_):
    context.caller_stack._push_frame()
    try:
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 60
        __M_writer(u'\r\n')
        # SOURCE LINE 61
        for item in items:
            # SOURCE LINE 62
            if item.path == current and item.type == type_:
                # SOURCE LINE 63
                __M_writer(u'<li class="')
                __M_writer(escape(class_))
                __M_writer(u' active" id="')
                __M_writer(escape(id))
                __M_writer(escape(str(item.id)))
                __M_writer(u'"><span class="current"><a\r\n    href="')
                # SOURCE LINE 64
                __M_writer(escape(item.path_info))
                __M_writer(u'" id="current">')
                __M_writer(escape(item.name))
                __M_writer(u'</a></span></li>')
                # SOURCE LINE 65
            else:
                # SOURCE LINE 66
                __M_writer(u'<li class="')
                __M_writer(escape(class_))
                __M_writer(u'" id="')
                __M_writer(escape(id))
                __M_writer(escape(str(item.id)))
                __M_writer(u'"\r\n    onclick="document.location =\'')
                # SOURCE LINE 67
                __M_writer(escape(item.path_info))
                __M_writer(u'\'"\r\n><span><a href="')
                # SOURCE LINE 68
                __M_writer(escape(item.path_info))
                __M_writer(u'">')
                __M_writer(escape(item.name))
                __M_writer(u'</a></span></li>')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_body(context):
    context.caller_stack._push_frame()
    try:
        def render_list(items,current,type_,id,class_):
            return render_render_list(context,items,current,type_,id,class_)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\r\n')
        # SOURCE LINE 40
        if len(c.breadcrumbs) > 2:
            # SOURCE LINE 41
            __M_writer(u'        <div id="menu">\r\n            <h2>Section Links</h2>\r\n            <ul class="draglist">\r\n                ')
            # SOURCE LINE 44
            __M_writer(escape(render_list(c.menu, c.breadcrumbs[-1].path,
                    type_=c.breadcrumbs[1].type, id='li1_', class_='list2')))
            # SOURCE LINE 45
            __M_writer(u'\r\n            </ul>\r\n        </div>\r\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context):
    context.caller_stack._push_frame()
    try:
        def breadcrumbs_body():
            return render_breadcrumbs_body(context)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\r\n    ')
        # SOURCE LINE 11

        try:
            c.page
            breadcrumbs_body()
        except:
            pass
            
        
        # SOURCE LINE 17
        __M_writer(u'     \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


