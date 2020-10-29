
import socket
import logging

from mytemplate.sockettemp import SocketTemplate as template
from config import ConfManage as config

logger = logging.getLogger(__name__)


class InitServer():
    def __init__(self):
        self.templates = template()
        self.socket = None
        self.platform = config().get_plaformdata()
        self.able_constant = {
            socket.AF_INET, socket.AF_INET6,
            socket.AF_UNIX, socket.SOCK_DGRAM, socket.SOCK_STREAM
                             }

    def return_items(self, obj):
        items = []
        if type(obj) is dict:
            obj = obj.items
        for i in obj:
            items.append(i)
        return items

    def output_constant(self, obj):
        constant = []
        constant = self.return_items(obj)
        return constant

    def set_socket_constant(self):
        socket_constants = {
            socket.AF_INET, socket.AF_INET6,
            socket.AF_UNIX, socket.SOCK_DGRAM, socket.SOCK_STREAM
                           }

    def check_exsistance_socket_options(self, *options):
        # How do this method if group of args is same?
        if len(options) < 2:
            raise TypeError
        socket_options = set()
        for i in self.able_constant:
            socket_options.add(i.name)
        common = socket_options.intersection(options)
        if len(common) < 2:
            raise False
        else:
            return True

    def create_socket(self, options):
        """[summary]

        Returns
        -------
        bool
            this method  will return False if Error happen
        """
        socket_opt = options
        try:
            self.socket = socket.socket(socket_opt)
            socket.setdefaulttimeout(False)
        except OSError:
            logger.error("could not create server socket")
            return False
        else:
            tuple_sock = (self.socket,)
            mess = self.templates.create_server_socket(tuple_sock)
            logger.info(mess)
            return self.socket

    def bind_socket(self, address):
        self.socket.bind(address)
        mess = self.templates.create_server_socket(address)
        logger.info(mess)

    def listen_socket(self, clients):
        self.socket.listen(clients)
        mess = self.templates.start_server(clients)
        logger.info(mess)


if __name__ == "__main__":
    initialize = InitServer()
