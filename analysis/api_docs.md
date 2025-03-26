# API接口文档

## 基础信息
- 基础路径: `/api/v1`
- 认证方式: Bearer Token
- 响应格式: JSON

## 模型服务API

### 1. 创建模型训练任务
```
POST /model/train
```

请求参数:
```json
{
  "model_type": "string",
  "dataset_id": "string",
  "params": {
    "learning_rate": 0.001,
    "batch_size": 32
  }
}
```

响应示例:
```json
{
  "code": 200,
  "data": {
    "task_id": "string",
    "status": "pending"
  }
}
```

### 2. 获取模型信息
```
GET /model/{model_id}
```

响应示例:
```json
{
  "code": 200,
  "data": {
    "id": "string",
    "name": "string",
    "version": "string",
    "status": "ready"
  }
}
```

## 文本转语音API

### 1. 文本转语音
```
POST /tts/convert
```

请求参数:
```json
{
  "text": "string",
  "voice_type": "female",
  "speed": 1.0,
  "pitch": 1.0
}
```

响应示例:
```json
{
  "code": 200,
  "data": {
    "audio_url": "string",
    "duration": 1200
  }
}
```

## 视频处理API

### 1. 提交视频处理任务
```
POST /video/process
```

请求参数:
```json
{
  "video_url": "string",
  "operation": "transcode",
  "format": "mp4"
}
```

响应示例:
```json
{
  "code": 200,
  "data": {
    "task_id": "string",
    "status": "queued"
  }
}
```

## 语音处理API

### 1. 语音识别
```
POST /voice/recognize
```

请求参数:
```json
{
  "audio_url": "string",
  "language": "zh-CN"
}
```

响应示例:
```json
{
  "code": 200,
  "data": {
    "text": "string",
    "confidence": 0.95
  }
}
```

## 错误码
| 代码 | 描述 |
|------|------|
| 200  | 成功 |
| 400  | 参数错误 |
| 401  | 未授权 |
| 500  | 服务器错误 |
