#!/usr/bin/env python 
#coding=utf-8
'''
Created on 5/08/17 15:36 PM
@author: Flowsnow
@file: create_jms_server.py 
@function: wlst创建JMS服务器
'''

import getopt
import sys
from java.io import FileInputStream


# 从create_jms_server.properties文件中加载properties
propInputStream = FileInputStream('create_jms_server.properties')
configProps = Properties()
configProps.load(propInputStream)

# 获取所有的properties
adminserver_username = configProps.get('adminserver_username')
adminserver_password = configProps.get('adminserver_password')
adminserver_ip = configProps.get('adminserver_ip')
adminserver_port = configProps.get('adminserver_port')

jms_server_name = configProps.get('jms_server_name')
jms_server_file_store = configProps.get('jms_server_file_store')
jms_server_target_type = configProps.get('jms_server_target_type')
jms_server_target_name = configProps.get('jms_server_target_name')


# 输出变量
print 'adminserver_username=', adminserver_username
print 'adminserver_password=', adminserver_password
print 'adminserver_ip=', adminserver_ip
print 'adminserver_port=', adminserver_port

print 'jms_server_name=', jms_server_name
print 'jms_server_file_store=', jms_server_file_store
print 'jms_server_target_type=', jms_server_target_type
print 'jms_server_target_name=', jms_server_target_name


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

# 创建jms服务器
def create_jms_server(name, file_stone, target_type, target_name):
    try:
        print '[INFO] creating mbean of type JMSServer ... '
        theBean = cmo.lookupJMSServer(name)
        if theBean == None:
            cmo.createJMSServer(name)
            cd('/Deployments/'+name)
            cmo.setPersistentStore(getMBean('/FileStores/'+file_stone))
            set('Targets',jarray.array([ObjectName('com.bea:Name='+str(target_name)+',Type=MigratableTarget')], ObjectName))
    except WLSTException:
        pass

try:
    connectToAdminserver()
    startTransaction()
    # starting to create JMSServer
    create_jms_server(jms_server_name, jms_server_file_store, jms_server_target_type ,jms_server_target_name)
    endTransaction()
    disconnect()
    exit()
except:
    print '出现异常，执行回滚操作'
    undo(defaultAnswer='y', unactivatedChanges='true')
    stopEdit('y')
    print '回滚操作结束'
