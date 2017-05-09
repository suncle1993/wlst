# jms_server脚本简介

WLST创建jms服务器时需要指向weblogic server，weblogic server分为Server和MigratableTarget两种类型，目前环境中指向的都是可迁移的weblogic server。

# jms_server脚本使用方法

## 修改create_jms_server.sh

此shell脚本是创建数据源的入口脚本，里面主要是设置环境变量，启动WLST环境，然后调用创建数据源的Jython脚本

```shell
export WL_HOME=/weblogic/wlserver_10.3
```

将以上两项修改为正确的路径。修改完成之后请确认$WL_HOME/server/bin/commEnv.sh中的JAVA_HOME是否已修改为实际的JAVA_HOME

## 修改create_jms_server.properties

create_jms_server.properties配置文件选项根据要创建的jms服务器的实际情况修改。示例如下：

```properties
# adminserver
# 管理服务器控控制台用户名
adminserver_username=weblogic
# 管理服务器控制台密码
adminserver_password=servyou2017
# 管理服务器ip
adminserver_ip=10.199.129.73
# 管理服务器端口
adminserver_port=7600

# jmsserver
# jms服务器名称
jms_server_name=JMSServer-hahaha
# 为jms服务器的指定的持久性存储的名称
jms_server_file_store=FileStore-cgjs01
# jms服务器的目标服务器类型
jms_server_target_type=MigratableTarget
# jms服务器的目标服务器名称
jms_server_target_name=gscgjs01_Server (migratable)
```

**当jms服务器的目标服务器类型为可迁移时，jms_server_target_type必须为MigratableTarget**

## 执行create_jms_server.sh脚本

```shell
sh create_jms_server.sh
```