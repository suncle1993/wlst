# 设置环境变量
export WL_HOME=/weblogic/wlserver_10.3
export JAVA_HOME=/weblogic/java/jdk1.6.0_45
export PATH=$JAVA_HOME/bin:$PATH

. $WL_HOME/server/bin/setWLSEnv.sh

# 执行WLST脚本
java weblogic.WLST create_data_source.py -p myDomain-ds.properties
