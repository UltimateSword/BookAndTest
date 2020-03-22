# sql注入
SQL注入是一种注入攻击,可以执行恶意SQL语句
sql 注入主要是由于sql拼接导致的漏洞.例如

`"select * from users where name = '" + userName + "'";`

将userName设为 `' or '1'='1` 可拼接成 `select * from users where name = '' or '1'='1'`

## 其他规则
mysql注释符 `/* */` `"--  ..."` `#..`
union join等方式也可导致注入

# sqlmap 盲注工具
安装sqlmap略

`python sqlmap.py -u 'http://10.12.25.110:8001/WebGoat/SqlInjection/attack6a' --cookie="JSESSIONID=458C562290DE59252F280FB00D209FBE --method="post"` 