# drfRbac 权限管理

基于Django rest framework开发的Rbac权限管理

## 项目配置（本地启动）

### 数据库

根目录创建`.env`文件，写入数据库配置信息

```
DB_NAME=drfRbac
DB_USER=root
DB_PASSWORD=12345678
DB_HOST=localhost
DB_PORT=3306
```

### 创建虚拟环境

```
# 创建名为 env 的虚拟环境
python3 -m venv env

# 激活环境
source env/bin/activate
```

使用Pycharm选择项目的创建虚拟环境，步骤....

### 安装相关库

终端执行命令

```
pip install -r requirements.txt
```

### 数据库迁移

```
python manage.py makemigrations

python manage.py migrate 
```

### 数据库同步rbac权限

```
python manage.py sync_permissions
```
超级管理员：

用户名：amdin 密码：admin

## docker-compose 部署