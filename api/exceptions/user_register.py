from api.exceptions import ApiException

INVALID_FULL_NAME_CODE = 1
INVALID_DOB_CODE = 2
INVALID_USERNAME_CODE = 3
INVALID_PASSWORD_CODE = 4
INVALID_EMAIL_CODE = 5
INVALID_ADDRESS_CODE = 6
INVALID_POSTCODE_CODE = 7
INVALID_JOB_TITLE_CODE = 8


class InvalidFullNameException(ApiException):
    code = INVALID_FULL_NAME_CODE
    http_status = ApiException.HTTP_BAD_REQUEST
    message = 'Invalid full name given.'


class InvalidDateOfBirthException(ApiException):
    code = INVALID_DOB_CODE
    http_status = ApiException.HTTP_BAD_REQUEST
    message = 'Invalid date of birth given.'


class InvalidUserNameException(ApiException):
    code = INVALID_USERNAME_CODE
    http_status = ApiException.HTTP_BAD_REQUEST
    message = 'Invalid user name given.'


class InvalidPasswordException(ApiException):
    code = INVALID_PASSWORD_CODE
    http_status = ApiException.HTTP_BAD_REQUEST
    message = 'Invalid password given.'


class InvalidEmailException(ApiException):
    code = INVALID_EMAIL_CODE
    http_status = ApiException.HTTP_BAD_REQUEST
    message = 'Invalid email given.'


class InvalidAddressException(ApiException):
    code = INVALID_ADDRESS_CODE
    http_status = ApiException.HTTP_BAD_REQUEST
    message = 'Invalid address given.'


class InvalidPostCodeException(ApiException):
    code = INVALID_POSTCODE_CODE
    http_status = ApiException.HTTP_BAD_REQUEST
    message = 'Invalid post code given.'


class InvalidJobTitleException(ApiException):
    code = INVALID_JOB_TITLE_CODE
    http_status = ApiException.HTTP_BAD_REQUEST
    message = 'Invalid job title given.'
