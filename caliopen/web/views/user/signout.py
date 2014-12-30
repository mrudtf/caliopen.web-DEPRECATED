#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

import logging
log = logging.getLogger(__name__)

messages = {
        'successfully_signed_out': 'You successfully signed out'
    }

@view_config(route_name='user.signout', request_method='GET')
def signout(self, request):
    # clear current user session
    request.session.invalidate()
    # XXX activate flash message once
    # https://github.com/Gandi/pyramid_kvs/issues/1 is resolved
    #request.session.flash(messages['successfully_signed_out'], queue='info')
    url = request.route_url('user.redirect_after_signout')
    return HTTPFound(location=url)
