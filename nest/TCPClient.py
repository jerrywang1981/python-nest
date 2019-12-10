#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Jerry Wang<wangjianjun@gmail.com>'
import socket
from .utils import pack_outgoing_message_to_nest, \
        receive_all_messages, \
        unpack_incoming_response_from_nest


class MsTcpClient():
    '''Tcp client for nestjs microservice'''
    def __init__(self, host, port):
        self.host = host
        if isinstance(port, str):
            self.port = int(port)
        else:
            self.port = port

    def send(self, pattern, data):
        '''send pattern data to microservice'''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            json_data = pack_outgoing_message_to_nest(pattern, data)
            sock.sendall(json_data)
            message = receive_all_messages(sock)

        return unpack_incoming_response_from_nest(message)
