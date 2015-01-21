#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_defaults
from pyramid.view import view_config

from caliopen.web.authentication.authenticate import authenticate_user
from caliopen.web.authentication.validation import validate

import logging
log = logging.getLogger(__name__)

@view_defaults(route_name='user.signin')
class SinginView(object):
    """Handles 'user.signin' related routes"""
    def __init__(self, request):
        self.request = request

        self.username = request.params['username'] if 'username' in request.params else ''
        self.password = request.params['password'] if 'password' in request.params else ''

    @view_config(request_method='GET', renderer='user/signin.html')
    def signin(self):
        """Display the signin form"""

        return {
                # Retrieve username if any
                'username': self.username,
                'errors': None
            };

    @view_config(request_method='POST', renderer='user/signin.html')
    def handle_signin(self):
        """Validate the user request"""

        # Validate request
        authentication = validate(self.username, self.password)

        # Handle successful request
        if authentication.success is True:
            authenticate_user(self.request, authentication.user)
            url = self.request.route_url('user.redirect_after_signin')
            return HTTPFound(location=url)

        # Handle error request
        self.request.status_int = 400
        return {
                'username':  self.username,
                'errors': authentication.errors
            }


