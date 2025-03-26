# Python版Heygem API 变更日志

## [0.1.0] - 2025-03-26
### 新增
- 初始化Python项目结构
- 实现基础配置系统(config.py)
- 添加FastAPI主应用框架(main.py)
- 完成模型服务模块转换:
  - API端点(api/model/endpoints.py)
  - 业务逻辑(api/model/services.py)
  - 数据模型(api/model/schemas.py)
- 实现异步数据库支持
- 添加Alembic数据库迁移
- 创建Docker容器化配置

### 新增
- 完成TTS服务模块转换:
  - API端点(api/tts/endpoints.py)
  - 业务逻辑(api/tts/services.py)
  - 数据模型(api/tts/schemas.py)
  - 异步任务处理(Celery)
  - 音频文件路由(api/tts/audio.py)
  - 数据目录初始化脚本(init_data_dir.py)
  - Dockerfile数据目录配置

### 新增
- 完成视频处理服务模块转换:
  - API端点(api/video/endpoints.py)
  - 业务逻辑(api/video/services.py)
  - 数据模型(api/video/schemas.py)
  - 输出路由(api/video/output.py)
  - 异步任务处理(Celery)

### 新增
- 完成语音处理服务模块转换:
  - API端点(api/voice/endpoints.py)
  - 业务逻辑(api/voice/services.py)
  - 数据模型(api/voice/schemas.py)
  - 输出路由(api/voice/output.py)
  - 异步任务处理(Celery)

### 新增
- 完成用户认证系统实现:
  - JWT认证流程
  - 密码哈希存储
  - 用户管理端点
  - 令牌获取和验证
  - 用户权限控制

### 新增
- 完成日志监控系统集成:
  - 多级别日志记录(应用、访问、错误、SQL)
  - 日志文件轮转管理
  - 日志查看API端点
  - 管理员权限控制
- 重构Docker容器化配置:
  - 采用多阶段构建(前端+Python+最终镜像)
  - 直接集成前端项目代码到仓库
  - 优化前端构建流程
  - 更新部署文档说明
  - 使用Alpine基础镜像(含FFmpeg)
  - 优化依赖管理
  - 减小最终镜像体积
  - 更新启动脚本(start.sh)支持资源路径配置
  - 完善前端资源目录结构
  - 标准化静态资源存放位置
