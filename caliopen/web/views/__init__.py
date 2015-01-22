#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from pyramid.httpexceptions import HTTPFound

def redirect(request, route):
    """Redirect to route name

    :request: pyramid.request
    :route: string the route name
    :returns: pyramid.httpexceptions.HTTPFound

    """
    scheme = request.headers.get('X-Forwarded-Proto', 'http')
    port = request.headers.get('X-Forwarded-Port', 443 if scheme == 'https' else 80)

    url = request.route_url(route, _port=port, _scheme=scheme)

    return HTTPFound(location=url)
