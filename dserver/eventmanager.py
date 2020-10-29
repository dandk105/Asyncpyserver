
import asyncio
from dserver import ServerSocket as server


class EventManager():
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.socket = server()

    def loop_corutine(self, coro):
        asyncio.run(coro)
