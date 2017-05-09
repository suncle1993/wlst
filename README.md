# wlst

此仓库用来存储所有常用的WLST脚本。所有脚本在weblogic11版本测试通过，下面按照不同的Resource分类

# data source

data_source文件夹中存储的是和数据源相关的WLST脚本，具体的使用见data_source/README.md

# jms server

jms_server文件夹中存储的是和jms服务器相关的WLST脚本，具体的使用见jms_server/README.md

# jms module

jms_module文件夹中存储的是和jms模块相关的WLST脚本，具体的使用见jms_module/README.md

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

每完成一个部分就补充一个部分