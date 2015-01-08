import datetime

from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from api.exceptions.user_register import InvalidAddressException
from api.exceptions.user_register import InvalidDateOfBirthException
from api.exceptions.user_register import InvalidEmailException
from api.exceptions.user_register import InvalidFullNameException
from api.exceptions.user_register import InvalidJobTitleException
from api.exceptions.user_register import InvalidPasswordException
from api.exceptions.user_register import InvalidPostCodeException
from api.exceptions.user_register import InvalidUserNameException
from api.models import User
from marketing.models import UserExtras


class UserManager(object):
    def register(self, full_name, date_of_birth, username, password, email, address, postcode, job_title):
        if not full_name:
            raise InvalidFullNameException("Full name can't be empty")

        try:

            datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
        except ValueError:
            raise InvalidDateOfBirthException('Date of birth should be YY-MM-DD')

        if not username:
            raise InvalidUserNameException
        if not password:
            raise InvalidPasswordException

        try:
            EmailValidator()(email)
        except ValidationError:
            raise InvalidEmailException

        if not address:
            raise InvalidAddressException

        if not postcode:
            raise InvalidPostCodeException
        if not job_title:
            raise InvalidJobTitleException

        user = User.objects.create(
            full_name=full_name,
            date_of_birth=date_of_birth,
            username=username,
            password=password,
            address=address,
            job_title=job_title
        )
        UserExtras.objects.create(
            id=user.pk,
            email=email,
            postcode=postcode
        )
