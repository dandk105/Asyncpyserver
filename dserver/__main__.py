# -*- coding: utf-8 -*-
# space level: 4
"""this module is the most importing in thie app.
"""
import sys
import asyncio

from .dserver import ServerSocket
from .config import ConfManage as conf


async def main():
    """
    docstring
    """
    # would manage conf class
    try:
        current_loop = asyncio.get_running_loop()
        asyncio.set_event_loop(current_loop)
        hostdata = conf()
        server = ServerSocket()
        result = await server.create_socket(hostdata.address, hostdata.port)
        if result is False:
            sys.exit()
    except OSError:
        pass


asyncio.run(main())
