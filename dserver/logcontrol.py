
import logging


class LogControl():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def info_output(self, mess, level):
        self.logger