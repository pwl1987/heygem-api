# 数据库设计分析

## 数据库模型概览
项目使用MySQL数据库，主要包含以下几类数据表：
1. 模型相关表
2. 视频处理相关表
3. 语音处理相关表

## 模型服务表结构
### model_info (模型信息表)
```sql
CREATE TABLE `model_info` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL COMMENT '模型名称',
  `type` varchar(50) NOT NULL COMMENT '模型类型',
  `version` varchar(50) NOT NULL COMMENT '模型版本',
  `path` varchar(512) NOT NULL COMMENT '模型存储路径',
  `status` tinyint NOT NULL DEFAULT '0' COMMENT '状态:0-训练中,1-可用,2-下线',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name_version` (`name`,`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## 视频服务表结构
### video_task (视频处理任务表)
```sql
CREATE TABLE `video_task` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL COMMENT '用户ID',
  `source_url` varchar(512) NOT NULL COMMENT '源视频URL',
  `target_url` varchar(512) DEFAULT NULL COMMENT '处理后视频URL',
  `task_type` varchar(50) NOT NULL COMMENT '任务类型:transcode-转码,clip-剪辑,effect-特效',
  `status` tinyint NOT NULL DEFAULT '0' COMMENT '状态:0-排队中,1-处理中,2-完成,3-失败',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## 语音服务表结构
### voice_record (语音记录表)
```sql
CREATE TABLE `voice_record` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL COMMENT '用户ID',
  `voice_data` longblob NOT NULL COMMENT '语音数据',
  `text_content` text COMMENT '识别文本',
  `duration` int DEFAULT NULL COMMENT '语音时长(ms)',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

## 数据访问模式
1. **模型服务**:
   - 高频查询模型信息
   - 低频更新模型状态

2. **视频服务**:
   - 频繁插入任务记录
   - 频繁更新任务状态

3. **语音服务**:
   - 批量插入语音数据
   - 按用户ID查询历史记录

## 索引设计
1. 模型服务:
   - 联合索引(name,version)用于快速查找特定版本模型

2. 视频服务:
   - 用户ID索引用于查询用户任务
   - 状态索引用于任务调度

3. 语音服务:
   - 用户ID索引用于查询用户语音记录
   - 时间索引用于按时间范围查询
