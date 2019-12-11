#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Jerry Wang<wangjianjun@gmail.com>'
import socketserver
import functools
from .TCPServer import MsTcpHandler


class NestMsServer():
    '''Nest style microservice server

    '''
    def __init__(self, host='0.0.0.0', port=None):
        self.host = host
        if port:
            if isinstance(port, str):
                self.port = int(port)
            else:
                self.port = port
        else:
            self.port = None

    def add_handler(self, message_handler_class):
        '''add handler'''
        message_handler = message_handler_class()
        cmd = message_handler.get_message_pattern()
        pattern_key = MsTcpHandler.get_key(cmd)
        if pattern_key in MsTcpHandler.MS_HANDLERS:
            raise Exception('You have registered it before')

        MsTcpHandler.MS_HANDLERS[pattern_key] = message_handler

    def message_pattern(self, pattern_name):
        '''message pattern decorator'''
        pattern_key = MsTcpHandler.get_key(pattern_name)

        def decorator(func):
            @functools.wraps(func)
            def wrapper(payload):
                return func(payload)

            if pattern_key in MsTcpHandler.MS_HANDLERS:
                raise Exception('You have registered it before')
            MsTcpHandler.MS_HANDLERS[pattern_key] = wrapper
            return wrapper
        return decorator

    def run(self, host='0.0.0.0', port=None):
        '''start to run the server'''
        self.__init__(host, port)
        with socketserver.TCPServer((self.host, self.port), MsTcpHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C
            server.serve_forever()

