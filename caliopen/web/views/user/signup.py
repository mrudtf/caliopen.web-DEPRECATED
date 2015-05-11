# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from collections import namedtuple

from pyramid.view import view_defaults
from pyramid.view import view_config

from caliopen.web.views import redirect
from caliopen.base.user.core import User
from caliopen.base.user.parameters import NewUser
from caliopen.base.user.parameters import NewContact

import logging
log = logging.getLogger(__name__)

messages = {
        'password_missmatch': 'Provided password does not match'
    }

@view_defaults(route_name='user.signup')
class SinginView(object):
    """Handles 'user.signup' related routes"""
    def __init__(self, request):
        self.request = request

    @view_config(request_method='GET', renderer='user/signup.html')
    def signup(self):
        username = sanitize_username(self.request)
        email = sanitize_email(self.request)
        return {
                'username': username,
                'email': email,
                'errors': None
            };

    @view_config(request_method='POST', renderer='user/signup.html')
    def handle_signup(self):
        # Validate request
        username = sanitize_username(self.request)
        email = sanitize_email(self.request)
        password = sanitize_password(self.request)
        password_repeat = sanitize_password(self.request, 'password_repeat')
        creation = validate_signup_params( username=username,
                                           email=email,
                                           password=password,
                                           password_repeat=password_repeat)

        # Handle successful request
        if creation.success is True:
            authenticate_user(self.request, creation.user)
            return redirect(self.request, 'user.redirect_after_signup')

        # Handle error request
        self.request.status_int = 400
        return {
                'username': username,
                'errors': creation.errors
            }


# FIXME
# Migrate validation logic in `caliopen.web.user_creation.validation`
# Just as `caliopen.web.authentication.validation`

def sanitize_username(request):
    """Sanitize username parameter from request"""
    if 'username' in request.params:
        return request.params['username'].encode('utf-8')
    return ''

def sanitize_email(request):
    """Sanitize email parameter from request"""
    if 'email' in request.params:
        return request.params['email'].encode('utf-8')
    return ''

def sanitize_password(request, param_name='password'):
    """Sanitize password parameter from request"""
    if param_name in request.params:
        return request.params[param_name].encode('utf-8')
    return ''

def validate_signup_params(username, email, password, password_repeat, given_name='', family_name=''):
    """Retrieve matching username and password.
    If no match is found, then return errors.

    @param string username
    @param string password
    @return Authentication
    """
    creation = namedtuple('Creation', ['success', 'user', 'errors'])
    errors = {
            'globals': [],
            'given_name': [],
            'family_name': [],
            'username': [],
            'password': [],
            'password_repeat': []
        }

    # validate user input
    has_error = False;
    if not password == password_repeat:
        errors['password_repeat'].append(messages['password_missmatch'])
        has_error = True

    # if an error occurred, then return the failed attempt
    if has_error:
        return creation(success=False, errors=errors, user=None)

    # create the user from parameters
    try:
        param = NewUser()
        param.name = email
        param.password = password
        contact = NewContact()
        contact.given_name = given_name
        contact.family_name = family_name
        param.contact = contact
        user = User.create(param)
        user.save()
        user = user.to_api()
        return  creation(success=True, user=user, errors=None)

    except (KeyError, Exception), exc:
        # prepare errors
        errors['globals'].append(str(exc))
        return creation(success=False, errors=errors, user=None)

def authenticate_user(request, user):
    """Persist provided user authentication into session
    """
    # activate user in session
    request.session['user'] = user['id']
