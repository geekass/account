from api.exceptions import ApiException
from api.response import ApiExceptionHttpResponse


class RequestExceptionsMiddleware(object):
    def _wrap_as_api_exception(self, exception, ):

        if isinstance(exception, ApiException):
            api_exception = exception
        return api_exception

    def process_exception(self, request, exception):
        if isinstance(exception, ApiException):
            return ApiExceptionHttpResponse(exception)