from general.config import get_config
from general.logger import init_logger
from logging import getLogger
import asyncio
from messages import TextMessage

config = get_config()
init_logger(config.LOG_LEVEL, config.LOG_FILE, config.CONSOLE_ENABLED)
logger = getLogger(__name__)


async def run():
    phone = input("Phone number (example: +48123456789): ")
    message = input("Message (example: Hello World!): ")
    async with TextMessage(config.PORT) as device:
        device.send_message(message, phone)
        logger.info(f"Sent message: {message} to {phone}")

if __name__ == "__main__":
    asyncio.run(run())
