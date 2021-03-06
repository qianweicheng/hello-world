## 统一建模语言(UML)的模型主要有三部分构成
- 事物(Things)：UML模型中最基本的构成元素，是具有代表性的成分的抽象 
- 关系(Relationships)：关系把事物紧密联系在一起 
- 图(Diagrams )：图是事物和关系的可视化表示 
## UML关系
- 依赖
    >当工具在使用（... uses a ...），并不拥有引用关系。而这种使用关系是具有偶然性、临时性的、非常弱的，但是B类的变化会影响到A；表现在代码层面，为类B作为参数被类A在某个method（方法）中使用。用带燕尾箭头的虚线表示。表示一个类依赖于另外一个类的定义；依赖关系仅仅描述了类与类之间的一种使用与被使用的关系。`带箭头的虚线`
- 关联
    >C1-C2：指双方都知道对方的存在，都可以调用对方的公共属性和方法。关联的两个对象彼此间没有任何强制性的约束，只要二者同意，可以随时解除关系或是进行关联，它们在生命期问题上没有任何约定。`（带箭头）实线`
- 聚合
    >聚合是关联的一种特殊形式。当类之间有整体-部分关系的时候，我们就可以使用组聚合。是“弱”的包含（" ... owns a ..." ）关系 `带空心箭头的实线`
- 组合/合成
    >合成是聚合的一种特殊形式，暗示“局部”在“整体”内部的生存期职责。合成也是非共享的。所以，虽然局部不一定要随整体的销毁而被销毁，但整体要么负责保持局部的存活状态，要么负责将其销毁。`带实心箭头的实线`

- 泛化（继承）
    用带空心三角形箭头的实线表示。
- 实现
    用带空心三角形箭头的虚线表示。

## UML图
#### UML 类图:
类图是使用面向对象的社会最流行的 UML 图。它描述了在一个系统中的对象和他们的关系，能够让我们在正确编写代码以前对系统有一个全面的认识。

一个单独的类图描述系统的一个具体方面，收集类图表示整个系统。基本上，类图表示系统的静态视图。

类图是唯一可以直接映射到面向对象的语言UML图。因此，它被广泛应用于开发者社区。

#### UML 对象图：
对象图是类图的一个实例。因此，一类图的基本要素是类似的。对象图是由对象和链接。在一个特定的时刻，它捕获该系统的实例。

对象图用于原型设计，逆向工程和实际场景建模。

#### UML 组件图：
组件图是一种特殊的UML图来描述系统的静态实现视图。组件图包括物理组件，如库，档案，文件夹等。

此图是用来从实施的角度。使用一个以上的元件图来表示整个系统。正向和逆向工程技术的使用，使可执行文件组件图。

#### UML 部署图：
组件图是用来描述一个系统的静态部署视图。这些图主要用于系统工程师。

部署图是由节点和它们之间的关系。一个高效的部署图是应用软件开发的一个组成部分。

#### UML 用例图:
用例图是从用户角度描述系统功能，并指出各功能的操作者，用来捕捉系统的动态性质。

一个高层次的设计用例图是用来捕捉系统的要求，因此它代表系统的功能和流向。虽然用例图的正向和反向工程是不是一个很好的选择，但他们仍然在一个稍微不同的方法来模拟它。

#### UML 交互图：
交互图，用于捕获系统的动态性质。

交互图包括序列图和协作图，其中：序列图显示对象之间的动态合作关系，它强调对象之间消息发送的顺序，同时显示对象之间的交互；协作图描述对象间的协作关系，协作图跟时序图相似，显示对象间的动态合作关系。

#### UML 状态图：
状态图是一个用于模拟系统的动态性质的五个图。这些图用来模拟一个对象的整个生命周期。

一个对象的状态被定义为对象所在的条件下，特定的时间和对象移动对其他状态，在某些事件发生时。状态图还用于正向和反向工程。

状态图着重描述从一个状态到另一个状态的流程，主要有外部事件的参与。

#### UML 活动图：
活动图是 UML 的动态模型的一种图形，一般用来描述相关用例图，活动图是一种特殊的状态图。
准确的活动图定义：活动图描述满足用例要求所要进行的活动以及活动间的约束关系，有利于识别并行活动。活动图是一种特殊的状态图，它对于系统的功能建模特别重要，强调对象间的控制流程