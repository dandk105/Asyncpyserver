
import asyncio
from eventcreater import EventCreater


class SendEvent():
    def __init__(self):
        self.loop = EventCreater().create_loop()
        self.coro = None

    def send_message(self, socket, len_bytes):
        coro = self.loop.sock_sendall(socket, len_bytes)
        self.coro = coro

    def subsc_coro(self):
        self.loop.run_until_complete(self.coro)
