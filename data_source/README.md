# data source脚本简介

WLST创建数据源（以Oracle数据源为例）总共有四种情况，按照下面两种分类来组合

- Oracle数据库单实例（Single Instance）或者RAC
- 数据源指向weblogic集群（Weblogic Cluster）或者单个节点（Weblogic Single Server）

此脚本已支持以上四种组合情况，使用方法如下

# data source脚本使用方法

## 修改create_data_source.sh

此shell脚本是创建数据源的入口脚本，里面主要是设置环境变量，启动WLST环境，然后调用创建数据源的Jython脚本

```shell
export WL_HOME=/weblogic/wlserver_10.3
```

将以上两项修改为正确的路径。修改完成之后请确认$WL_HOME/server/bin/commEnv.sh中的JAVA_HOME是否已修改为实际的JAVA_HOME

## 修改create_data_source.properties

此文件为创建数据源的配置文件，根据提示修改，其中重点注意数据库为单实例还是RAC，数据源的目标是weblogic集群的还是单节点的。

如果数据库为单实例的，则`datasource_url`修改为如下形式

```properties
# 数据源url
datasource_url=jdbc:oracle:thin:@10.199.129.74:1521:ltjsdb74
```

如果数据库为RAC的，则数据源url修改为如下形式

```properties
# 数据源url
datasource_url=jdbc:oracle:thin:@(DESCRIPTION =(ADDRESS_LIST =(ADDRESS = (PROTOCOL = TCP)(HOST =141.12.73.18 )(PORT = 1521))(ADDRESS = (PROTOCOL = TCP)(HOST =141.12.73.17 )(PORT = 1521))(LOAD_BALANCE = ON)(FAILOVER = ON))(CONNECT_DATA =(SERVICE_NAME = jslthxcx)(FAILOVER_METHOD =(TYPE = SESSION)(METHOD = BASIC))))
```

如果要创建的数据源的目标是weblogic单节点的，则修改`datasource_target_type`和`datasource_target_name`为如下形式

```properties
# 数据源目标类型
datasource_target_type=Server
# 数据源目标名称
datasource_target_name=gsdt01Server, gshx01Server
```

其中数据源的目标可以支持多个单节点，每个节点名称之间要用逗号隔开，请注意节点名称必须存在。

如果要创建的数据源的目标是weblogic集群的，则修改`datasource_target_type`和`datasource_target_name`为如下形式

```properties
# 数据源目标类型
datasource_target_type=Cluster
# 数据源目标名称
datasource_target_name=Cluster-gsdt, Cluster-gshx, Cluster-gsxj
```

其中数据源的目标可以支持多个集群，每个集群名称之间要用逗号隔开，请注意集群名称必须存在。

## 修改其他配置项

create_data_source.properties配置文件中的其他选项根据要创建的数据源的实际情况修改。示例如下：

```properties
# adminserver
# 管理服务器控控制台用户名
adminserver_username=weblogic
# 管理服务器控制台密码
adminserver_password=servyou2015
# 管理服务器ip
adminserver_ip=141.12.65.16
# 管理服务器端口
adminserver_port=9001

# datasource
# 数据源名称
datasource_name=hahaha
# JNDI名称
datasource_jndi_name=hahaha
# 数据源url
datasource_url=jdbc:oracle:thin:@(DESCRIPTION =(ADDRESS_LIST =(ADDRESS = (PROTOCOL = TCP)(HOST =141.12.73.18 )(PORT = 1521))(ADDRESS = (PROTOCOL = TCP)(HOST =141.12.73.17 )(PORT = 1521))(LOAD_BALANCE = ON)(FAILOVER = ON))(CONNECT_DATA =(SERVICE_NAME = jslthxcx)(FAILOVER_METHOD =(TYPE = SESSION)(METHOD = BASIC))))
# 数据源驱动名称
datasource_driver=oracle.jdbc.OracleDriver
# 数据源用户名
datasource_username=gs_cx
# 数据源密码
datasource_password=servyou2015
# 数据源目标类型
datasource_target_type=Cluster
# 数据源目标名称
datasource_target_name=gscx_cluster
# 数据源连接池最大容量
datasource_MaxCapacity=15
# 数据源连接池起始容量
datasource_InitialCapacity=5
# 数据源连接池每次递增容量
datasource_CapacityIncrement=5
```

## 执行create_data_source.sh脚本

```shell
sh create_data_source.sh
```