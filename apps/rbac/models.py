from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    roles = models.ManyToManyField('Role', related_name='users')
    username = models.CharField("用户名", max_length=255, unique=True)
    real_name = models.CharField("真实姓名", max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "rbac_user"

    def token(self):
        token = Token.objects.filter(user=self).first()
        return token.key if token else None


class Role(BaseModel):
    permissions = models.ManyToManyField('Permissions', related_name='roles')
    role_name = models.CharField("角色名称", unique=True, max_length=15)
    role_status = models.BooleanField("角色状态", default=False)
    role_desc = models.CharField("角色描述", null=True, max_length=255)

    class Meta:
        db_table = "rbac_role"


class Permissions(BaseModel):
    permissions_name = models.CharField("权限名称", unique=True, max_length=15)
    permissions_desc = models.CharField("权限描述", null=True, max_length=255)
    permissions_status = models.BooleanField("权限状态", default=True)

    class Meta:
        db_table = "rbac_permissions"
