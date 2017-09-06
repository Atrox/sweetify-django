import json

from django.test import SimpleTestCase, RequestFactory

import sweetify


class SimpleTest(SimpleTestCase):
    def setUp(self):
        super(SimpleTest, self).setUp()

        self.request = RequestFactory().get('/fake-path')
        self.request.session = {}

    def test_general_sweetalert(self):
        title = 'Test Sweetify'
        sweetify.sweetalert(self.request, title)

        session_opts = json.loads(self.request.session['sweetify'])

        opts = sweetify.DEFAULT_OPTS.copy()
        opts.update({'title': title})
        assert session_opts == opts
