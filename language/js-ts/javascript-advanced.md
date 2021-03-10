# JS
js单线程消息队列模式
## 消息队列
任务队列又分为macro-task（宏任务)与 micro-task（微任务）
### macro-task大概包括：
script(整体代码), setTimeout, setInterval, setImmediate, I/O, UI rendering。
### 微任务
micro-task大概包括: process.nextTick, Promise
### 运行调度机制
1. 执行一个宏任务（栈中没有就从事件队列中获取）
2. 执行过程中如果遇到微任务，就将它添加到微任务的任务队列中
3. 宏任务执行完毕后，立即执行当前微任务队列中的所有微任务（依次执行）
4. 当前宏任务执行完毕，开始检查渲染，然后GUI线程接管渲染
5. 渲染完毕后，JS引擎线程继续，开始下一个宏任务（从宏任务队列中获取）
