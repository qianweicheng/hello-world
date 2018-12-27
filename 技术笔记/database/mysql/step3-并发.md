# 数据库并发
## 事务
四大特性：
1. 原子性（Atomicity）
2. 一致性（Consistency）
3. 隔离性（Isolation）
4. 持久性（Durability）
## 锁
锁的分类：
1. 独占锁，X锁。
    独占锁锁定的资源只允许进行锁定操作的程序使用，其它任何对它的操作均不会被接受。执行数据更新命令，即INSERT、UPDATE 或DELETE 命令时会自动使用独占锁。
    SELECT ... for update
2. 共享锁，s锁
    共享锁锁定的资源可以被其它用户读取，但其它用户不能修改它。在
    SELECT ... lock in share mode命令执行时，通常会对对象进行共享锁锁定。
3. 更新锁
InnoDB的锁：Shared Locks, Exclusive Locks, Record Locks, Gap Locks, Next-Key Locks

另外一种角度，锁分为以下两种类型：
- 悲观锁
- 乐观锁
> 锁加在哪里：数据库的锁是加在数据行对应的索引上的，
## 什么时候会加锁？
select: 即最常用的查询，是不加任何锁的
select ... lock in share mode: 会加共享锁(即Shared Lock)
select ... for update: 会加排它锁
insert、delete和update都是会加排它锁

## 并发问题:
1. 脏读：脏读是指在一个事务处理过程里读取了另一个未提交的事务中的数据。
2. 不可重复读：一个事务范围内多次查询却返回了不同的数据值，这是由于在查询间隔，被另一个事务修改并提交了
3. 虚读(幻读)
>幻读和不可重复读都是读取了另一条已经提交的事务（这点就脏读不同），所不同的是不可重复读查询的都是同一个数据项，而幻读针对的是一批数据整体（比如数据的个数）。

四种隔离级别：
1. Read uncommitted (读未提交)：最低级别，任何情况都无法保证。
    >所有写操作都会加排它锁， 该级别主要的特点是释放锁的时机与众不同：在执行完写操作后立即释放行锁，而不像其他隔离级别在事务提交以后释放
2. Read committed (读已提交)：可避免脏读的发生。
    - MVCC版本的生成时机: 是每次select时。在读已提交的级别下，每次select时都会通过MVCC获取当前数据的最新快照，也无视任何锁, 不加任何锁. 完美解决读写之间的并发问题，
    - 锁的范围：行锁。 和READ UNCOMMITTED的并发性能只差在写写操作上。而为了进一步提升写写操作上的并发性能，该级别下不会使用前文提到的间隙锁，无论什么查询都只会加行锁，而且在执行完WHERE条件筛选之后，会立即释放掉不符合条件的行锁，对于并发性能的追求可谓仁至义尽了。留下了不可重复读和幻读问题
3. Repeatable read (可重复读)：可避免脏读、不可重复读的发生。很多数据库都默认在这个级别，部分数据库默认在#2
    - MVCC版本的生成时间: 一次事务中只在第一次select时生成版本，后续的查询都是在这个版本上进行，从而实现了可重复读
    - 锁的范围：行锁或间隙锁
4. Serializable (串行化)：可避免脏读、不可重复读、幻读的发生。
    - 基于锁的Serializable的实现准则是：读要block写，写也要block读，读不block读。行锁或间隙锁. 
    - (MYSQL)跟#3的区别主要在，该级别下，会自动将所有普通select转化为select ... lock in share mode执行
    - (PostgreSQL)基于SSI实现
> 不同级别下，只有写操作释放锁的时机不同，而Locking Read的锁，不论什么级别，都是在事务结束后释放
## MVCC
MVCC是"Multi-Version Concurrency Control"的缩写
一般两种实现：
- B+树实现保留数据的一个或多个历史版本（PostgreSQL）
- 在需要时通过undo log构造出历史版本（Mysql）

