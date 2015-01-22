#-*- coding: utf-8 -*-

from __future__ import unicode_literals


import logging
log = logging.getLogger(__name__)

def includeme(config):
    """
    Declaration related to application general behaviour
    """
    log.debug('Declare open.web.app routes')

    config.add_route('app.index', '/app/')
    config.add_route('app.public', '/')

    config.scan('.index')
