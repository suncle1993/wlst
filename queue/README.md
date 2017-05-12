# create_queue脚本简介

这里的队列特指一般队列，即**非分布式队列**。创建队列之前需要创建好以下资源：

1. 指向weblogic server单节点的JMS模块
2. 指向JMSServer的子部署

即一切资源都需要非集群模式。

# create_queue脚本使用方法

## 修改create_queue.sh

此shell脚本是创建队列的入口脚本，里面主要是设置环境变量，启动WLST环境，然后调用创建队列的Jython脚本

```shell
export WL_HOME=/weblogic/wlserver_10.3
```

将以上两项修改为正确的路径。修改完成之后请确认$WL_HOME/server/bin/commEnv.sh中的JAVA_HOME是否已修改为实际的JAVA_HOME

## 修改create_queue.properties

create_queue.properties配置文件选项根据要创建的队列的实际情况修改。示例如下：

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

# queue：当前队列所在的JMS模块必须指向单个weblogic server
# 队列名称
queue_name=Queue-hahaha
# 队列JNDI名称
queue_jndi_name=Queue-hahaha
# 队列子部署
queue_subdeployment=subdeployment-hahaha
# 队列子部署的目标类型，子部署指向的类型必须是JMSServer
queue_subdeployment_target_type=JMSServer
# 队列子部署的目标名称
queue_subdeployment_target_name=JMSServer-0
# 队列所在的JMS模块名称
queue_jms_moduel=SystemModule-hahaha
```

一个队列指向一个JMSServer，因此此处的queue_subdeployment_target_name不允许有多个名称

## 执行create_queue.sh脚本

```shell
sh create_queue.sh
```