# 基本数据机构
## Map
Map(I)
^
|
SortedMap(I)
^
|--------------------|
NavigableMap    AbstractMap
|                    |  |  
----------------------  |----------------------
         |                    |                |
      TreeMap               HashMap         IdentityHashMap
                              |
                            LinkedHashMap


## Set
HashSet 内部聚合一个HashMap
TreeSet
## List
Iterable<-Collection
            |
    ---------------------------------
    |                 |             |
 List(I)           Queue(I)       AbstractCollection(C)
                      |             |
                   Deqeue(I)      AbstractList
                      |             |
                      |           AbstractSequentialList
                      |             |
                      ---------------
                             |
                          LikedList
## Array
Arrays.copyOf,Arrays.copyOfRange 底层都是System.arraycopy
## HashMap
HashSet底层使用hashMap实现
- 数组Entity
    填充因子: 0.75
- Node:
    当数量少时，用LinkedList，当数量到达8时候，使用NodeTree(红黑)
## SparseArray(Android Only)
从这里可以看出Android里面，很多时候需要时间换空间
- 数组实现，使用二分查找
- 主要是为了节省内存，比HashMap慢一些
#### WeakHashMap
Entry<K,V> extends WeakReference<Object>
- Key是WeakReference
- Value是强引用
- 在计算size等的时候expungeStaleEntries一次清除掉无效的Entry