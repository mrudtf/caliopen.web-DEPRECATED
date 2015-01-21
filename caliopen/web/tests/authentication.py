from __future__ import unicode_literals

import unittest
import json

from pyramid import testing

from caliopen.web.authentication.validation import validate


class TestViewSessions(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_should_reject_empty_username(self):
        """
        Retrieve the list of messages of a thread.
        """
        with self.assertRaise(ValidationError) as cm:
            validate(username="", password="Foo")

        exception = cm.exception
        self.assertEqual(the_exception.messages, '')

