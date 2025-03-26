import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
from config import settings

def setup_logging():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # 主应用日志
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler(
                log_dir/"app.log",
                maxBytes=10*1024*1024,  # 10MB
                backupCount=5
            ),
            logging.StreamHandler()
        ]
    )

    # 访问日志
    access_log = logging.getLogger("uvicorn.access")
    access_log.propagate = False
    access_handler = RotatingFileHandler(
        log_dir/"access.log",
        maxBytes=10*1024*1024,
        backupCount=5
    )
    access_log.addHandler(access_handler)

    # 错误日志
    error_log = logging.getLogger("uvicorn.error")
    error_handler = RotatingFileHandler(
        log_dir/"error.log",
        maxBytes=10*1024*1024,
        backupCount=5
    )
    error_log.addHandler(error_handler)

    # SQL日志
    sql_log = logging.getLogger("sqlalchemy.engine")
    sql_handler = RotatingFileHandler(
        log_dir/"sql.log",
        maxBytes=10*1024*1024,
        backupCount=3
    )
    sql_log.addHandler(sql_handler)
    sql_log.setLevel(logging.WARNING)
