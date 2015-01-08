from time import sleep
from django.test.testcases import TestCase

from api.exceptions.user_register import InvalidAddressException
from api.exceptions.user_register import InvalidDateOfBirthException
from api.exceptions.user_register import InvalidEmailException
from api.exceptions.user_register import InvalidFullNameException
from api.exceptions.user_register import InvalidJobTitleException
from api.exceptions.user_register import InvalidPasswordException
from api.exceptions.user_register import InvalidPostCodeException
from api.exceptions.user_register import InvalidUserNameException
from api.models import User
from api.user_manager import UserManager
from marketing.models import UserExtras


class UserRegisterTest(TestCase):
    def setUp(self):
        super(UserRegisterTest, self).setUp()
        self.valid_register_args = {'full_name': 'Hassan Khalid',
                               'date_of_birth': '1099-10-10',
                               'username': 'h.scorpion.k',
                               'password': 'imsafe',
                               'email': 'foo@foo.com',
                               'address': 'asdad',
                               'postcode': 'N$F',
                               'job_title': 'Dev'}

    def test_register_with_empty_full_name_fails(self):
        user_manager = UserManager()
        self.valid_register_args['full_name'] = ''
        with self.assertRaises(InvalidFullNameException):
            user_manager.register(**self.valid_register_args)

    def test_invalid_date_of_birth_fails(self):
        user_manager = UserManager()
        self.valid_register_args['date_of_birth'] = '22/22/22'
        with self.assertRaises(InvalidDateOfBirthException):
            user_manager.register(**self.valid_register_args)

    def test_invalid_user_name_fails(self):
        user_manager = UserManager()
        self.valid_register_args['username'] = None
        with self.assertRaises(InvalidUserNameException):
            user_manager.register(**self.valid_register_args)

    def test_invalid_password_fails(self):
        user_manager = UserManager()
        self.valid_register_args['password'] = ''
        with self.assertRaises(InvalidPasswordException):
            user_manager.register(**self.valid_register_args)

    def test_invalid_email_fails(self):
        user_manager = UserManager()
        self.valid_register_args['email'] = 'foo'
        with self.assertRaises(InvalidEmailException):
            user_manager.register(**self.valid_register_args)

    def test_invalid_address_fails(self):
        user_manager = UserManager()
        self.valid_register_args['address'] = ''
        with self.assertRaises(InvalidAddressException):
            user_manager.register(**self.valid_register_args)

    def test_invalid_postcode_fails(self):
        user_manager = UserManager()
        self.valid_register_args['postcode'] = ''
        with self.assertRaises(InvalidPostCodeException):
            user_manager.register(**self.valid_register_args)

    def test_invalid_job_title_fails(self):
        user_manager = UserManager()
        self.valid_register_args['job_title'] = ''
        with self.assertRaises(InvalidJobTitleException):
            user_manager.register(**self.valid_register_args)

    def test_user_info_is_saved_in_default_db(self):
        user_manager = UserManager()
        user_manager.register(**self.valid_register_args)

        self.assertEqual(1, User.objects.count())
        self.assertEqual('Dev', User.objects.all()[0].job_title)

    def test_user_email_and_postcode_is_saved_in_marketing_db(self):
        total_user_extra = UserExtras.objects.count()
        user_manager = UserManager()
        user_manager.register(**self.valid_register_args)
        self.assertEqual(total_user_extra + 1, UserExtras.objects.count())

    def test_user_and_user_extra_are_linked_via_uuid(self):
        user_manager = UserManager()
        user_manager.register(**self.valid_register_args)

        self.assertEqual(User.objects.all()[0].pk, UserExtras.objects.all()[0].pk)
