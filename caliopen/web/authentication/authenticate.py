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
    """
    # activate user in session
    request.session['user'] = user['id']

def unauthenticate_user(request):
    """
    Clear session and user authentication
    """
    request.session.invalidate()
