# Simple service that authenticate the user int the session.
#
# from caliopen.web.authentication.authenticate import authenticate_user
# from caliopen.web.authentication.validation import validate
#
# try:
#   user = validate(username='John', password='Doe')
#   authenticate_user(request, user)
# excerpt ValidationError, e:
#   # This is a validation error.
#   # send a 400
#   print e.messages
# excerpt e:
#   # This is an internal error
#   # send a 500
#   print "Unexpected error occured"

def authenticate_user(request, user):
    """
    Persist provided user authentication into session

    @param pyramid.request request the current request
    """
    # activate user in session
    # FIXME this should leverage pyramid authentication
    # process
    request.session['user'] = user['user_id']

def unauthenticate_user(request):
    """
    Clear session and user authentication

    @param pyramid.request request the current request
    """
    request.session.invalidate()

def is_user_authenticated(request):
    """
    Check wether the user is authenticatedor not.

    @param pyramid.request request the current request
    @return Boolean
    """
    # FIXME this should leverage pyramid authentication
    # process
    return request.session['user']
