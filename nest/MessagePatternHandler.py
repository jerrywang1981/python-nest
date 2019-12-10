#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Jerry Wang<wangjianjun@gmail.com>'


class MessagePatterBaseHandler():
    '''base class for message pattern handler'''
    def __init__(self):
        pass

    def get_message_pattern(self):
        '''return the message pattern

        { cmd: UPDATE_JOB }
        then this should return UPDATE_JOB
        '''
        raise NotImplementedError

    def handle(self, payload):
        '''handler function to process payload

        It should returns
        err - any error or None
        result - the processed result
        '''
        raise NotImplementedError
