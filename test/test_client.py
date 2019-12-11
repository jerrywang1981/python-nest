#!/usr/bin/env python
# -*- coding:utf-8 -*-

from nest import NestMsClient

if __name__ == '__main__':
    HOST ='localhost'
    PORT = 7086
    client = NestMsClient(HOST, PORT)
    pattern = 'TEST_PATTERN'
    res = client.send(pattern, None)
    print(res)
    pattern = { 'cmd' :'TEST_PATTERN' }
    res = client.send(pattern, None)
    print(res)
    pattern = { 'cmd' :'test_decorator' }
    res = client.send(pattern, 'this is ok')
    print(res)
