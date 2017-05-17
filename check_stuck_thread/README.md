# check_stuck_thread脚本简介

此次thread相关信息是通过ApplicationRuntimesMBean获取，ThreadPoolRuntimeMBean中提供的信息里面和阻塞的线程没有太多关系。脚本中提供的方法包含集群和单节点两种模式，需要自己在脚本中选择。

**选择方法**

```python
# 第一种方式：监控指定server
server_name = 'gscgjs01_Server'
monitor_stuck_thread_of_server(server_name)

# 第二种方式：监控cluster里面的所有server
# monitor_stuck_thread_of_cluster()

disconnect()
```

脚本中想使用哪种方式就注释另外一种方式。

**参数介绍**

```python
# 管理服务器控控制台用户名
adminserver_username = 'weblogic'
# 管理服务器控制台密码
adminserver_password = 'servyou2017'
# 管理服务器ip
adminserver_ip = '10.199.129.73'
# 管理服务器端口
adminserver_port = 7600

# 阻塞线程上限，超出此上限报警
stuck_thread_limit = 5
```

脚本中的这五项参数修改完成之后就可以按照下面的方法执行

```shell
java weblogic.WLST check_weblogic_jvm.py
```

前提需要先设置好WLST执行环境，可以参见根目录的README

---

参考

- [Exporting the stuck thread count from WebLogic](https://www.qualogy.com/techblog/oracle/exporting-the-stuck-thread-count-from-weblogic)
- [Servers: Monitoring: Threads](https://docs.oracle.com/middleware/1212/wls/WLACH/pagehelp/Corecoreserverservermonitorthreadstitle.html)