# Generated by Django 3.2.16 on 2023-06-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('permissions_name', models.CharField(max_length=15, verbose_name='权限名称')),
                ('permissions_desc', models.CharField(max_length=255, null=True, verbose_name='权限描述')),
                ('permissions_status', models.BooleanField(default=False, verbose_name='权限状态')),
            ],
            options={
                'db_table': 'rbac_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role_name', models.CharField(max_length=15, verbose_name='角色名称')),
                ('role_status', models.BooleanField(default=False, verbose_name='角色状态')),
                ('role_desc', models.CharField(max_length=255, null=True, verbose_name='角色描述')),
                ('permissions', models.ManyToManyField(related_name='roles', to='rbac.Permissions')),
            ],
            options={
                'db_table': 'rbac_user_role',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(related_name='users', to='rbac.Role'),
        ),
    ]
