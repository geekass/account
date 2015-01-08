class ApiException(Exception):
    HTTP_REDIRECT = 302
    HTTP_BAD_REQUEST = 400
    HTTP_UNAUTHORIZED = 401
    HTTP_NOT_FOUND = 404
    HTTP_CONFLICT = 409
    HTTP_SERVER_ERROR = 500

    code = 0
    message = 'Base api exception'
    http_status = HTTP_BAD_REQUEST
    debug_message = ''

    def __unicode__(self):
        """Render the exception as a Unicode string."""
        lines = ['{0.message}, {0.code}, {0.http_status}'.format(self)]
        if self.debug_message:
            lines.append(unicode(self.debug_message))
        return '\n'.join(lines)

    def __str__(self):
        """Provide an ASCII output for the exception by taking the
        Unicode output and backslash encoding any non-ASCII characters."""
        return unicode(self).encode('ascii', 'backslashreplace')


class InvalidJsonException(ApiException):
    code = '00'
    http_status = ApiException.HTTP_BAD_REQUEST
    message = 'Invalid json given.'
