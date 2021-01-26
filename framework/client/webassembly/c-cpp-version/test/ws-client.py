import asyncio
import websockets
import time


# 向服务器端发送认证后的消息
async def send_msg(websocket):
    while True:
        _text = input("please enter your context: ")
        if _text == "exit":
            print(f'you have enter "exit", goodbye')
            await websocket.close(reason="user exit")
            return False
        await websocket.send(_text)
        # recv_text = await websocket.recv()
        # print(f"{recv_text}")
        time.sleep(2)

# 客户端主逻辑
async def main_logic():
    async with websockets.connect('ws://127.0.0.1:8001') as websocket:
        await send_msg(websocket)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main_logic())