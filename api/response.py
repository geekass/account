import json
from django.http.response import HttpResponse


class ApiSuccessHttpResponse(HttpResponse):
    def __init__(self, body=None, http_code=200):
        if body is None:
            body = {}

        content = json.dumps({
            "status": {
                "ok": True
            },
            'body': body
        })

        super(ApiSuccessHttpResponse, self).__init__(content,
                                                     status=int(http_code),
                                                     content_type='application/json')


class ApiExceptionHttpResponse(HttpResponse):
    def __init__(self, api_exception, **kwargs):
        self.api_exception = api_exception

        content = json.dumps({
            "status": {
                "ok": False,
                "http_status_code": api_exception.http_status,
                "internal_error_code": api_exception.code,
                "user_msg": api_exception.message,
                "debug_msg": api_exception.debug_message,
            },
            'body': None
        })

        super(ApiExceptionHttpResponse, self).__init__(content,
                                                       status=int(api_exception.http_status),
                                                       content_type='application/json')
