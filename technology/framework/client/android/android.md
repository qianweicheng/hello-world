# Android
## Install
- HAXM: 硬件加速起，模拟器使用
## Build Project
- Gradle
- BUCK(Facebook)
## 常用框架
https://blog.csdn.net/csdn_aiyang/article/details/56016649
- okhttp
- retrofit
- RxJava+RxAndroid
- Dragger2
## Handler, Message, Looper, MessageQueue
Looper是核心:
- 负责调用Handler->dispatchMessage
- 负责创建MessageQueue
- Handler在创建的时候引用了Looper和Looper.MessageQueue
```
class LooperThread extends Thread {
    public Handler mHandler;
    public void run() {
        Looper.prepare();

        mHandler = new Handler() {
            public void handleMessage(Message msg) {
                // process incoming messages here
            }
        };

        Looper.loop();
    }
}
```
## Android AIDL
## Inter-Process-Communication(IPC)

## 序列化
#### 序列化场景
1. 永久性保存对象，保存对象的字节序列到本地文件中；
2. 通过序列化对象在网络中传递对象；
3. 通过序列化在进程间传递对象。 
#### Serializable 和 Parcelable 区别
1. 在使用内存的时候，Parcelable 类比Serializable性能高，所以推荐使用Parcelable类。
2. Serializable在序列化的时候会产生大量的临时变量，从而引起频繁的GC。

## Inteview
- UserControls
- Theme Style