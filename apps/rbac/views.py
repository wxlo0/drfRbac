from rest_framework.response import Response
from rest_framework import generics, permissions, status
from drf_yasg.utils import swagger_auto_schema
from apps.rbac.models import User, Role, Permissions
from apps.rbac.serializers import LoginSerializer, RegisterSerializer, UserSerializer, RoleSerializer, \
    ChangeUserRoleSerializer, PermissionsSerializer
from rest_framework.authtoken.models import Token
from core.ExceptionHandler import RequestException
from core.RbacPermissionVerification import rbac_permission
from rest_framework.views import APIView


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


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    @swagger_auto_schema(
        tags=["User"],
        operation_description="User List",
    )
    def list(self, request, *args, **kwargs):
        return_data = super().list(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})


class RoleListAPIView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    @swagger_auto_schema(
        tags=["User"],
        operation_description="Role List",
    )
    @rbac_permission(name="role_list", desc="角色列表查看")
    def list(self, request, *args, **kwargs):
        return_data = super().list(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})


class RoleUpdateAPIView(generics.UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    @swagger_auto_schema(
        tags=["User"],
        operation_description="Role Update",
    )
    @rbac_permission(name="role_update", desc="角色更新")
    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        role = Role.objects.filter(id=kwargs['pk']).first()
        if not role or role.role_name == "admin":
            raise RequestException("角色不存在或者不允许修改")
        role.permissions.clear()
        role.permissions.add(*request.data['permissions'])
        role.save()
        return Response({"code": 200, "msg": "成功", "data": ""})


class ChangeUserRoleAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangeUserRoleSerializer

    @swagger_auto_schema(
        tags=["User"],
        operation_description="Change User Role",
    )
    @rbac_permission(name="change_user_role", desc="修改用户角色")
    def put(self, request, *args, **kwargs):
        user = User.objects.filter(id=kwargs['pk']).first()
        if not user:
            raise RequestException("用户不存在")
        if user.username == "admin":
            raise RequestException("admin用户不允许修改角色")

        user.roles.clear()
        user.roles.add(*request.data['roles'])
        user.save()
        return Response({"code": 200, "msg": "成功", "data": ""})


class PermissionsListAPIView(generics.ListAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer

    @swagger_auto_schema(
        tags=["User"],
        operation_description="Permissions List",
    )
    @rbac_permission(name="permissions_list", desc="权限列表查看")
    def list(self, request, *args, **kwargs):
        return_data = super().list(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})


class RolePermissionsListAPIView(APIView):
    @swagger_auto_schema(
        tags=["User"],
        operation_description="Role Permissions List",
    )
    @rbac_permission(name="role_permissions_list", desc="角色权限列表查看")
    def get(self, request, role_id):
        role = Role.objects.filter(id=role_id).first()
        if not role:
            raise RequestException("角色不存在")
        permission = role.permissions.values_list('id', flat=True)
        return Response({"code": 200, "msg": "成功", "data": permission})

