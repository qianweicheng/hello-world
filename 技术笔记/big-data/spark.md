#### 总述
从任务的角度来看分成：
驱动器节点：负责一个做也内部计算的调度
执行器节点：
从集群的角度来看分成：
* 主节点，负责各个作业的调度
* 工作节点

#### pycharm
依赖两个环境变量：PYSPARK_PYTHON=python
依赖两个环境变量：SPARK_HOME

#### Transformations
    map
    filter
    flatMap
    mapPartitions
    mapPartitionsithIndex
    sample
    union
    intersection
    distinct
    groupByKey
    reduceByKey
    aggregateByKey
    sortByKey
    cogroup
    cartesian
    pipe
    coalesce
    repartition
    repartitionAndSortWithinPartitions

#### Actions
    reduce
    collect
    count
    first
    taken
    takeSample
    takeOrdered
    saveAsTextFile
    countByKey
    foreach

#### Spark SQL
|Property Name | Meaning|
|-|-|
|url|路径|
|dbtable||
|driver|The class name of the JDBC driver to use to connect to this URL.|
|partitionColumn,lowerBound,upperBound|三者必须同时|
|numPartitions||
|fetchsize||
|batchsize||
|isolatitionLevel||
|sessionInitStatement||
|truncate||
|createTableOptions||
|createTableColumnTypes||
|customSchema||


