from serial import Serial
import asyncio


class TextMessage():
    """
    A class to send text messages using a GSM modem.
    """
    port: str
    timeout: float
    baudrate: int
    __connection: Serial

    def __init__(self,
                 port: str,
                 baudrate: int = 115200,
                 timeout: float = 5):
        self.port = port
        self.timeout = timeout
        self.baudrate = baudrate

    def __connect(self):
        """Connect to the device."""
        self.__connection = Serial(
            self.port,
            self.baudrate,
            timeout=self.timeout
        )

    def __disconnect(self):
        """Disconnect from the device."""
        self.__connection.close()

    async def send_message(self, message: str, phone_number: str):
        """
        Send a text message.
        Args:
            message (str): The message to send.
            phone_number (str): The phone number to send the message to.
        """
        await asyncio.sleep(0.1)
        self.__connection.write(b'ATZ\r')
        await asyncio.sleep(0.1)
        self.__connection.write(b'AT+CMGF=1\r')
        await asyncio.sleep(0.1)
        self.__connection.write(b'AT+CMGS="' + phone_number.encode() + b'"\r')
        await asyncio.sleep(0.1)
        self.__connection.write(message.encode() + b"\r")
        await asyncio.sleep(0.1)
        self.__connection.write(bytes([26]))
        await asyncio.sleep(0.1)

    async def __aenter__(self):
        self.__connect()
        return self

    async def __aexit__(self, _, __, ___):
        self.__disconnect()
