from __future__ import unicode_literals

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_defaults
from pyramid.view import view_config

from caliopen.web.authentication.authenticate import is_user_authenticated

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
        url = request.route_url('app.index')
    else:
        url = request.route_url('user.signin')

    return HTTPFound(location=url)
