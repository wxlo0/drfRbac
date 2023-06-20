from django.db import models
from apps.rbac.models import BaseModel, User


class Class(BaseModel):
    name = models.CharField("班级名称", max_length=20)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField("上课地点", max_length=255)
    level = models.CharField("等级", max_length=20)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "rbac_class"


class Student(BaseModel):
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField("学生姓名", max_length=20)
    sex = models.CharField("性别", max_length=11)
    telephone = models.CharField("电话", max_length=11)
    subject = models.CharField("科目", max_length=255)
    grade = models.CharField("年级", max_length=10)
    school = models.CharField("学校", max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "rbac_student"
