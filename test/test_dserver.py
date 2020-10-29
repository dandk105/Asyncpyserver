# -*- coding: utf-8 -*-
# tab level: 4
#!/usr/bin/env python3.8
"""test main module.

"""

import itertools
import socket
import unittest
from unittest.mock import MagicMock

from src.dserver import ServerSocket as ds
from src.config import ConfManage as cm


def return_converted_dict(key, *value):
    """this method create dict from token key and value parameters.
    It is converted element of list,
    if parameters of this method get the str.

    NOTE
    ----
    if you give str to parameters of this method,
    Dictionary return key will be unexpected

    Parameters
    ----------
    key : sequence
        [description]
    value : list tuple
        [description]

    Returns
    -------
    dictionary : dict
        if length of key and value is not much droped value other one
    """
    dictionary = {}
    for key, val in zip(key, value):
        dictionary[key] = val
    return dictionary


def return_list_from_set(sets, convain_num=2):
    """[summary]

    Parameters
    ----------
    sets : [type]
        [description]
    convain_num : int, optional
        [description], by default 2

    Returns
    -------
    com_li: list
        [description]
    """
    com_li = []
    for i in itertools.combinations(sets, convain_num):
        com_li.append(i)
    return com_li


class TestDserver(unittest.TestCase):
    """test dserver class.
    many option should check.
    """

    def setUp(self):
        self.dumy4_class = ds()
        cm().setup_logging()

    def test_muching_return_sockettypes(self):
        option = [(socket.AF_INET, socket.SOCK_STREAM),
                  [socket.AF_INET, socket.SOCK_STREAM],
                  {"family": socket.AF_INET,
                   "type": socket.SOCK_STREAM}
                  ]
        # test = {"AF_INET", "AF_INET6", "AF_UNIX", "SOCK_STREAM", "SOCK_DGRAM"}
        for item in option:
            with self.subTest(item=item):
                result = self.dumy4_class.create_socket(*item)
                self.assertIs(result, True)

    def test_creating_several_socket(self):
        soc6_mock = MagicMock(address_type="AF_INET6")
        soc4_mock = MagicMock(address_type="AF_INET")
        test_petttern_6 = ds(soc6_mock)
        test_petttern_4 = ds(soc4_mock)
        famlily6 = "AF_INET6"
        family4 = "AF_INET"
        self.assertIs(famlily6, test_petttern_6.socket.family)
        self.assertIs(family4, test_petttern_4.socket.family)

    def test_start_ip4_server(self):
        dumy_host_tuple = ("0.0.0.0", 1334)
        start_status = self.dumy4_class.standby_server(dumy_host_tuple)
        self.assertEqual(True, start_status)

    @unittest.skip("this method is not ready to test.")
    def test_loopchat_handler(self):
        self.dumy4_class.loop_chat_handler()

    def test_async_accept_client(self):
        pass

    def tearDown(self):
        if self.dumy4_class.socket is not None:
            self.dumy4_class.socket.close()


if __name__ == "__main__":
    TestDserver.run()
