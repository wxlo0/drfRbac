from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib import auth
from apps.rbac.models import User
from core.ExceptionHandler import RequestException
import re


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    real_name = serializers.CharField(write_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['real_name', 'username', 'password']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        real_name = attrs.get('real_name', '')
        # 检查字符串是否只包含数字和字母
        if not real_name.isalnum():
            raise RequestException("用户名应该只包含字母数字字符")
        if not re.match(r"^1[35789]\d{9}$", username):
            raise RequestException("手机号不正确")
        if not len(password) >= 6:
            raise RequestException("密码长度不正确")
        if User.objects.filter(username=username).exists():
            raise RequestException("手机账号已存在")

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()
    real_name = serializers.CharField(read_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        user = User.objects.get(username=obj.get('username'))
        return user.token()

    class Meta:
        model = User
        fields = ['username', 'password', 'token', 'real_name']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if not user:
            raise RequestException('无效账号密码，请重试')
        if not user.is_active:
            raise RequestException('帐户已禁用，请联系管理员')
        if not user.token():
            Token.objects.create(user=user)
        return {'real_name': user.real_name, 'username': username, 'token': user.token()}
