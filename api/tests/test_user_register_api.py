import json
from api.exceptions.user_register import InvalidFullNameException
from api.models import User
from api.tests.utils import ApiTestCase
from marketing.models import UserExtras


class UserRegisterApiTest(ApiTestCase):
    path = '/api/account/register/'

    def test_get_returns_method_not_allowed(self):
        response = self.client.get(path=self.path,
                                   content_type='application/json')
        self.assertEqual(405, response.status_code)

    def test_post_with_no_full_name_returns_bad_request(self):
        response = self.client.post(path=self.path, data=json.dumps({}), content_type='application/json')
        self.assert_api_exception(response=response, error_class=InvalidFullNameException)

    def test_post_with_correct_params_creates_account(self):
        valid_data = {'full_name': 'Hassan Khalid',
                      'date_of_birth': '1099-10-10',
                      'username': 'h.scorpion.k',
                      'password': 'imsafe',
                      'email': 'foo@foo.com',
                      'address': 'asdad',
                      'postcode': 'N$F',
                      'job_title': 'Dev'
        }
        response = self.client.post(path=self.path, data=json.dumps(valid_data), content_type='application/json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(1, User.objects.count())
        self.assertEqual(1, UserExtras.objects.count())