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

def includeme(config=None):
    if config:
        settings = config.registry.settings

        # Configure local templates
        template_path = join(dirname(abspath(__file__)), 'templates')
        assets_path = settings['caliopen.assets.path']
        frontend_template_path = dirname(dirname(assets_path))

        config.add_jinja2_renderer('.html')
        config.add_jinja2_search_path(template_path, name='.html')

        # Retrieve ember assets path.
        # templates should be located in a directory named "frontend" as
        # this is used as template prefix.
        config.add_static_view(name='/app/', path=assets_path)
        log.debug('Will serve "frontend" assets from %s' % assets_path)
        # index is prefixed by frontend

        config.add_jinja2_search_path(frontend_template_path, name='.html')

        config.add_notfound_view(notfound, append_slash=True)

