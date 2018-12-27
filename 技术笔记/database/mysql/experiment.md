# 实验课
## 实验目的：通过EXPLAIN检查索引设置效果和查询性能
## 准备工作:
```
CREATE TABLE `t_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name`    varchar(45) NOT NULL,
  `desc`    varchar(45),
  PRIMARY KEY (`id`),
  KEY `t_group_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name`    varchar(45) NOT NULL,
  `email`   varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `t_user_name` (`name`),
  UNIQUE KEY `t_user_email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_group_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rold`    varchar(45),
  PRIMARY KEY (`id`),
  KEY `t_group_user_group_id` (`group_id`),
  KEY `t_group_user_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_group_user2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rold`    varchar(45),
  PRIMARY KEY (`id`),
  KEY `t_group_user_multi_idx` (`group_id`,`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
## 查询分析
业务|SQL实现|分析
-|-|-
查询所有group|SELECT * FROM t_group|全表扫描
根据主键id查询|SELECT * FROM t_group WHERE id =1;|利用主键，常数时间
查询最大ID|SELECT MAX(id) FROM t_user;|B-Tree最右边节点
查询明显不存在的|SELECT * FROM t_user WHERE id=-1|提前终止
查询特定Group中所有Usser|SELECT t_user.* FROM t_user

## 案例 Group<->User
Case|SQL|备注
:-:|-|-
查询User(t_group_user,子查询)|EXPLAIN SELECT t_user.* FROM t_user WHERE t_user.id IN (SELECT t_group_user.user_id  FROM t_group_user WHERE t_group_user.group_id=1);
查询User(t_group_user,join)|EXPLAIN SELECT t_user.* FROM t_user LEFT JOIN t_group_user ON t_group_user.user_id=t_user.id  WHERE t_group_user.group_id=1;
查询User(t_group_user2,子查询)|EXPLAIN SELECT t_user.* FROM t_user WHERE t_user.id IN (SELECT t_group_user2.user_id  FROM t_group_user2 WHERE t_group_user2.group_id=1);
查询User(t_group_user,join)|EXPLAIN SELECT t_user.* FROM t_user LEFT JOIN t_group_user2 ON t_group_user2.user_id=t_user.id  WHERE t_group_user2.group_id=1;
查询Group(t_group_user,子查询)|SELECT t_group.* FROM t_group WHERE t_group.id IN (SELECT t_group_user.group_id  FROM t_group_user WHERE t_group_user.user_id=1);
查询Group(t_group_user,join)|SELECT t_group.* FROM t_group LEFT JOIN t_group_user ON t_group_user.group_id=t_group.id  WHERE t_group_user.user_id=1;
查询Group(t_group_user2,子查询)|EXPLAIN SELECT t_group.* FROM t_group WHERE t_group.id IN (SELECT t_group_user2.group_id  FROM t_group_user2 WHERE t_group_user2.user_id=1);|全表扫描
查询Group(t_group_user2,join)|EXPLAIN SELECT t_group.* FROM t_group LEFT JOIN t_group_user2 ON t_group_user2.group_id=t_group.id  WHERE t_group_user2.user_id=1;|全表扫描