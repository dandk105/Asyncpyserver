
import itertools
import unittest
from unittest.mock import MagicMock, patch

from src.initserver import InitServer as init


class TestInit(unittest.TestCase):

    def setUp(self):
        self.initialize = init()
        self.socketset = {"AF_INET", "SOCK_STREAM", "AF_UNIX", "SOCK_DGRAM"}

    def test_socket_initialize(self):
        status = self.initialize.socket
        self.assertIsNone(status)

    def test_check_socketoption(self):
        option = [[], ["SOCK_STREAM"], ["AF_INET"], ["SOCK_STREAM", "AF_INET"]]
        for i in option:
            with self.subTest(i=i):
                res = self.initialize.check_exsistance_socket_options(i)
                self.assertTrue(res)

    def test_create_socket(self):
        options = itertools.combinations(self.socketset, 2)
        for i in options:
            with self.subTest(i=i):
                res = self.initialize.create_socket(i)
                self.assertTrue(res)

    def test_could_call_template_first(self):
        with patch('template') as mock:
            instance = mock.return_value
            instance.method.return_value = 'sucssess'
            result = init()
            ex = 'sucssess'
            self.assertIs(ex, result)

    def test_bind_socket(self):
        self.initialize.bind_socket()
        res = self.initialize.socket
        # test socket self.
        self.assertEqual(res, ("127.0.0.1", 12345))

    def test_raise_custom_error(self):
        self.initialize._sock_opt = None
        self.assertRaises(
            OSError,
            self.initialize.create_socket()
                         )

    def tearDown(self):
        if self.initialize.socket is not None:
            self.initialize.socket.close()
