#!/usr/bin/env python
# -*- coding:utf-8 -*-

from nest import NestMsServer, MessagePatternBaseHandler


class TestHanlder(MessagePatternBaseHandler.MessagePatterBaseHandler):
    def __init__(self):
        pass

    def get_message_pattern(self):
        return 'TEST_PATTERN'

    def handle(self, payload):
        print(payload)
        return None, ['this is test', 'another test result']

if __name__ == '__main__':
    HOST ='localhost'
    PORT = 7086
    app = NestMsServer.NestMsServer(HOST, PORT)
    app.add_handler(TestHanlder)
    app.run()
