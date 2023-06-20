"""
@Created on 2023/6/13 21:45
@Author: clyde.liu
@Des: rbac权限验证
"""

from rest_framework.response import Response
from rest_framework import status
from functools import wraps

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
                    return Response({'code': 401, 'msg': '权限不足'}, status=status.HTTP_403_FORBIDDEN)

            return function(request, *args, **kwargs)

        return wrapper

    return decorator
