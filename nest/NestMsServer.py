#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Jerry Wang<wangjianjun@gmail.com>'
import socketserver
from .TCPServer import MsTcpHandler


class NestMsServer():
    '''Nest style microservice server

    '''
    def __init__(self, host, port):
        self.host = host
        if isinstance(port, str):
            self.port = int(port)
        else:
            self.port = port

    def add_handler(self, message_handler_class):
        '''add handler'''
        message_handler = message_handler_class()
        cmd = message_handler.get_message_pattern()
        pattern_key = MsTcpHandler.get_key(cmd)
        if pattern_key in MsTcpHandler.MS_HANDLERS:
            raise Exception('You have registered it before')

        MsTcpHandler.MS_HANDLERS[pattern_key] = message_handler

    def run(self):
        '''run the server'''
        with socketserver.TCPServer((self.host, self.port), MsTcpHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C
            server.serve_forever()

