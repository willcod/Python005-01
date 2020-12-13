* 修改字符集的配置项、验证字符集的 SQL 语句
```sql
    * ALTER DATABASE [database-name] CHARACTER SET [charset-name] COLLATE [collation-name];
```

* 增加远程用户的 SQL 语句
```sql
mysql> CREATE USER 'remoteUser'@'%' IDENTIFIED BY '123456';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'remoteUser'@'%';
mysql> FLUSH PRIVILEGES;
```
* 为以下 sql 语句标注执行顺序：

```sql
[5] SELECT DISTINCT player_id, player_name, count(*) as num 
[1] FROM player JOIN team ON player.team_id = team.team_id 
[2] WHERE height > 1.80 
[3] GROUP BY player.team_id 
[4] HAVING num > 2 
[6] ORDER BY num DESC 
[7] LIMIT 2
```


* inner join
``` sql
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;
```
得到两个表同时满足条件Table1.id = Table2.id的记录。

* left join
``` sql
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id;
```
得到两个表同时满足条件Table1.id = Table2.id的记录，外加不满足条件的Table1中的记录，那些不满足条件的记录中的name为null

* right join
``` sql
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id;
```
得到两个表同时满足条件Table1.id = Table2.id的记录，外加不满足条件的Table2中的记录，那些不满足条件的记录中的name为null


<br>

* 索引

MySQL内部使用了B树来建立索引。
增加索引不一定会提高查询速度。

使用索引的场景有：

* 主键自动建立唯一索引
* 经常作为查询条件在WHERE或者ORDER BY 语句中出现的列要建立索引
* 作为排序的列要建立索引
* 查询中与其他表关联的字段，外键关系建立索引
* 高并发条件下倾向组合索引
* 用于聚合函数的列可以建立索引，例如使用了max(column_1)或者count(column_1)时的column_1就需要建立索引

避免建立索引的场景有：

* 经常增删改的列不要建立索引
* 有大量重复的列不建立索引
* 表记录太少不要建立索引


