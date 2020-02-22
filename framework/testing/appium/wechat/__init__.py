import threading


def post_runnable(func):
    print('Hello Timer!')
    timer = threading.Timer(0.001, func)
    timer.start()
