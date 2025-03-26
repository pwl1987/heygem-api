#!/bin/sh

# 定义资源路径
ASSETS_DIR="/app/frontend/dist/assets"
FAVICON_FILE="/app/frontend/dist/favicon.ico"
INDEX_FILE="/app/frontend/dist/index.html"
PUBLIC_ASSETS_DIR="/app/frontend/dist/public/assets"

# 设置数据路径
DATA_DIR=${DATA_DIR:-/app/data}
LOG_DIR=${LOG_DIR:-/app/logs}
CONFIG_FILE=${CONFIG_FILE:-/app/config.py}

# 检查并创建目录
mkdir -p ${DATA_DIR}/tts_audio \
         ${DATA_DIR}/video_output \
         ${DATA_DIR}/voice_output \
         ${LOG_DIR} \
         ${ASSETS_DIR} \
         ${PUBLIC_ASSETS_DIR}

# 检查必要文件
if [ ! -f ${CONFIG_FILE} ]; then
    echo "Error: Config file ${CONFIG_FILE} not found!"
    exit 1
fi

if [ ! -f ${FAVICON_FILE} ]; then
    echo "Warning: Favicon file ${FAVICON_FILE} not found!"
fi

if [ ! -f ${INDEX_FILE} ]; then
    echo "Warning: Index file ${INDEX_FILE} not found!" 
fi

# 设置环境变量
export PYTHONPATH=/app
export DATA_DIR=${DATA_DIR}
export LOG_DIR=${LOG_DIR}
export ASSETS_DIR=${ASSETS_DIR}

# 启动应用
exec python -m uvicorn main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers ${WORKERS:-4} \
    --log-config ${LOG_DIR}/uvicorn_logging.json
