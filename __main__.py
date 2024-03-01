from general.config import get_config
from general.logger import init_logger
from logging import getLogger

config = get_config()
init_logger(config.LOG_LEVEL, config.LOG_FILE, config.CONSOLE_ENABLED)
logger = getLogger(__name__)

if __name__ == "__main__":
    logger.debug(config.WELCOME_MESSAGE)
