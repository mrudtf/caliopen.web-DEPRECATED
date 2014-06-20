#!/usr/bin/env python

"""
This script create a user with a password in a caliopen instance.

"""
import logging

log = logging.getLogger(__name__)


def create_user(**kwargs):

    from caliopen.core.user import User
    email = kwargs['email']
    password = kwargs['password']
    first_name = kwargs.get('first_name')
    last_name = kwargs.get('last_name')
    user = User.create(user_id=email, password=password,
                       first_name=first_name, last_name=last_name)
    user.save()
    log.info('User %s created' % user.user_id)
