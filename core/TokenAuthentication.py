"""
@Created on 2023/6/13 21:48
@Author: clyde.liu
@Des: 接口token验证
"""
import datetime
from django.conf import settings
from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from django.core.cache import cache


EXPIRE_MINUTES = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES', 60 * 24 * 7)


class MyTokenAuthentication(TokenAuthentication):

    def authenticate(self, request):
        request.META['HTTP_AUTHORIZATION'] = f'Token {request.META.get("HTTP_TOKEN")}'
        return super(MyTokenAuthentication, self).authenticate(request)

    def authenticate_credentials(self, key):
        cache_user = cache.get(key)
        if cache_user:
            return cache_user, key

        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('用户认证失败，请重新登录')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('用户未激活或已删除')

        time_now = timezone.now()

        if token.created < time_now - datetime.timedelta(minutes=EXPIRE_MINUTES):
            token.delete()
            raise exceptions.AuthenticationFailed('登录已过期，请重新登录')

        if token:
            cache.set(key, token.user, EXPIRE_MINUTES * 60)
        return token.user, token
