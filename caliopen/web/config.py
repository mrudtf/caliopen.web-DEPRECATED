#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from os.path import abspath
from os.path import dirname
from os.path import join

from pyramid.httpexceptions import HTTPNotFound

import logging
log = logging.getLogger(__name__)

def notfound(request):
    """
    A default view to handle not found exception
    """
    return HTTPNotFound('Not found.')

def includeme(config):
    settings = config.registry.settings

    # Configure local templates
    config.add_jinja2_renderer('.html')
    template_path = join(dirname(abspath(__file__)), 'templates')
    config.add_jinja2_search_path(template_path, name='.html')

    # Retrieve ember assets path.
    assets_path = settings['caliopen.assets.path']
    config.add_static_view(name='frontend', path=assets_path)
    log.debug('Will serve "frontend" assets from %s' % assets_path)

    config.add_notfound_view(notfound, append_slash=True)
