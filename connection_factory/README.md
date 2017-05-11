# connection_factory脚本简介



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
11
```

## 执行create_connection_factory.sh脚本

```shell
sh create_connection_factory.sh
```