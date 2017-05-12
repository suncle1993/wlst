# connection_factory脚本简介

WLST创建连接工厂时需要指定子部署和JNDI名称，而且连接工厂依赖于JMS模块，连接工厂的指向目标默认和JMS模块的目标一致。因此需要提前创建好JMS模块和子部署。

# connection_factory脚本使用方法

## 修改create_connection_factory.sh

此shell脚本是创建数据源的入口脚本，里面主要是设置环境变量，启动WLST环境，然后调用创建数据源的Jython脚本

```shell
export WL_HOME=/weblogic/wlserver_10.3
```

将以上两项修改为正确的路径。修改完成之后请确认$WL_HOME/server/bin/commEnv.sh中的JAVA_HOME是否已修改为实际的JAVA_HOME

## 修改create_connection_factory.properties

create_connection_factory.properties配置文件选项根据要创建的连接工厂的实际情况修改。示例如下：

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

# connection factory
# 连接工厂名称
connection_factory_name=ConnectionFactory-0
# 连接工厂JNDI名称
connection_factory_jndi_name=XjxtOuterGapFactory-0
# 连接工厂子部署
connection_factory_subdeployment=subdeployment-hahaha
# 连接工厂所在的JMS模块名称
connection_factory_jms_moduel=SystemModule-hahaha
```

其中，JMS模块名称和连接工厂子部署必须已经存在。

## 执行create_connection_factory.sh脚本

```shell
sh create_connection_factory.sh
```