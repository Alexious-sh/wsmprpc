# wsmpRPC

Python msgpack RPC over websocket

## Features

* **Asynchronous**
* Compared to json, [msgpack](https://msgpack.org/) can transfer **binary data**.
* Client is able to **cancel** long running calculation on server.
* Supports **Bidirectional streaming** RPC, where the client sends or receives a sequence of messages to/from server within one RPC. Similar to [gRPC](https://grpc.io/docs/tutorials/basic/python/).
* No need to define .proto files, thanks to python's dynamic features, RPC methods defined on server side can be readily used by client as if it's client's own method.
* Easy integration into any async web frameworks that supports websocket.
* lib for **javascript** client on web browser

## Install

`pip install wsmprpc`

## Dependency:
[python](https://msgpack.org/) and [javascript](https://github.com/ygoe/msgpack.js) versions of msgpack 

## Examples
* [server_test.py](https://github.com/hyansuper/wsmprpc/blob/master/examples/server_test.py)
* [client_test.py](https://github.com/hyansuper/wsmprpc/blob/master/examples/client_test.py)
* [client_test.html (javascript client)](https://github.com/hyansuper/wsmprpc/blob/master/js/client_test.js)