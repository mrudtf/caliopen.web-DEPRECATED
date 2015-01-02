#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
log = logging.getLogger(__name__)

def includeme(config):
    """Add user authentication and creation related views.
    Handles subscription, connection and password retrieval.
    """
    log.debug('Declare routes')

    config.add_route('user.signin', '/signin')
    config.add_route('user.signout', '/signout')
    config.add_route('user.signup', '/signup')
    config.add_route('user.password_resend', '/login/password-resend')
    config.add_route('user.redirect_after_signout', '/signin')
    config.add_route('user.redirect_after_signin', '/')
    config.add_route('user.redirect_after_signup', '/')

    config.scan('.signin')
    config.scan('.signout')
    config.scan('.signup')

