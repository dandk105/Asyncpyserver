# -*- coding: utf-8 -*-
# tab level: 4
# !/usr/bin/env python3
"""
this module setting a logging module
in started this server.
"""


import logging
import logging.config
import logging.handlers
import json
import os
from pathlib import Path

from mytemplate.errorclass import CustomError as customerr

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ConfManage:
    """this class manage all config on this server.

    this class use setting data from pyserver/conf/json file in default.

    Methods
    -------
    convert_path(relative_path)
        return absolute path
    load_data_dict
        set json data
    return_server_addr
        return tuple of server data
    subsclibe_client(client_address)

    """

    def __init__(self, env_path):
        self.abs_path = None
        self.confi_set = {}
        self.env = os.getenv("PY_SERVER_CONF")
        if env_path is None:
            self.rel_path = self.env
        else:
            self.rel_path = env_path

    def setup_logging(self,
                      Defaultpath="./conf/logconf.json",
                      Defaultlevel=logging.INFO,
                      Envkey="LOG_CFG"
                      ):
        """this method setting of logging.
        default logging level is INFO.
        if you want to change level,you should change Defaultlevel parameters.

        Parameters
        ----------
        Defaultpath : str, optional
            [description], by default "./conf/logconf.json"
        Defaultlevel : logginLevel, optional
            [description], by default logging.INFO
        Envkey : str, optional
            [description], by default "LOG_CFG"
        """
        log_locate_rel = Defaultpath
        log_locate_abs = self.convert_path(log_locate_rel)
        abs_path = Path(log_locate_abs)
        if abs_path.exists():
            c_dict = self.load_jsonfile(str(abs_path))
            logging.config.dictConfig(c_dict)
        else:
            logging.basicConfig(level=Defaultlevel)

    def convert_path(self, relative_path):
        """return boolean parameter.
        This function return Flase if happend error.

        Parameters
        ----------
        relative_path : str

        Returns
        -------
        abs_path : str
        """
        try:
            if self.rel_path is not None:
                relative_path = self.rel_path
            rel_path = Path(relative_path)
            abs_path = rel_path.resolve(strict=True)
        except FileNotFoundError:
            raise customerr.PathError
        except Exception as e:
            logger.error(e)
        else:
            return str(abs_path)

    def return_pathobj(self, abs_path):
        path = Path(abs_path)
        return path

    def output_fileobj(self, abs_path):
        path = self.return_pathobj(abs_path)
        try:
            with path.open("r", encoding="utf-8") as f:
                obj = self.format_IO(f)
        except TypeError as e:
            print(e)
        return obj

    def format_IO(self, IO):
        # bad condition
        if IO is True:
            Fobj = json.loads(IO)
        elif IO is False:
            Fobj = IO.read()
        else:
            raise OSError
        return Fobj

    def load_jsonfile(self, abs_path):
        """this method convert JSON file to fit object of python,
        So this can only be used for JSON files.

        Patameters
        ----------
        abs_path: str
            purpose json file path

        Returns
        -------
        py_dataobj: Python object
        """
        path = self.return_pathobj(abs_path)
        try:
            with path.open(mode="r", encoding="utf-8") as f:
                py_dataobj = json.load(f)
                logger.info("%s", "read conf file sucess.")
        except (OSError, json.JSONDecodeError):
            logger.error("%s", "cant read conf file. should check there is config file")
            return None
        else:
            return py_dataobj

    def return_server_addr(self):
        """this method get path data from its args.
        which return tuple about this server address data.

        Returns
        -------
        conf_tuple : tuple
            exsample ("0.0.0.0",1234)
        """
        conf_dict = self.confi_set.copy()
        key = conf_dict.keys()
        ip_port = ("host_ip", "host_port")
        # bad code
        if key is ip_port[0] & key is ip_port[1]:
            conf_tuple = conf_dict[ip_port[0]], conf_dict[ip_port[1]]
        logger.info("%s", "compleate this app conf")
        return conf_tuple
