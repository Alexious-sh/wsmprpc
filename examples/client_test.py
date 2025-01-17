import asyncio, websockets
from wsmprpc import RPCClient

async def main():
    async with websockets.connect('ws://localhost:8000') as ws:
        stub = RPCClient(ws)

        # normal rpc
        print(await stub.div(1, 3))

        # cancellation
        s = stub.sleep(3)
        async def cancel_sleep():
            await asyncio.sleep(1)
            s.cancel()
        try:
            asyncio.get_event_loop().create_task(cancel_sleep())
            print(await s)
        except asyncio.CancelledError as e:
            print('cancelled')

        # request-streaming
        print(await stub.sum(request_stream=range(1, 3)))

        # response-streaming
        async for i in stub.repeat('bla...', 4):
            print(i)

        # combine request-streaming and response-streaming
        async for i in stub.uppercase(request_stream=['hello', 'rpc']):
            print(i)


asyncio.get_event_loop().run_until_complete(main())
