#!/usr/bin/env python 
#coding=utf-8
'''
Created on 5/12/17 09:37 AM
@author: Flowsnow
@file: create_distributed_queue.py 
@function: wlst创建队列和分布式队列
'''

import getopt
import sys
from java.io import FileInputStream


# 从create_jms_server.properties文件中加载properties
propInputStream = FileInputStream('create_distributed_queue.properties')
configProps = Properties()
configProps.load(propInputStream)

# 获取所有的properties
adminserver_username = configProps.get('adminserver_username')
adminserver_password = configProps.get('adminserver_password')
adminserver_ip = configProps.get('adminserver_ip')
adminserver_port = configProps.get('adminserver_port')

distributed_queue_name = configProps.get('distributed_queue_name')
distributed_queue_jndi_name = configProps.get('distributed_queue_jndi_name')
distributed_queue_subdeployment = configProps.get('distributed_queue_subdeployment')
distributed_queue_jms_module = configProps.get('distributed_queue_jms_module')

# 输出变量
print 'adminserver_username=', adminserver_username
print 'adminserver_password=', adminserver_password
print 'adminserver_ip=', adminserver_ip
print 'adminserver_port=', adminserver_port

print 'distributed_queue_name=', distributed_queue_name
print 'distributed_queue_jndi_name=', distributed_queue_jndi_name
print 'distributed_queue_subdeployment=', distributed_queue_subdeployment
print 'distributed_queue_jms_module=', distributed_queue_jms_module

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

# 创建分布式队列
def create_distributed_queue(name, jndi_name, subdeployment, module):
    cd('/JMSSystemResources')
    theJmsBean = cmo.lookupJMSSystemResource(module)
    if theJmsBean != None:
        jms_module_path = '/JMSSystemResources/' + module + '/JMSResource/' + module
        cd(jms_module_path)
        theUniformDistributedQueueBean = cmo.lookupUniformDistributedQueue(name)
        if theUniformDistributedQueueBean == None:
            cmo.createUniformDistributedQueue(name)
            cd('/JMSSystemResources/'+module+'/JMSResource/'+module+'/UniformDistributedQueues/'+name)
            cmo.setJNDIName(jndi_name)
            cmo.setSubDeploymentName(subdeployment)
        else:
            print '分布式队列' + name + '已存在，请确认是否正确'
    else:
        print 'JMS模块' + module + '不存在，请先创建好jms模块'

try:
    connectToAdminserver()
    startTransaction()
    # starting to create UniformDistributedQueues
    create_distributed_queue(distributed_queue_name, distributed_queue_jndi_name, distributed_queue_subdeployment, distributed_queue_jms_module)
    endTransaction()
    disconnect()
    exit()
except:
    print '出现异常，执行回滚操作'
    undo(defaultAnswer='y', unactivatedChanges='true')
    stopEdit('y')
    print '回滚操作结束'
