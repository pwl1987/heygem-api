# 第一阶段：构建前端
FROM node:16-alpine as frontend-builder

RUN apk update && apk add git
RUN npm install -g pnpm
COPY frontend /frontend
WORKDIR /frontend
RUN pnpm install && pnpm build

# 第二阶段：构建Python环境
FROM python:3.9-slim as python-builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# 第三阶段：最终镜像
FROM registry.cn-hangzhou.aliyuncs.com/it00021hot/alpine:latest-ffmpeg

# 复制Python环境
WORKDIR /app
COPY --from=python-builder /root/.local /root/.local
COPY . .

# 复制前端构建结果到统一资源目录
COPY --from=frontend-builder /frontend/dist /app/frontend/dist

# 设置环境变量
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

# 安装系统依赖
RUN apk add --no-cache libstdc++

# 初始化应用
RUN python init_data_dir.py && \
    chmod +x /app/start.sh

EXPOSE 8000
CMD ["sh", "start.sh"]
