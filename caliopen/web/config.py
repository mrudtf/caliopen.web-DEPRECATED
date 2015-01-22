#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from os.path import abspath
from os.path import dirname
from os.path import join

def includeme(config):
    settings = config.registry.settings

    # Configure local templates
    config.add_jinja2_renderer('.html')
    template_path = join(dirname(abspath(__file__)), 'templates')
    config.add_jinja2_search_path(template_path, name='.html')

    # Retrieve assets path.
    assets_path = settings['caliopen.assets.path']
