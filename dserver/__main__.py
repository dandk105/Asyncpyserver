# -*- coding: utf-8 -*-
# space level: 4
"""this module is the most importing in thie app.
"""

from dserver import ServerSocket as server
from config import ConfManage as conf


if __name__ == "__main__":
    # would manage conf class
    hostdata = conf("./conf/base.json")
    hostdata.setup_logging()
    server = server()
    server.standby_server()
    server.accept_client()
