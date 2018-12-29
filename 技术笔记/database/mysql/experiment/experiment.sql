-- 通过Group ID搜索User, group_user
EXPLAIN SELECT t_user.* FROM t_user WHERE t_user.id IN (SELECT t_group_user.user_id  FROM t_group_user WHERE t_group_user.group_id=1);
EXPLAIN SELECT t_user.* FROM t_user LEFT JOIN t_group_user ON t_group_user.user_id=t_user.id  WHERE t_group_user.group_id=1;

-- 通过Group ID搜索User, group_user2
EXPLAIN SELECT t_user.* FROM t_user WHERE t_user.id IN (SELECT t_group_user2.user_id  FROM t_group_user2 WHERE t_group_user2.group_id=1);
EXPLAIN SELECT t_user.* FROM t_user LEFT JOIN t_group_user2 ON t_group_user2.user_id=t_user.id  WHERE t_group_user2.group_id=1;
EXPLAIN SELECT t_user.* FROM t_group_user2 LEFT JOIN t_user ON t_group_user2.user_id=t_user.id  WHERE t_group_user2.group_id=1;

-- 通过User ID搜索Group, group_user
EXPLAIN SELECT t_group.* FROM t_group WHERE t_group.id IN (SELECT t_group_user.group_id  FROM t_group_user WHERE t_group_user.user_id=1);
EXPLAIN SELECT t_group.* FROM t_group LEFT JOIN t_group_user ON t_group_user.group_id=t_group.id  WHERE t_group_user.user_id=1;
EXPLAIN SELECT t_group.* FROM t_group_user LEFT JOIN t_group ON t_group_user.group_id=t_group.id  WHERE t_group_user.user_id=1;

-- 通过User ID搜索Group, group_user2
 SELECT t_group.* FROM t_group WHERE t_group.id IN (SELECT t_group_user2.group_id  FROM t_group_user2 WHERE t_group_user2.user_id=1);
EXPLAIN SELECT t_group.* FROM t_group LEFT JOIN t_group_user2 ON t_group_user2.group_id=t_group.id  WHERE t_group_user2.user_id=1;
EXPLAIN SELECT t_group.* FROM t_group_user2 LEFT JOIN t_group ON t_group_user2.group_id=t_group.id  WHERE t_group_user2.user_id=1;
 
--  覆盖索引测试
EXPLAIN SELECT t_group_user.group_id, t_group_user.user_id  FROM t_group_user WHERE t_group_user.group_id=1;
EXPLAIN SELECT t_group_user2.group_id, t_group_user2.user_id  FROM t_group_user2 WHERE t_group_user2.group_id=1;

-- Exists,IN,JOIN
-- 查询
 SELECT COUNT(*) FROM t_user WHERE EXISTS (SELECT 1 FROM t_group_user WHERE t_user.id=t_group_user.user_id );
 SELECT COUNT(*) FROM t_user WHERE EXISTS (SELECT 1 FROM t_group_user WHERE t_group_user.group_id = 1);
 SELECT COUNT(*) FROM t_user WHERE id NOT IN (SELECT user_id FROM t_group_user WHERE t_group_user.group_id=1);
 SELECT t_user.* FROM t_user JOIN t_group_user ON  t_user.id=t_group_user.user_id WHERE t_group_user.group_id=1;

-- 查找部门底下有>N个人的所有组
-- 为啥使用t_group_name索引?
 SELECT t1.id, t1.name FROM t_group as t1 WHERE t1.id IN (SELECT t2.group_id FROM t_group_user   as t2 GROUP BY t2.group_id HAVING count(t2.group_id)>0);
 SELECT t1.id, t1.name FROM t_group as t1 WHERE t1.id IN (SELECT t2.group_id FROM t_group_user2 as t2 GROUP BY t2.group_id HAVING count(t2.group_id)>0);
 SELECT t2.group_id,t1.name FROM t_group as t1 JOIN t_group_user2 as t2 ON t1.id = t2.group_id group by t2.group_id,t1.name HAVING COUNT(t2.group_id)>0;
 -- 0.05122800
 -- 0.05483700
 -- 0.01241200