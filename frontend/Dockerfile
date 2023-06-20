# 阶段1，基于Node镜像，构建并编译Vue项目
FROM node:16 as build-stage

WORKDIR /app

COPY package*.json ./

# 安装项目依赖
RUN npm install --production --registry=https://registry.npm.taobao.org

COPY . .

# 构建应用
RUN npm run build

# 阶段2，基于Nginx镜像，部署Vue应用
FROM nginx:stable-alpine as production-stage

# 将阶段1中构建的dist文件复制到Nginx中
COPY --from=build-stage /app/dist /usr/share/nginx/html

# 更换Nginx的阿里源
RUN echo "http://mirrors.aliyun.com/alpine/v3.6/main/" > /etc/apk/repositories

# 暴露80端口
EXPOSE 80

# 启动Nginx
CMD ["nginx", "-g", "daemon off;"]
