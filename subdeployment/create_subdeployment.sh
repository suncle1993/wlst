# 设置环境变量
export WL_HOME=/weblogic/wlserver_10.3

. $WL_HOME/server/bin/setWLSEnv.sh

# 执行WLST脚本
java weblogic.WLST create_subdeployment.py -p create_subdeployment.properties
