# RX响应式编程
rxcpp大部分计算都是基于可观测的概念。该库提供了大量原语来创建来自各种数据源的可观察流。数据源可以是范围、stl容器等等。我们可以在可观察对象和它们的消费者之间放置操作符(称为观察者)。由于函数编程构造支持函数的组合，所以我们可以将操作符链作为单个实体放在可观察对象和订阅流的观察者之间。与库关联的调度程序将确保当数据以可观察流的形式可用时，它将通过操作符传递，并且在经过一系列筛选和转换之后，如果有数据存在，将向订阅者发出通知。当调用订阅者中的一个lambda方法时，观察者需要考虑一些事情。观察员可以把注意力集中在他们主要负责的任务上。
## RXCPP
`auto observable = rxcpp::observable<>::range(1, 12);`
```
    std::array< int, 3 > a={{1, 2, 3}};
    auto values1 = rxcpp::observable<>::iterate(a);
```
```
auto ints = rxcpp::observable<>::create<int>([](rxcpp::subscriber<int> s) {
    s.on_next(1);
    s.on_next(4);
    s.on_next(9);
    s.on_completed();
    });
```