# 模块详细说明

## 模型服务 (Model)

### 功能概述
- 模型训练管理
- 模型推理服务
- 模型版本控制

### 核心文件
- `api/model/model.go`: 基础API定义
- `api/model/v1/model.go`: v1版本API
- `internal/controller/model/`: 控制器实现
- `internal/logic/model/`: 业务逻辑
- `internal/dao/model.go`: 数据访问

### 接口定义
```go
// 模型训练接口
type ModelTrainRequest struct {
    ModelType string
    DataSet   string
    Params    map[string]interface{}
}

// 模型推理接口
type ModelPredictRequest struct {
    ModelID string
    Input   []float32
}
```

## 文本转语音服务 (TTS)

### 功能概述
- 文本转语音合成
- 语音风格调整
- 语音参数配置

### 核心文件
- `api/tts/tts.go`: 基础API
- `api/tts/v1/tts.go`: v1版本API
- `internal/controller/tts/`: 控制器
- `internal/logic/tts/`: 业务逻辑

### 接口定义
```go
// TTS请求
type TTSRequest struct {
    Text      string
    VoiceType string
    Speed     float32
    Pitch     float32
}
```

## 视频处理服务 (Video)

### 功能概述
- 视频转码
- 视频剪辑
- 特效处理

### 核心文件
- `api/video/video.go`: 基础API
- `api/video/v1/video.go`: v1版本API
- `internal/controller/video/`: 控制器
- `internal/dao/video.go`: 数据访问

## 语音处理服务 (Voice)

### 功能概述
- 语音识别
- 语音增强
- 声纹识别

### 核心文件
- `api/voice/voice.go`: 基础API
- `api/voice/v1/voice.go`: v1版本API
- `internal/logic/voice/`: 业务逻辑
- `internal/dao/voice.go`: 数据访问
