from __future__ import unicode_literals

from pyramid.view import view_defaults
from pyramid.view import view_config

from caliopen.web.authentication.authenticate import is_user_authenticated
from caliopen.web.views import redirect

import logging
log = logging.getLogger(__name__)

@view_config(request_method='GET', renderer='app/index.html',
             route_name='app.index')
def authenticated_index(request):
    """
    Application Route Index.
    """

    return {}

@view_config(request_method='GET', route_name='app.public')
def public_index(request):
    """
    Default route for non authenticated request.

    If request is authenticated, redirect to index.
    Redirect to signin page otherwise.
    """

    if is_user_authenticated(request):
        route = 'app.index';
    else:
        route = 'user.signin';

    return redirect(request, route)
