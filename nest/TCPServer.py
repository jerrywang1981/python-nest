#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Jerry Wang<wangjianjun@gmail.com>'
import socketserver
import json
#  import os
#  import sys
#  sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from .utils import unpack_incoming_message_from_client, \
        receive_all_messages, \
        pack_outgoing_message_to_client


class MsTcpHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    """
    MS_HANDLERS = dict()

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.data = None
        self.pattern = None
        self.payload = None
        self.message_id = None

    def __dispatch(self):
        '''dispatch the pattern and payload'''
        pattern_key = self.get_key(self.pattern)
        if pattern_key in self.MS_HANDLERS:
            return self.MS_HANDLERS[pattern_key].handle(self.payload)
        raise Exception('no handler found')

    @classmethod
    def get_key(cls, key):
        '''get the key as string'''
        if isinstance(key, str):
            return key

        if isinstance(key, dict):
            return json.dumps(obj=key)

        raise KeyError('not a valid pattern')

    def handle(self):
        '''handler function'''
        self.data = receive_all_messages(self.request)
        self.pattern, self.payload, self.message_id = \
            unpack_incoming_message_from_client(self.data)
        err, result = self.__dispatch()
        self.request.sendall(
            pack_outgoing_message_to_client(result, self.message_id, err))
