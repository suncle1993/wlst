# subdeployment脚本简介

WLST创建子部署时需要指向Weblogic Cluster或者Weblogic Server或者JMSServer，此脚本已支持所有类型，目前生产环境中全部是指向Cluster。脚本使用的前提是必须创建好JMS模块。

# subdeployment脚本使用方法

## 修改create_subdeployment.sh

此shell脚本是创建数据源的入口脚本，里面主要是设置环境变量，启动WLST环境，然后调用创建数据源的Jython脚本

```shell
export WL_HOME=/weblogic/wlserver_10.3
```

将以上两项修改为正确的路径。修改完成之后请确认$WL_HOME/server/bin/commEnv.sh中的JAVA_HOME是否已修改为实际的JAVA_HOME

## 修改create_subdeployment.properties

create_subdeployment.properties配置文件选项根据要创建的子部署的实际情况修改。示例如下：

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

# subdeployment
# 子部署名称
subdeployment_name=subdeployment-hahaha
# 子部署目标类型，支持Server，Cluster，JMSServer，生产环境全部使用Cluster
subdeployment_target_type=Cluster
# 子部署目标名称
subdeployment_target_name=Cluster_cgjs
# jms模块名称
jms_module_name=SystemModule-hahaha
```

如果此子部署指向Weblogic Cluster，则需要修改subdeployment_target_type和subdeployment_target_name两个参数如下：

```properties
# jms模块的目标类型
subdeployment_target_type=Cluster
# jms模块的目标名称
subdeployment_target_name=Cluster_cgjs
```

**子部署的目标已支持多个集群的模式，需要在subdeployment_target_name后面用逗号隔开多个集群名称**

如果此子部署指向Weblogic Server，则需要修改subdeployment_target_type和subdeployment_target_name两个参数如下：

```properties
# 子部署的目标类型
subdeployment_target_type=Server
# 子部署的目标名称
subdeployment_target_name=gscgjs01_Server
```

**子部署的目标已支持多个Server的模式，需要在subdeployment_target_name后面用逗号隔开多个Server名称**

如果此子部署指向JMSServer，则需要修改subdeployment_target_type和subdeployment_target_name两个参数如下：

```properties
# 子部署的目标类型
subdeployment_target_type=JMSServer
# 子部署的目标名称
subdeployment_target_name=JMSServer-cgjs01
```

**子部署的目标已支持多个JMSServer的模式，需要在subdeployment_target_name后面用逗号隔开多个JMSServer名称**

## 执行create_subdeployment.sh脚本

```shell
sh create_jms_module.sh
```