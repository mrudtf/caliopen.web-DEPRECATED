#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from pyramid.view import view_config

from caliopen.web.views import redirect
from caliopen.web.authentication.authenticate import unauthenticate_user

import logging
log = logging.getLogger(__name__)

messages = {
        'successfully_signed_out': 'You successfully signed out'
    }

@view_config(route_name='user.signout', request_method='GET')
def signout(self, request):
    # clear current user session
    unauthenticate_user(request)
    request.session.flash(messages['successfully_signed_out'], queue='info')
    return redirect(request, 'user.redirect_after_signout')
