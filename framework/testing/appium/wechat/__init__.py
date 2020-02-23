import threading


def post_runnable(func, delay=0.001):
    print('Hello Timer!')
    timer = threading.Timer(delay, func)
    timer.start()
