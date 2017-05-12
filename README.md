# wlst

此仓库用来存储所有常用的WLST脚本。所有脚本在weblogic11版本测试通过，下面按照不同的Resource分类。

如果自己试验脚本，请注意执行顺序，weblogic的各个JMS资源之间有不同的相互依赖。建议顺序：

jms module -> subdeployment -> connection_factory -> distributed_queue

data source和jms server与JMS资源之间没有相互依赖关系。而非集群的队列必须要找一个单节点的环境试验。因此都需要单独处理。

# data source

data_source文件夹中存储的是和数据源相关的WLST脚本，具体的使用见data_source/README.md

# jms server

jms_server文件夹中存储的是和jms服务器相关的WLST脚本，具体的使用见jms_server/README.md

# jms module

jms_module文件夹中存储的是和jms模块相关的WLST脚本，具体的使用见jms_module/README.md

# subdeployment

subdeployment文件夹中存储的是和子部署相关的WLST脚本，具体的使用见subdeployment/README.md

# connection_factory

connection_factory文件夹中存储的是和连接工厂相关的WLST脚本，具体的使用见connection_factory/README.md

# queue

queue文件夹中存储的是和队列相关的WLST脚本，具体的使用见queue/README.md

# distributed_queue

distributed_queue文件夹中存储的是和分布式队列相关的WLST脚本，具体的使用见distributed_queue/README.md

# 注意事项

## commEnv.sh修改JAVA_HOME

在$WL_HOME/server/bin/commEnv.sh脚本中的149行左右的内容

```shell
# Reset JAVA_HOME, JAVA_VENDOR and PRODUCTION_MODE unless JAVA_HOME
# and JAVA_VENDOR are pre-defined.
if [ -z "${JAVA_HOME}" -o -z "${JAVA_VENDOR}" ]; then
   # Set up JAVA HOME
   JAVA_HOME="/usr/lib/jvm/java-1.6.0-openjdk-1.6.0.0.x86_64"
   # Set up JAVA VENDOR, possible values are
   #Oracle, HP, IBM, Sun ...
   JAVA_VENDOR=Sun
   # PRODUCTION_MODE, default to the development mode
   PRODUCTION_MODE=""
 fi
```

需要修改JAVA_HOME为实际的JAVA_HOME路径，比如：

```shell
JAVA_HOME="/weblogic/java/jdk1.6.0_45"
```

此处修改不影响weblogic其他的使用。

---

参考资料：

- [个人**重点推荐**的WLST **MBean机制**入门教程](http://www.beansoft.biz/weblogic/docs92/config_scripting/nav_edit.html)


- [WebLogic Server 管理任务自动化](http://www.beansoft.biz/weblogic/docs92/config_scripting/config_WLS.html#wp1004872)


- [Create a Data Source Using WebLogic Scripting Tool (WLST)](https://oracle-base.com/articles/web/wlst-create-data-source#properties)


- [Create distributed JMS destinations Tips](http://www.dba-oracle.com/t_weblogic_create_distributed_jms_destinations.htm)
- [JMS module using WLST](http://wlstbyexamples.blogspot.com/2013/01/this-post-is-continous-series-of-jms.html#.WRVipmJ97Dc)
- [WebLogic Scripting Tool (WLST) Overview](http://wlstbyexamples.blogspot.jp/2010/05/weblogic-server-weblogic-scripting-tool.html#.WRVodWJ97Dd)