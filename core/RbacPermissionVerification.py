"""
@Created on 2023/6/13 21:45
@Author: clyde.liu
@Des: rbac权限验证
"""

from rest_framework.response import Response
from rest_framework import status
from functools import wraps

from core.ExceptionHandler import RequestException

rbac_permissions = []


def rbac_permission(name, desc):
    def decorator(function):
        rbac_permissions.append({
            'permissions_name': name,
            'permissions_desc': desc
        })

        @wraps(function)
        def wrapper(request, *args, **kwargs):
            is_super_admin = request.request.user.roles.filter(role_name="超级管理员").exists()
            if not is_super_admin:
                if not request.request.user.roles.filter(permissions__permissions_name=name,
                                                         permissions__permissions_status=True).exists():
                    raise RequestException('抱歉，您没有此操作权限', code=403)
            return function(request, *args, **kwargs)

        return wrapper

    return decorator
