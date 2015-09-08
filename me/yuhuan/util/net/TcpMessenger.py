#!/usr/bin/env python
# -*- coding: utf-8; -*-

""""""
import socket
import struct

__author__ = "Yuhuan Jiang"
__email__ = "jyuhuan@gmail.com"
__version__ = "1.0"


class TcpMessenger:
    def __init__(self, host_name, port_number):
        self.server_socket = socket.socket()
        self.server_socket.connect((host_name, port_number))

    def send_int(self, int_value):
        self.server_socket.send(struct.pack(">I", int_value))

    def send_string(self, unicode_str):
        self.server_socket.send(struct.pack("!H", len(unicode_str)))
        self.server_socket.send(unicode_str)

    def send_strings(self, unicode_strings):
        self.send_int(len(unicode_strings))
        for unicode_str in unicode_strings:
            self.send_string(unicode_str)

