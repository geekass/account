import json
from django.test.testcases import TestCase


class ApiTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super(ApiTestCase, self).__init__(*args, **kwargs)

    def assert_api_exception(self, response, error_class, debug_message=None):
        self.assertEqual(response.status_code, error_class.http_status)

        content = json.loads(response.content)

        self.assertFalse(content['status']['ok'], content)
        self.assertEqual(error_class.code, content['status']['internal_error_code'], content)

        self.assertEqual(error_class.message, content['status']['user_msg'], content)

        if debug_message is not None:
            self.assertEqual(debug_message, content['status']['debug_msg'], content)