from __future__ import unicode_literals

import unittest
import json

from pyramid import testing
from schematics.exceptions import ValidationError
from caliopen.core.user import CredentialException

from caliopen.web.authentication.validation import validate
from .compat import mock

class TestAuthenticationValidate(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def assertHasError(self, auth, fieldName, errorMessage=None):
        self.assertIn(fieldName, auth.errors)
        self.assertTrue(len(auth.errors[fieldName]) > 0)
        if errorMessage:
            self.assertIn(errorMessage, auth.errors[fieldName])

    def test_should_reject_empty_username(self):
        """
        Should reject empty username.
        """
        for val in [ None, ""]:
            auth = validate(username=val, password="Foo")
            self.assertFalse(auth.success)
            self.assertIsNone(auth.user)
            self.assertHasError(auth, fieldName='username')

    def test_should_reject_empty_password(self):
        """
        Should reject empty password.
        """
        for val in [ None, ""]:
            auth = validate(username="julien.muetton@gandi.net", password=val)
            self.assertFalse(auth.success)
            self.assertIsNone(auth.user)
            self.assertHasError(auth, fieldName='password')

    def test_should_rethrow_if_internal_errors(self):
        """
        Should rethrow if internal error during validation
        """
        # Mock User.authenticate method
        # to raise an un expected Exception
        User = mock.Mock()
        User.authenticate = mock.Mock(side_effect=Exception('Internal error'))

        with mock.patch.multiple('caliopen.web.authentication.validation', User=User):
            with self.assertRaises(Exception) as context:
                auth = validate(username="John", password="Doe")
                # ensure mock has been called

            User.authenticate.assert_call_once_with("John", "Doe")
            self.assertTrue('Internal error' in context.exception, 'Erorr is raised again')

    def test_should_reject_if_validation_error(self):
        """
        Should reject if thereis validation error
        """
        # Mock User.authenticate method
        # to raise a ValidationError
        User = mock.Mock()
        User.authenticate = mock.Mock(side_effect=ValidationError('A validation Error'))

        with mock.patch.multiple('caliopen.web.authentication.validation', User=User):
            auth = validate(username="John", password="Doe")
            # ensure mock has been called
            User.authenticate.assert_call_once_with("John", "Doe")
            self.assertFalse(auth.success, 'User should not be authenticated')

    def test_should_reject_if_credentials_are_invalid(self):
        """
        Should reject invalid credentials
        """
        # Mock User.authenticate method
        # to raise a ValidationError
        User = mock.Mock()
        User.authenticate = mock.Mock(side_effect=CredentialException('A credential Error'))

        with mock.patch.multiple('caliopen.web.authentication.validation', User=User):
            auth = validate(username="John", password="Doe")
            # ensure mock has been called
            User.authenticate.assert_call_once_with("John", "Doe")
            self.assertFalse(auth.success, 'User should not be authenticated')

    def test_should_authenticate_if_credentials_are_valid(self):
        """
        Should accept valid credentials
        """
        # Mock user dto from core.
        authenticated_user_dto = mock.Mock()
        # Mock user object
        authenticated_user = mock.Mock()
        authenticated_user.serialize = mock.Mock(return_value={})

        # Mock User.authenticate method
        # to return mock user
        User = mock.Mock()
        User.authenticate = mock.Mock(return_value=authenticated_user_dto)

        # Mock the ReturnUser
        ReturnUser = mock.Mock()
        ReturnUser.build = mock.Mock(return_value=authenticated_user)

        with mock.patch.multiple('caliopen.web.authentication.validation', User=User, ReturnUser=ReturnUser):
            auth = validate(username="John", password="Doe")
            # Assert we called user.to_api()
            authenticated_user.to_api.assert_call_once()
            # assert mock was called
            User.authenticate.assert_call_once_with("John", "Doe")
            ReturnUser.build.assert_call_once_with(authenticated_user_dto)
            authenticated_user.serialize.assert_call_once()
            self.assertTrue(auth.success, 'User should be authenticated')

if __name__ == '__main__':
    unittest.main()
