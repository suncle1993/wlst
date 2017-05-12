#!/usr/bin/env python 
#coding=utf-8
'''
Created on 5/11/17 16:55 PM
@author: Flowsnow
@file: create_connection_factory.py 
@function: wlst创建连接工厂
'''

import getopt
import sys
from java.io import FileInputStream


# 从create_jms_server.properties文件中加载properties
propInputStream = FileInputStream('create_connection_factory.properties')
configProps = Properties()
configProps.load(propInputStream)

# 获取所有的properties
adminserver_username = configProps.get('adminserver_username')
adminserver_password = configProps.get('adminserver_password')
adminserver_ip = configProps.get('adminserver_ip')
adminserver_port = configProps.get('adminserver_port')

connection_factory_name = configProps.get('connection_factory_name')
connection_factory_jndi_name = configProps.get('connection_factory_jndi_name')
connection_factory_subdeployment = configProps.get('connection_factory_subdeployment')
connection_factory_jms_module = configProps.get('connection_factory_jms_module')

# 输出变量
print 'adminserver_username=', adminserver_username
print 'adminserver_password=', adminserver_password
print 'adminserver_ip=', adminserver_ip
print 'adminserver_port=', adminserver_port

print 'connection_factory_name=', connection_factory_name
print 'connection_factory_jndi_name=', connection_factory_jndi_name
print 'connection_factory_subdeployment=', connection_factory_subdeployment
print 'connection_factory_jms_module=', connection_factory_jms_module

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

# 创建连接工厂：连接工厂默认指向当前JMS模块的目标
def create_connection_factory(name, jndi_name, subdeployment, module):
    cd('/JMSSystemResources')
    theJmsBean = cmo.lookupJMSSystemResource(module)
    if theJmsBean != None:
        jms_module_path = '/JMSSystemResources/' + module + '/JMSResource/' + module
        cd(jms_module_path)
        theConnectionFactoryBean = cmo.lookupConnectionFactory(name)
        if theConnectionFactoryBean == None:
            cmo.createConnectionFactory(name)
            cd(jms_module_path + '/ConnectionFactories/' + name)
            cmo.setJNDIName(jndi_name)
            # 为连接工厂指定子部署
            cmo.setSubDeploymentName(subdeployment)
            # JMS 连接工厂的安全配置参数，用于指定 WebLogic Server 是否将已通过验证的用户名附加到发送的消息中
            cd(jms_module_path + '/ConnectionFactories/' + name + '/SecurityParams/' + name)
            cmo.setAttachJMSXUserId(false)  # false表示不发送
        else:
            print '连接工厂' + name + '已存在，请确认是否正确'
    else:
        print 'JMS模块' + module + '不存在，请先创建好jms模块'

try:
    connectToAdminserver()
    startTransaction()
    # starting to create connection factory
    create_connection_factory(connection_factory_name, connection_factory_jndi_name, connection_factory_subdeployment, connection_factory_jms_module)
    endTransaction()
    disconnect()
    exit()
except:
    print '出现异常，执行回滚操作'
    undo(defaultAnswer='y', unactivatedChanges='true')
    stopEdit('y')
    print '回滚操作结束'
