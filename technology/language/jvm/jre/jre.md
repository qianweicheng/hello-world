# Java Runtime Environment(JRE)
## 数据结构
#### HashMap
HashSet底层使用hashMap实现
- 数组Entity
    填充因子: 0.75
- Node:
    当数量少时，用LinkedList，当数量到达8时候，使用NodeTree(红黑)
#### SparseArray
从这里可以看出Android里面，很多时候需要时间换空间
- 数组实现，使用二分查找
- 主要是为了节省内存，比HashMap慢一些
#### WeakHashMap
Entry<K,V> extends WeakReference<Object>
- Key是WeakReference
- Value是强引用
- 在计算size等的时候expungeStaleEntries一次清除掉无效的Entry
#### ThreadLocal
每个Thread都有个ThreadLocal.ThreadLocalMap，用来存储ThreadLocal的值
```
Entry extends WeakReference<ThreadLocal<?>>
- value
```
## Reference
- StrongReference
- SoftReference
    内存紧张时回收
- WeakReference
    GC时回收
- PhantomReference
    跟WeakReference的区别时，它必须结合ReferenceQueue，手动从Queue中清除poll/remove。
    PhantomReference对象插入ReferenceQueue队列，而此时PhantomReference对象并没有被垃圾回收器回收，而是要等到ReferenceQueue被你真正的处理后才会被回收。
- ReferenceQueue
    在构造Reference的时候，传入ReferenceQueue， 则再回收Reference的时候，会把其放入ReferenceQueue