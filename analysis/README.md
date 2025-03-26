# Heygem API 项目分析报告

## 项目概述
这是一个基于Go语言开发的多功能API服务，主要提供以下功能模块：
- 模型服务(Model)
- 文本转语音服务(TTS)
- 视频处理服务(Video)
- 语音处理服务(Voice)

## 目录结构分析

### 1. 根目录文件
- `main.go`: 项目主入口文件
- `go.mod/go.sum`: Go模块依赖管理文件
- `Makefile`: 项目构建脚本
- `README.MD`: 项目说明文档
- `.gitignore`: Git忽略规则
- `.gitattributes`: Git属性配置
- `.clinerules`: CLI工具规则配置

### 2. API定义层 (api/)
定义各模块的API接口规范，采用版本化设计(v1子目录)
- `api/model/`: 模型服务API定义
- `api/tts/`: 文本转语音服务API定义  
- `api/video/`: 视频服务API定义
- `api/voice/`: 语音服务API定义

### 3. 内部实现层 (internal/)
核心业务逻辑实现，采用分层架构：
- `internal/boot/`: 初始化逻辑
- `internal/cmd/`: 命令行处理
- `internal/consts/`: 常量定义
- `internal/controller/`: 控制器层(HTTP请求处理)
- `internal/dao/`: 数据访问层
- `internal/logic/`: 业务逻辑层
- `internal/model/`: 数据模型定义
- `internal/service/`: 服务接口定义

### 4. 部署配置 (manifest/)
包含各种部署配置：
- `manifest/config/`: 应用配置文件
- `manifest/deploy/`: 部署配置(Kubernetes/Docker)
- `manifest/docker/`: Docker相关文件
- `manifest/i18n/`: 国际化资源
- `manifest/protobuf/`: Protobuf定义

### 5. 其他目录
- `hack/`: 开发工具脚本
- `resource/`: 静态资源
- `test/`: 测试代码
- `utility/`: 工具类

## 主要模块功能

### 模型服务(Model)
提供AI模型相关功能，包括：
- 模型训练
- 模型推理
- 模型管理

### 文本转语音服务(TTS)
提供文本转语音功能，包括：
- 语音合成
- 语音风格转换
- 语音参数调整

### 视频处理服务(Video)
提供视频处理功能，包括：
- 视频转码
- 视频剪辑
- 视频特效处理

### 语音处理服务(Voice)
提供语音处理功能，包括：
- 语音识别
- 语音增强
- 语音特征提取

## 数据库设计
项目使用MySQL数据库，主要表包括：
- model_xxx: 模型相关表
- video_xxx: 视频相关表  
- voice_xxx: 语音相关表

## 部署架构
项目支持多种部署方式：
1. Docker Compose部署
2. Kubernetes部署
3. 裸机部署
