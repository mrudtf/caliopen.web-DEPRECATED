#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from collections import namedtuple;

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_defaults
from pyramid.view import view_config

from caliopen.core.user import User

import logging
log = logging.getLogger(__name__)

@view_defaults(route_name='user.signin')
class SinginView(object):
    """Handles 'user.signin' related routes"""
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET', renderer='user/signin.html')
    def signin(self):
        username = sanitize_username(self.request)
        return {
                'username': username,
                'errors': None
            };

    @view_config(request_method='POST', renderer='user/signin.html')
    def handle_signin(self):
        # Validate request
        username = sanitize_username(self.request)
        password = sanitize_password(self.request)
        authentication = validate_signin_params(username, password)

        # Handle successful request
        if authentication.success is True:
            authenticate_user(self.request, authentication.user)
            url = self.request.route_url('user.redirect_after_signin')
            return HTTPFound(location=url)

        # Handle error request
        self.request.status_int = 400
        return {
                'username': username,
                'errors': authentication.errors
            }



def sanitize_username(request):
    """Sanitize username parameter from request"""
    if 'username' in request.params:
        return request.params['username']
    return ''

def sanitize_password(request):
    """Sanitize password parameter from request"""
    if 'password' in request.params:
        return request.params['password']
    return ''

def validate_signin_params(username, password):
    """Retrieve matching username and password.
    If no match is found, then return errors.

    @param string username
    @param string password
    @return Authentication
    """
    authentication = namedtuple('Authentication', ['success', 'user', 'errors'])

    try:
        user = User.authenticate(username, password)
        user = user.to_api()
        return  authentication(success=True, user=user, errors=None)

    except (KeyError, Exception), exc:
        # prepare errors
        errors = {
                'globals': [str(exc)],
                'username': [],
                'password': []
            }
        return authentication(success=False, errors=errors, user=None)


def authenticate_user(request, user):
    """Persist provided user authentication into session
    """
    # activate user in session
    request.session['user'] = user['id']
