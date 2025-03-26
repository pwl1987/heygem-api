# Python版Heygem API项目

## 项目概述
本项目是Heygem.ai的Python实现版本，基于FastAPI框架构建，提供以下核心功能：
- 模型服务API
- 文本转语音(TTS)服务  
- 视频处理服务
- 语音处理服务
- 用户认证系统
- 日志监控系统

## 当前状态
✅ 已完成所有功能模块开发  
✅ 完成Docker容器化部署  
✅ 统一前端资源路径标准化  
✅ 通过全部测试用例

## 快速开始
```bash
# 克隆项目
git clone https://github.com/it00021hot/heygem-api-python.git
cd heygem-api-python

# 获取前端代码（如果git clone失败，请手动下载并解压到frontend目录）
# 1. 从 https://github.com/it00021hot/HeyGem.ai 下载web分支代码
# 2. 解压到项目根目录下的frontend文件夹

# 构建并运行
docker-compose up -d
```

## 文档说明
- [部署指南](DEPLOYMENT.md)
- [API文档](api_docs.md)  
- [测试报告](TEST_REPORT.md)
- [变更日志](CHANGELOG.md)

## 技术栈
- Python 3.9
- FastAPI
- PostgreSQL
- Redis  
- Celery
- Docker
