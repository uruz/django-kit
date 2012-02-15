# -*- coding:utf-8 -*-
from django.contrib.sites.models import get_current_site
from django.core.urlresolvers import resolve, Resolver404
from django.forms.widgets import Media

def uni_form_media(request):
    media = Media(css = {'all': ('uni_form/uni-form.css',
                                 'uni_form/default.uni-form.css'
                        )},
            js = ('uni_form/uni-form.jquery.js',)
    )
    return {'uni_form_media': media}

def js_csrf(request):
    media = Media(js=('django_kit/csrf.js',))
    return {'js_csrf': media}

def site(request):
    return {'site': get_current_site(request)}

def view_name(request):
    try:
        resolver_match = resolve(request.path_info)
        return {'view_name': resolver_match.url_name}
    except Resolver404:
        return {}