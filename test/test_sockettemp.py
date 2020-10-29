
import unittest

from mytemplate.sockettemp import SocketTemplate as socktemp


class DemoData():
    def __init__(self):
        self.client_sock = ("this is client socket")
        self.client_addr = ("192.0.0.255")


demo = DemoData()


class TestTempmess(unittest.TestCase):

    def test_sock_data(self):
        c_sock = socktemp().client_socket_data(
            socket=demo.client_sock,
            addr=demo.client_addr
            )
        self.assertEqual(str, type(c_sock))
        print(c_sock)
