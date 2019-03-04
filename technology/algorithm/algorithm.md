# 算法
## 基本
- 枚举法
- 递归法
- 分治法
- 贪心法
## 数据结构
- 堆栈
- 队列
- 并查集，
    朋友圈问题。 [简易说明](https://blog.csdn.net/qq_31828515/article/details/60590370)
- 线段树
- 树
    - AVL
        平衡二叉树。应用比较少，Windows进程管理
    - 红黑树(重要)
        - 每个节点要么是红色，要么是黑色。
        - 根节点必须是黑色
        - 红色节点不能连续（也即是，红色节点的孩子和父亲都不能是红色）。
        - 对于每个节点，从该点至null（树尾端）的任何路径，都含有相同个数的黑色节点。

        插入最多两次旋转，删除最多三次旋转
        插入调整策略(5种情况):
        - 父亲是黑色，无需调整
        - 右叔叔是红色
        - 右叔叔是黑色
        - 左叔叔是红色
        - 左叔叔是黑色
        近似平衡二叉树。通过对任何一条从根到叶子的简单路径上各个节点的颜色进行约束，确保没有一条路径会比其他路径长2倍，旋转次数少，效率高于AVL树，应用广泛
        - stl中map，set
        - linux进程调度
        - epoll， nginx
        - java的TreeMap等
    - B树: B树可以看作是对2-3查找树的一种扩展
        B-树中所有结点中孩子结点个数的最大值成为B-树的阶,通常用m表示，从查找效率考虑，一般要求m>=3。如果是根结点且不是叶子结点，则至少要有两个分支
        白话版: 每个节点可以有N个值，分成了N+1个范围，N必须满足(m>N>ceil(m/2)),在大块数据读取中有效率优势.
        是多路查找树，一般用于数据库中做索引，几乎都用B+树了
    - B+树
        B树的变种树，查询性能更好. 有n棵子树的节点中含有n个关键字.是为文件系统而生的
        - 每个关键字不保存数据，只用来索引，数据都保存在叶子节点。
        - 通常在b+树上有两个头指针，一个指向根结点，一个指向关键字最小的叶子结点
        - 同一个数字会在不同节点中重复出现，根节点的最大元素就是b+树的最大元素
    - Trie树
    - 霍夫曼树
    - 左偏树
- Hash表
    HashSet
    HashMap
    ConcurrentHashMap
- 链表
    计算两个链表是否相交
    计算两个链表的第一个公共子节点
- 跳表
## 动态规划
- 线性动态规划
- 树形动态规划
- 概率动态规划
## 图
- 最短路算法
- 生成树算法
- 图的联通
- 网络流
- 二分图
## 字符串
- KMP
    查找子字符串，[简易说明](http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/)
- tire树(字典书/前缀树)
- AC自动机
- 后缀数组
## 海量数据处理方法论
- Bloom filter。[参数设置k,m/n](http://pages.cs.wisc.edu/~cao/papers/summary-cache/node8.html)
    改进型：Cuckoo filter
- Hashing
- bit-map
- 堆
- 双层桶划分
- 数据库索引
- 倒排索引
- 外排序
- tire树(字典书/前缀树)
- 分布式mapreduce

## 场景
#### 排序
JDK1.7之后, 会根据排序的类型，排序的规模选择不同的排序算法
归并排序>286>双轴快排>47>插入排
![排序](./sort.png)
- 冒泡排序
- 选择排序
- 插入排序
- 希尔排序
    1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
- 堆排序
    ```
        # 在堆中做结构调整使得父节点的值大于子节点
        def max_heapify(heap, heap_size, root):
            left = 2 * root + 1
            right = left + 1
            larger = root
            if left < heap_size and heap[larger] < heap[left]:
                larger = left
            if right < heap_size and heap[larger] < heap[right]:
                larger = right
            if larger != root:
                heap[larger], heap[root] = heap[root], heap[larger]
                max_heapify(heap, heap_size, larger)


        def build_max_heap(heap):
            heap_size = len(heap)
            for i in range(heap_size // 2 - 1, -1, -1):
                max_heapify(heap, heap_size, i)
                print(a)

        def heap_sort(heap):  
            build_max_heap(heap)
            for i in range(len(heap) - 1, -1, -1):
                heap[0], heap[i] = heap[i], heap[0]
                max_heapify(heap, i, 0)
            return heap


        if __name__ == '__main__':
            a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
            print(a)
            heap_sort(a)
            print(a)
    ```
- 快速排序
    快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。
    - 单轴快排(传统/Single PivotQuickSort)
        ```
            private static void quickSort(int[] a, int low, int high) {
                if (low >= high) return;
                int base = a[low];
                int start = low, end = high;
                while (start < end) {
                    while (start < end && a[end] >= base) end--;
                    a[start] = a[end];
                    while (start < end && a[start] <= base) start++;
                    a[end] = a[start];
                }
                a[end] = base;
                quickSort(a, low, end - 1);
                quickSort(a, end + 1, high);
            }
        ```
    - 单轴快排(单向扫描划分方式)
    - 单轴快排(3 Way QuickSort/三分单向扫描)
        ```
            private static void quickSort3Way(int[] input, int lowIndex, int highIndex) {
                if (lowIndex >= highIndex) return;
                int lt = lowIndex;
                int gt = highIndex;
                int i = lowIndex + 1;

                int pivotValue = input[lowIndex];

                while (i <= gt) {
                    if (input[i] < pivotValue) {
                        swap(input, i++, lt++);
                    } else if (input[i] > pivotValue) {
                        swap(input, i, gt--);
                    } else {
                        i++;
                    }
                }
                quickSort3Way(input, lowIndex, lt - 1);
                quickSort3Way(input, gt + 1, highIndex);
            }
        ```
    - Dual-Pivot QuickSort(JDK 1.7默认)
        ```


        ```
- 归并排序
    归并排序是一种稳定的排序方法。和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是O(nlogn）的时间复杂度。代价是需要额外的内存空间。
- 计数排序
    适用于排序数的范围比较小的情况。计数排序是一个稳定的排序算法。当输入的元素是 n 个 0到 k 之间的整数时，时间复杂度是O(n+k)，空间复杂度也是O(n+k)，其排序速度快于任何比较排序算法。当k不是很大并且序列比较集中时，计数排序是一个很有效的排序算法。
- 桶排序
    桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。
- 基数排序
    基数排序基于分别排序，分别收集，所以是稳定的。但基数排序的性能比桶排序要略差，每一次关键字的桶分配都需要O(n)的时间复杂度，而且分配之后得到新的关键字序列又需要O(n)的时间复杂度。假如待排数据可以分为d个关键字，则基数排序的时间复杂度将是O(d*2n) ，当然d要远远小于n，因此基本上还是线性级别的。