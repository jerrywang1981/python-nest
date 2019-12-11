# python-nest
Python library for nest style Microservices

# Description

There is one nodejs framework named [nestjs](https://nestjs.com) which is perfect to develop microservices. but we wanted to
implement some microservices in python to work together with nestjs framework, I didn't find a solution, so I developed this 
package to do that, for now, it only implemented the [MessagePattern](https://docs.nestjs.com/microservices/basics#request-response) 
so in nestjs, it is @MessagePattern and we can have same function in python with this lib/package.


# How to use

## Install latest version
```python
pip install python-nestjs
```
## The microservices server

in nestjs, you can do it with @MessagePattern, and the pattern can be string or object in nestjs, similarly
in python the pattern can also be str or dict, you can find sample code [test_server.py](test/test_server.py)
here is sample code, e.g.

### in your `nest_server.py`
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from nest import NestMsServer, MessagePatternBaseHandler

app = NestMsServer()

```

### to have handler function to process the pattern, you have two options
* have a class which extends `MessagePatternBaseHandler` 

1. have the class
```python
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
```
2. add/register the handler class
```python
app.add_handler(TestDictHanlder)
```

* have a function decorated with decorator `message_pattern`
1. write a function and decorate it
```python
@app.message_pattern({'cmd': 'test_decorator'})
def test_decorator(payload):
    '''test decorator function

    the function accepts one parameter payload
    '''
    print(payload)
    return None, payload
```
### start/run it
```python
    HOST ='localhost'
    PORT = 7086
    print(f'started to run and listed to port {PORT}')
    app.run(HOST, PORT)
```

## The microservices client

if you want to call microservices which was implemented in nestjs, it is also simple, find in [test_client.py](test/test_client.py)
or sample code here.
```python
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
```

# Maintainers
[@jerrywang1981](https://github.com/jerrywang1981)

# Contributors
[![](https://github.com/jerrywang1981.png?size=50)](https://github.com/jerrywang1981)

# License
MIT License
