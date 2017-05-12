#!/usr/bin/env python 
#coding=utf-8
'''
Created on 5/12/17 09:37 AM
@author: Flowsnow
@file: create_queue.py 
@function: wlst创建队列
'''

import getopt
import sys
from java.io import FileInputStream


# 从create_jms_server.properties文件中加载properties
propInputStream = FileInputStream('create_queue.properties')
configProps = Properties()
configProps.load(propInputStream)

# 获取所有的properties
adminserver_username = configProps.get('adminserver_username')
adminserver_password = configProps.get('adminserver_password')
adminserver_ip = configProps.get('adminserver_ip')
adminserver_port = configProps.get('adminserver_port')

queue_name = configProps.get('queue_name')
queue_jndi_name = configProps.get('queue_jndi_name')
queue_subdeployment = configProps.get('queue_subdeployment')
queue_subdeployment_target_type = configProps.get('queue_subdeployment_target_type')
queue_subdeployment_target_name = configProps.get('queue_subdeployment_target_name')
queue_jms_module = configProps.get('queue_jms_module')

# 输出变量
print 'adminserver_username=', adminserver_username
print 'adminserver_password=', adminserver_password
print 'adminserver_ip=', adminserver_ip
print 'adminserver_port=', adminserver_port

print 'queue_name=', queue_name
print 'queue_jndi_name=', queue_jndi_name
print 'queue_subdeployment=', queue_subdeployment
print 'queue_subdeployment_target_type=', queue_subdeployment_target_type
print 'queue_subdeployment_target_name=', queue_subdeployment_target_name
print 'queue_jms_module=', queue_jms_module

# 连接管理节点
def connectToAdminserver():
    connect(adminserver_username, adminserver_password,'t3://' + adminserver_ip + ':' + str(adminserver_port) )

# 开启edit会话
def startTransaction():
    edit()
    startEdit()

# 关闭edit会话
def endTransaction():
    save()
    activate()

# 创建队列
def create_queue(name, jndi_name, subdeployment, target_type, target_name, module):
    cd('/JMSSystemResources')
    theJmsBean = cmo.lookupJMSSystemResource(module)
    if theJmsBean != None:
        jms_module_path = '/JMSSystemResources/' + module + '/JMSResource/' + module
        cd(jms_module_path)
        cmo.createQueue(name)
        cd('/JMSSystemResources/'+module+'/JMSResource/'+module+'/Queues/'+name)
        cmo.setJNDIName(jndi_name)
        cmo.setSubDeploymentName(subdeployment)
        # 设置队列使用的子部署所指向的目标
        s = 'com.bea:Name=' + target_name.strip() + ',Type=' + target_type
        try:
            cd('/SystemResources/'+module+'/SubDeployments/'+subdeployment)
            set('Targets',jarray.array([ObjectName(str(s))], ObjectName))
        except WLSTException:
            print '\033[1;35m[ERROR] 请检查' + target_name + '中的各个目标在管理节点的config.xml中是否存在 \033[0m'
            sys.exit()
try:
    connectToAdminserver()
    startTransaction()
    # starting to create queue
    create_queue(queue_name, queue_jndi_name, queue_subdeployment, queue_subdeployment_target_type, queue_subdeployment_target_name, queue_jms_module)
    endTransaction()
    disconnect()
    exit()
except:
    print '出现异常，执行回滚操作'
    undo(defaultAnswer='y', unactivatedChanges='true')
    stopEdit('y')
    print '回滚操作结束'
