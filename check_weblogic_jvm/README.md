# check_weblogic_jvm脚本简介

WLST 联机版脚本check_weblogic_jvm为域中正在运行的所有服务器监视 `JVMHeapSize`；如果JVM堆大小大于指定的阈值，则打印警告。此脚本可以用于nagios监控weblogic时的执行脚本

**参数如下**

```python
# 管理服务器控控制台用户名
adminserver_username = 'weblogic'
# 管理服务器控制台密码
adminserver_password = 'servyou2017'
# 管理服务器ip
adminserver_ip = '10.199.129.73'
# 管理服务器端口
adminserver_port = 7600

# jvm报警百分比 
jvm_warning_percent = 70
```

脚本中的这五项参数修改完成之后就可以按照下面的方法执行

```shell
java weblogic.WLST check_weblogic_jvm.py
```

前提需要先设置好WLST执行环境，可以参见根目录的README

