# 算法
## 基本
- 枚举法
- 递归法
- 分治法
- 贪心法
## 数据结构
- 堆栈
- 队列
- 并查集
- 线段树
- 树
    - AVL
        平衡二叉树。应用比较少，Windows进程管理
    - 红黑树
        近似平衡二叉树。通过对任何一条从根到叶子的简单路径上各个节点的颜色进行约束，确保没有一条路径会比其他路径长2倍，旋转次数少，效率高于AVL树，应用广泛
        - stl中map，set
        - linux进程调度
        - epoll， nginx
        - java的TreeMap等
    - B树
        是多路查找树，一般用于数据库中做索引，几乎都用B+树了
    - B+树
        B树的变种树，有n棵子树的节点中含有n个关键字，每个关键字不保存数据，只用来索引，数据都保存在叶子节点。是为文件系统而生的
    - Trie树
    - 霍夫曼树
    - 左偏树
- Hash表
    HashSet
    HashMap
    ConcurrentHashMap
- 链表，跳表
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

# 字符串
- KMP
    查找子字符串，[简易说明](http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/)
- tire树(字典书/前缀树)
- AC自动机
- 后缀数组
#海量数据处理方法论
- Bloom filter。[参数设置k,m/n](http://pages.cs.wisc.edu/~cao/papers/summary-cache/node8.html)
    改进型：Cuckoo filter
- Hashing
- bit-map
- 堆（Top N)
- 双层桶划分
- 数据库索引
- 倒排索引
- 外排序
- tire树(字典书/前缀树)
- 分布式mapreduce