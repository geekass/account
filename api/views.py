import json
from django.views.decorators.http import require_POST
from api.exceptions import InvalidJsonException
from api.response import ApiSuccessHttpResponse
from api.user_manager import UserManager


@require_POST
def register(request):
    user_manager = UserManager()
    try:
        body = json.loads(request.body)
    except ValueError:
        print request.body
        raise InvalidJsonException
    params = {'full_name': body.get('full_name', None),
              'date_of_birth': body.get('date_of_birth', ''),
              'username': body.get('username', None),
              'password': body.get('password', None),
              'email': body.get('email', None),
              'address': body.get('address', None),
              'postcode': body.get('postcode', None),
              'job_title': body.get('job_title', None)}
    user_manager.register(**params)
    return ApiSuccessHttpResponse(http_code=201)
