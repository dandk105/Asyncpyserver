
import asyncio
import logging

logger = logging.getLogger(__name__)


class AcceptEvent():
    def __init__(self):
        self.loop = asyncio.new_event_loop()

    async def accept_client(self, loop):
        """this function will work only when get client connection.

        Returns
        -------
        tuple
            convain client socket and this address
        """
        asyncio.set_event_loop(self.loop)
        try:
            (connect_data, client_addr) = loop.run_until_compleate(
                self.loop.sock_accept(self.socket)
                )
        except OSError as e:
            logger.error("%s", e)
        return (connect_data, client_addr)
        # eternal loop
