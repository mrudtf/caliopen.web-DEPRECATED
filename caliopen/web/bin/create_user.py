#!/usr/bin/env python

"""
This script create a user with a password in a caliopen instance.

"""
import logging

log = logging.getLogger(__name__)


def create_user(**kwargs):

    from caliopen.core.user import User
    from caliopen.core.parameters.user import NewUser
    param = NewUser()
    param.name = kwargs['email']
    param.password = kwargs['password']
    param.given_name = kwargs.get('given_name')
    param.family_name = kwargs.get('family_name')
    user = User.create(param)
    user.save()
    log.info('User %s created' % user.user_id)
