# -*- coding: utf-8 -*-
# tab level: 4
#!/usr/bin/env python3.8
"""If an argument exists, it will be used to set up to the host server.\n
this module is providing basic socket server processing.
this server provide traditional socket chat between which and clients.
"""

import logging
import socket
import threading
import asyncio

from mytemplate.sockettemp import SocketTemplate as temp

logger = logging.getLogger(__name__)


class ServerSocket:
    """main socket server informaition class.

    default socket config is AF_INET and SOCK_STREAN.

    default socket address family is only AF_INET.

    this class first function is initial server socket and set information.

    Parameters
    ----------
    sock : socket
        the socket
    address_family : str
        socket address family

    Methods
    -------
    stanby_server(host_data=tuple server socket and address)
        listen server
    accept_client
        accpet clients
    create_on_client_thread(client_data=tuple client socket and address)
        create thread
    loop_chat_handler(client_socket=socket address=address)
        chat loop
    """

    def __init__(self):
        self._client = []
        self.socket = None

    def create_socket(self,
                      socket_family, socket_type,
                      *list_args, **dict_args):
        """[summary]

        Parameters
        ----------
        socket_family : [type]
            [description]
        socket_type : [type]
            [description]

        Returns
        -------
        [type]
            [description]
        """
        l_a = list_args
        d_a = dict_args
        try:
            # this blow block code is worse
            self.socket = socket.socket()
            socket.setdefaulttimeout(False)
        except OSError:
            logger.error("cant create server socket")
            return False
        else:
            mess = temp().create_server_socket(tuple(self.socket))
            logger.info(mess)
            return True

    def bind_socket(self, host_data):
        """bind address to server socket

        Parameters
        ----------
        host_data : tuple
            (ip, address)

        Returns
        -------
        bool
            if happen except return false, other hands return True
        """
        self.socket.bind(host_data)
        logger.info("succes server socket bind")

    def start_lisning_client(self, how_many=1):
        """[summary]

        Parameters
        ----------
        how_many : int, optional
            [description], by default 1
        """
        self.socket.listen(how_many)
        mess = temp().start_server()
        logger.info(mess)

    async def accept_client(self, loop):
        """this function will work only when get client connection.

        Returns
        -------
        tuple
            convain client socket and this address
        """
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        try:
            (connect_data, client_addr) = loop.run_until_compleate(
                new_loop.sock_accept(self.socket)
                )
        except OSError as e:
            logger.error("%s", e)
        return (connect_data, client_addr)
    # eternal loop

    def add_clients(self, cl_sock, addr):
        if type(addr) != tuple:
            raise ValueError
        self._client.append(cl_sock, addr)
        mess = temp.client_socket_data(cl_sock, addr)
        logger.info(mess)
        return True

    def create_on_client_thread(self, client_data):
        """this member function is wating while server working.
            this loop is fundamentally infinity loop.

            Parameters
            ----------
            client_data tuple
                need clients socket and clients address
        """

        (client_socket, client_addr) = client_data
        while True:
            try:
                with client_socket:
                    logger.info(temp().client_socket_data(
                        client_socket, client_addr
                        ))
                    chat_thread = threading.Thread(
                        target=ServerSocket.loop_chat_handler,
                        args=(client_socket, client_addr),
                        daemon=True)
                    chat_thread.start()
                    logger.info("thread start")
            except Exception as err:
                logger.error(err)

    def loop_chat_handler(self, client_socket, address):
        """main process which to do chat.

        Excaption will occuer when infinity loop is broken

        Parameters
        ----------
        client_socket: socket
            clients socket
        address: tuple
            ("0.0.0.0",1443)
        """

        recv_byte = b""
        while True:
            try:
                recv_byte = client_socket.recv(4096)
                if recv_byte is None:
                    logger.info("end chat.")
                    raise OSError
                else:
                    logger.info("Get client socket.Checking these length ")
                    self.send_message_status(recv_byte, client_socket)
            except (OSError, IOError):
                pass
            except Exception:
                pass

    async def recv_mess(self, client_socket, loop):
        nloop = asyncio.new_event_loop()
        asyncio.set_event_loop(nloop)
        try:
            message = loop.run_until_compleate(
                nloop.sock_recv(client_socket, 4096)
                )
        except Exception as e:
            logger.error(e)
        return message
    # eternal loop

    def check_message_len(self, mess):
        mess_length = len(mess)
        self.mess_length = mess_length

    def close_serversocket(self):
        mess = temp().close_server(self.socket)
        logger.info(mess)
        self.socket.close()
