from rest_framework import viewsets
from rest_framework import permissions
from core.RbacPermissionVerification import rbac_permission
from core.TokenAuthentication import MyTokenAuthentication
from .serializers import ClassSerializer, StudentSerializer
from .models import Class, Student
from rest_framework.response import Response


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    @rbac_permission(name="student_list", desc="学生信息列表查看")
    def list(self, request, *args, **kwargs):
        return_data = super().list(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})

    @rbac_permission(name="student_get", desc="单个学生信息查看")
    def retrieve(self, request, *args, **kwargs):
        return_data = super().retrieve(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})

    @rbac_permission(name="student_create", desc="添加学生信息")
    def create(self, request, *args, **kwargs):
        return_data = super().create(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})

    @rbac_permission(name="student_update", desc="更新学生信息")
    def update(self, request, *args, **kwargs):
        return_data = super().update(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})

    @rbac_permission(name="student_delete", desc="删除学生信息")
    def destroy(self, request, *args, **kwargs):
        return_data = super().destroy(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @rbac_permission(name="class_list", desc="班级信息列表查看")
    def list(self, request, *args, **kwargs):
        return_data = super().list(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})

    @rbac_permission(name="class_get", desc="单个班级信息查看")
    def retrieve(self, request, *args, **kwargs):
        return_data = super().retrieve(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})

    @rbac_permission(name="class_create", desc="添加班级信息")
    def create(self, request, *args, **kwargs):
        return_data = super().create(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})

    @rbac_permission(name="class_update", desc="更新班级信息")
    def update(self, request, *args, **kwargs):
        return_data = super().update(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})

    @rbac_permission(name="class_delete", desc="删除班级信息")
    def destroy(self, request, *args, **kwargs):
        return_data = super().destroy(request, *args, **kwargs).data
        return Response({"code": 200, "msg": "成功", "data": return_data})
