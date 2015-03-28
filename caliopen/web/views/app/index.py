from __future__ import unicode_literals

from pyramid.view import view_defaults
from pyramid.view import view_config

from caliopen.web.authentication.authenticate import is_user_authenticated
from caliopen.web.views import redirect

import logging
log = logging.getLogger(__name__)



class AuthenticationError(Exception):
    """
    Used to warn when a user in unauthenticated.

    As authenticated_index core business is shared among several routes
    and the only difference in implementation is the error handling,
    This exception is used to tell the view implementation that user is not
    authenticated, so the view should handle error.
    """
    pass


def authenticated_index(request):
    """
    authenticated_index view business logic.
    Raises a `AuthenticationError` when user cannot access the view.

    An abstraction is used to allow different error handling depending on
    request accept header.
    """
    if not is_user_authenticated(request):
        raise AuthenticationError(
                            'Only authenticated users can access this page')

    # User is authenticated
    request.response.status_int = 200
    return { 'user': request.session['user'] }



@view_config(request_method='GET', renderer='json',
             route_name='app.index', accept='application/json')
@view_config(request_method='GET', renderer='json',
             route_name='app.index', accept='text/json')
def authenticated_index_api(request):
    """
    Application Route Index as JSON.

    Ask authenticated_index to do the job.
    Returns 401 Unauthorised in case user is unauthenticated.
    """

    try:
        return authenticated_index(request)

    except AuthenticationError, e:
        # Unauthorized.
        # As raising a pyramid.httpexceptions.HTTPUnauthorized does not render
        # as JSON, format the error manually.
        request.response.status_int = 401
        return {
                'error': e.message
            }



@view_config(request_method='GET', renderer='frontend/index.html',
             route_name='app.index', accept='text/html')
def authenticated_index_html(request):
    """
    Application Route Index served as HTML.

    Ask authenticated_index to do the job.
    Redirect to signin in case user is unauthenticated.
    """

    try:
        return authenticated_index(request)

    except AuthenticationError, e:
        # Send the user on signin page.
        return redirect(request, 'user.signin')





@view_config(request_method='GET', route_name='app.public')
def public_index(request):
    """
    Default route for non authenticated request.

    If request is authenticated, redirect to index.
    Redirect to signin page otherwise.
    """

    if is_user_authenticated(request):
        return redirect(request, 'app.index', optional='');

    return redirect(request, 'user.signin');
