# Python async
常见的阻塞形式有：网络I/O阻塞、磁盘I/O阻塞、用户输入阻塞等。
## multi-process
## Threading
## 协程
- yield(Python 2.2)
    `yield some-value`
    `result = yield some-value` and `xxx.send(result)`
- yield from(Python3.3)
    使用它可以把复杂的生成器重构成小型的嵌套生成器,比如生成器里面调用另外的生成器
    ```
    >>> def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i
    ```
    等价
    ```
    >>> def gen():
        yield from 'AB'
        yield from range(1, 3)
    ```
- await/async(Python3.4)
- asyncio库(Python3.5)
    ```
    async def do_some_work(x):
        print("waiting:", x)
    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    # 将协程加入到事件循环loop
    loop.run_until_complete(coroutine)
    ```
