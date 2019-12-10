#!/usr/bin/env python
# -*- coding:utf-8 -*-

from nest import NestMsServer, MessagePatternBaseHandler


class TestHanlder(MessagePatternBaseHandler):
    def __init__(self):
        pass

    def get_message_pattern(self):
        return 'TEST_PATTERN'

    def handle(self, payload):
        print(payload)
        return None, ['this is test', 'another test result']

class TestDictHanlder(MessagePatternBaseHandler):
    def __init__(self):
        pass

    def get_message_pattern(self):
        return {'cmd': 'TEST_PATTERN' }

    def handle(self, payload):
        print(payload)
        return None, ['this is test dict', 'another test dict result']

if __name__ == '__main__':
    HOST ='localhost'
    PORT = 7086
    app = NestMsServer(HOST, PORT)
    app.add_handler(TestHanlder)
    app.add_handler(TestDictHanlder)
    print(f'started to run and listed to port {PORT}')
    app.run()
