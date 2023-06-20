"""
@Created on 2023/6/13 21:51
@Author: clyde.liu
@Des: 自定义异常捕获
"""

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework.response import Response


def common_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        print(exc, context)
        response = Response({'code': 500, 'msg': str(exc) or '未知错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        response.data['code'] = response.status_code
        if response.data.get('detail'):
            response.data['msg'] = response.data.pop('detail')
        response.status_code = 200
    return response


class RequestException(APIException):
    """
    serializers自定义错误响应
    """
    def __init__(self, error, code=400):
        self.detail = error
        self.status_code = code