每个数据记录携带两个额外的数据created_by_txn_id和deleted_by_txn_id。
- 当一个数据被insert时，created_by_txn_id记录下插入该数据的事务ID，deleted_by_txn_id留空。
- 当一个数据被delete时，该数据的deleted_by_txn_id记录执行该删除的事务ID。
- 当一个数据被update时，原有数据的deleted_by_txn_id记录执行该更新的事务ID，- 当新增一条新的数据记录，其created_by_txn_id记录下更新该数据的事务ID

MVCC工作原理:
- SELECT时，读取创建版本号<=当前事务版本号，删除版本号为空或>当前事务版本号。
- INSERT时，保存当前事务版本号为行的创建版本号
- DELETE时，保存当前事务版本号为行的删除版本号
- UPDATE时，插入一条新纪录，保存当前事务版本号为行创建版本号，同时保存当前事务版本号到原来删除的行

>MVCC只在 REPEATABLE READ和READ COMMITTED两种隔离级别下工作。而未提交读隔离级别总是读取最新的数据行，无需使用 MVCC

## 数据清除
在另一个事务进行读取时，由隔离级别来控制到底取哪个版本。同时，在读取过程中，完全不加锁（除非用SELECT … FOR UPDATE强行加锁）。这样可以极大降低数据读取时因为冲突被Block的机会。那么那些多出来的无用数据怎么被最终被清理呢？支持MVCC的数据库一般会有一个背景任务来定时清理那些肯定没用的数据。只要一个数据记录的deleted_by_txn_id不为空，并且比当前还没结束的事务ID中最小的一个还要小，该数据记录就可以被清理掉。在PostgreSQL中，这个背景任务叫做“VACUUM”进程；而在MySQL InnoDB中，叫做“purge“
## 写前提困境
尽管在MVCC的加持下Read Committed和Repeatable Read都可以得到很好的实现。但是对于某些业务代码来讲，在当前事务中看到/看不到其他的事务已经提交的修改的意义不是很大。这种业务代码一般是这样的：
1. 先读取一段现有的数据
2. 在这个数据的基础上做逻辑判断或者计算；
3. 将计算的结果写回数据库。
在修改的事务在提交时，无法确保这个修改的前提是否还可靠。这种问题我称之为写前提困境。
Repeatable Read 无法解决这个问题:

事务A|事务B
-|-
get counter (counter = 1)|
||get counter (counter = 1)
||counter = counter + 1 (counter = 2)
||set counter = 2
||commit
counter = counter + 1 (counter = 2)|
set counter = 2|
commit|

解决这类问题有3种办法：
- 数据库支持某种代码块，这个代码块的执行是排他的.(Actual Serial Execution)
    - 单线程数据库：Redis，VoltDB等
    - 用单SQL语句的事务。`UPDATE counter_tbl SET counter = counter + 1 where id = xxx;`
- 加悲观锁，把期望依赖的数据独占，在修改完成前不允许其他并发修改发生；
- 加乐观锁，在事务提交的一刹那（注意是commit时，不是修改时），检查修改的依赖是不是没有被修改；
    ```
    do{
        select counter as old_counter from counter_tbl where id = xxx;
        result = update counter_tbl set counter = counter + 1 where id = xxx and counter=old_counter;
        //忽略死循环情况
    } while(result != 1);
    ```
## SSI
Serialized Snopshot Isolation
个事务还是Snapshot Isolation，但事务在进行过程中，除了对数据进行操作外，还要对整个事务的“写前提”——所有修改操作的依赖数据做追踪。当事务被commit时，当前事务会检查这个“写前提”是否被其他事务修改过，如果是，则回滚掉当前事务。PostgreSQL的Serializable基于SSI实现。

## 参考文档
1. https://baike.baidu.com/item/%E9%AB%98%E6%80%A7%E8%83%BDMySQL/10913803?fr=aladdin
2. https://www.jianshu.com/p/eae001e603d6