
import asyncio
from eventcreater import EventCreater


class RecvEvent():
    def __init__(self):
        self.loop = EventCreater().create_loop()

    async def recv_message(self, socket, len_bytes=2048):
        coro = self.loop.sock_recv(socket, len_bytes)
        message = await self.loop.run_until_complete(coro)
        return message
