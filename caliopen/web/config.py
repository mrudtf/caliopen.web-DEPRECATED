#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import


def includeme(config):
    settings = config.registry.settings

    # XXX should be removed
    # configure templates dir (angular build dir)
    template_path = settings['caliopen.ng.path']
    config.add_jinja2_renderer('.html')
    config.add_jinja2_search_path(template_path, name='.html')

    # configure static dir on the same dir (angular build dir)
    config.add_static_view('/static', template_path)
