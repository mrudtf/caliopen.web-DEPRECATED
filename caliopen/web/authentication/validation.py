#-*- coding: utf-8 -*-
#
# Authentication Validation
# =========================
#
# Provides tools to vlaidate user inputs concerning user authentication.
#

from __future__ import unicode_literals

from schematics.models import Model
from schematics.types import StringType
from schematics.exceptions import ValidationError

from collections import namedtuple;

from caliopen.core.user import User

from pyramid.i18n import TranslationString

import logging
log = logging.getLogger(__name__)

class CredentialException(Exception):
    pass

MESSAGES = {
    'field_required': 'This field is required'
}

validation_messages = {
    'required': MESSAGES['field_required'],
    'min_length': MESSAGES['field_required']
}

class AuthenticationParams(Model):
    """
    Validation class for Authentication data

    This is expected to remains internal.
    """

    username = StringType(required=True, min_length=1, messages=validation_messages)
    password = StringType(required=True, min_length=1, messages=validation_messages)


def _validate_authentication_params(username, password):
    """
    Validate provided authentication parameters.

    Any validation error throws a `ValidationError`.

    @param string username provided username
    @param string password provided password
    @return dict sanitized params
    """
    params = {'username': username, 'password': password }
    auth = AuthenticationParams(params)

    auth.validate()

    return auth

def _validate_authentication_credentials(params):
    """
    Check the user credentials and returns the associated user object.

    @param dict params  the sanitized parameters for authentication
    @return user
    """
    try:
        user = User.authenticate(params['username'], params['password'])
        user = user.to_api()

    except ValidationError, e:
        raise ValidationError(e.messages)

    except Exception, e:
        # It appears the User.authenticate method throws an Exception
        # error if password does not match
        raise CredentialException()

    return user;


def validate(username, password):
    """
    Validate provided form values

    @param string username
    @param string password
    @return Authentication
    """

    authentication = namedtuple('Authentication', ['success', 'user', 'errors'])

    try:
        params = _validate_authentication_params(username, password)
        user = _validate_authentication_credentials(params)

        return  authentication(success=True, user=user, errors=None)

    except (ValidationError), exc:
        errors = exc.messages
        log.debug(exc)
        return authentication(success=False, errors=errors, user=None)

    except (CredentialException), exc:
        errors = {
                'globals': ['Unable to authenticate with provided credentials']
            }
        return authentication(success=False, errors=errors, user=None)

    except (Exception), exc:
        log.debug(exc);
        # this is an unexpected error, let's rethrow
        raise exc

