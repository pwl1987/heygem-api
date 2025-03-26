# Python版Heygem API 部署指南

## 系统要求
- Docker 20.10+
- Python 3.9+
- 至少2GB可用内存

## 项目初始化
```bash
# 克隆主仓库
git clone https://github.com/it00021hot/heygem-api-python.git
cd heygem-api-python

# 获取前端代码（如果git clone失败）
# 方案1：使用git clone
# git clone https://github.com/it00021hot/HeyGem.ai.git -b web frontend

# 方案2：手动下载
# 1. 访问 https://github.com/it00021hot/HeyGem.ai
# 2. 下载web分支代码
# 3. 解压到项目根目录下的frontend文件夹

# 构建镜像
docker build -t heygem-api-python .

# 检查前端资源
docker run --rm heygem-api-python ls -l /app/frontend/dist
```

## 运行容器
```bash
# 开发模式
docker run -it --rm \
  -p 8000:8000 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  heygem-api-python

# 生产模式
docker run -d \
  --name heygem-api \
  -p 8000:8000 \
  -v /path/to/data:/app/data \
  -v /path/to/logs:/app/logs \
  heygem-api-python
```

## 测试验证
```bash
# 测试API健康状态
curl http://localhost:8000/api/health

# 测试认证系统
curl -X POST http://localhost:8000/api/auth/token \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"your_password"}'

# 查看日志
docker logs -f heygem-api
```

## 环境变量配置
可在`config.py`中修改或通过Docker环境变量覆盖：
- `DATABASE_URL`: 数据库连接字符串
- `SECRET_KEY`: JWT加密密钥
- `LOG_LEVEL`: 日志级别(DEBUG/INFO/WARNING/ERROR)
