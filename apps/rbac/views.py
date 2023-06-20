from rest_framework.response import Response
from rest_framework import generics, permissions, status
from drf_yasg.utils import swagger_auto_schema
from apps.rbac.models import User
from apps.rbac.serializers import LoginSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        tags=["User"],
        operation_description="Register a new user",
    )
    def post(self, request):
        # todo: 手机短信验证
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(username=user_data['username'])
        Token.objects.create(user=user)
        return Response({"code": 200, "msg": "成功", "data": ""}, status=status.HTTP_200_OK)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        tags=["User"],
        operation_description="User login",
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"code": 200, "msg": "成功", "data": serializer.data}, status=status.HTTP_200_OK)
