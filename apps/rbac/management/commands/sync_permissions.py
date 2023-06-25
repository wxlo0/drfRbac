"""
@Created on 2023/6/13 23:04
@Author: clyde.liu
@Des: 
"""

from django.core.management.base import BaseCommand

from apps.rbac.models import Permissions, Role, User
from core.RbacPermissionVerification import rbac_permissions


class Command(BaseCommand):
    help = '同步 RBAC 权限'

    def handle(self, *args, **options):
        # 删除多余权限
        existing_permissions = Permissions.objects.all()
        existing_permissions_names = {permission.permissions_name for permission in existing_permissions}
        rbac_permissions_names = {item["permissions_name"] for item in rbac_permissions}
        permissions_to_delete = existing_permissions_names - rbac_permissions_names
        Permissions.objects.filter(permissions_name__in=permissions_to_delete).delete()

        # 新建或更新权限
        for item in rbac_permissions:
            permission, created = Permissions.objects.get_or_create(permissions_name=item["permissions_name"],
                                                                    defaults=item)
            if not created:
                # 如果存在，更新描述
                for key, value in item.items():
                    setattr(permission, key, value)
                permission.save()

        # 如果超级管理员角色不存在则创建
        superuser_group, created = Role.objects.get_or_create(role_name='超级管理员')

        # 如果超级管理员用户不存在则创建
        superuser, created = User.objects.get_or_create(username='admin',
                                                        defaults={'is_superuser': True, 'is_staff': True,
                                                                  'password': 'admin', 'real_name': 'admin'})
        User.objects.get_or_create(username='user', defaults={'is_superuser': False, 'is_staff': False,
                                                              'password': 'admin', 'real_name': 'user'})
        if created:
            superuser.roles.add(superuser_group)
            superuser.set_password('admin')
            superuser.save()

        print("\n同步 RBAC 权限成功")

