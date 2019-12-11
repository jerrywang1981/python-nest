#!/usr/bin/env python
# -*- coding:utf-8 -*-

from nest import NestMsServer, MessagePatternBaseHandler

app = NestMsServer()

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
        '''return the message pattern

        it can be string or dict
        e.g. 'TEST' or {'cmd': 'test'}
        '''
        return {'cmd': 'TEST_PATTERN' }

    def handle(self, payload):
        '''handler function to process payload

        It should returns
        err - any error or None
        result - the processed result
        '''
        print(payload)
        return None, ['this is test dict', 'another test dict result']


@app.message_pattern({'cmd': 'test_decorator'})
def test_decorator(payload):
    '''test decorator'''
    print(payload)
    return None, payload

if __name__ == '__main__':
    HOST ='localhost'
    PORT = 7086
    app.add_handler(TestHanlder)
    app.add_handler(TestDictHanlder)
    print(f'started to run and listed to port {PORT}')
    app.run(HOST, PORT)
