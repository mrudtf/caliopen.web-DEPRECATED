#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from urlparse import urlparse

from pyramid.httpexceptions import HTTPFound

import logging
log = logging.getLogger(__name__)

def redirect(request, route, **kwargs):
    """Redirect to route name

    :request: pyramid.request
    :route: string the route name
    :returns: pyramid.httpexceptions.HTTPFound

    """

    parsed = urlparse(request.host_url)

    scheme = request.headers.get('X-Forwarded-Proto', parsed.scheme)
    port = request.headers.get('X-Forwarded-Port', parsed.port)
    host = request.headers.get('X-Forwarded-Host', parsed.hostname)

    if port:
        url = request.route_url(route, _port=port, _host=host, _scheme=scheme, **kwargs)
    else:
        url = request.route_url(route, _host=host, _scheme=scheme, **kwargs)

    log.debug(url)

    return HTTPFound(location=url)
