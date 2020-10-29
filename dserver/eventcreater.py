
import asyncio


class EventCreater():
    def create_loop(self):
        eventloop = asyncio.get_event_loop()
        return eventloop
