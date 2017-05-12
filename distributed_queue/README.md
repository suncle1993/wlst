# distributed_queue脚本简介

这里的队列特指**分布式队列**。创建队列之前需要创建好以下资源：

1. 指向Cluster的JMS模块
2. 指向Cluster的子部署

即一切资源应该是集群模式。

# distributed_queue脚本使用方法

## 修改create_distributed_queue.sh

此shell脚本是创建分布式队列的入口脚本，里面主要是设置环境变量，启动WLST环境，然后调用创建分布式队列的Jython脚本

```shell
export WL_HOME=/weblogic/wlserver_10.3
```

将以上两项修改为正确的路径。修改完成之后请确认$WL_HOME/server/bin/commEnv.sh中的JAVA_HOME是否已修改为实际的JAVA_HOME

## 修改create_distributed_queue.properties

create_distributed_queue.properties配置文件选项根据要创建的分布式队列的实际情况修改。示例如下：

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

# queue：当前队列所在的JMS模块必须是单节点的
# 分布式队列名称
distributed_queue_name=Queue-hahaha
# 分布式队列JNDI名称
distributed_queue_jndi_name=Queue-hahaha
# 分布式队列子部署：必须已经存在，子部署的目标和类型在创建的时候已经制定，此处不需要再指定
distributed_queue_subdeployment=subdeployment-hahaha
# 分布式队列所在的JMS模块名称
distributed_queue_jms_module=SystemModule-hahaha
```

其中，JMS模块名称和子部署必须已经存在。

## 执行create_distributed_queue.sh脚本

```shell
sh create_distributed_queue.sh
```