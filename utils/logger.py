from loguru import logger
import os

# Create logs directory
os.makedirs("logs", exist_ok=True)

logger.add(
    "logs/ai_system.log",
    rotation="1 MB",
    retention="10 days",
    level="INFO"
)

def get_logger():
    return logger