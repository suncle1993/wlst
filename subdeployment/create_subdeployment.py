#!/usr/bin/env python 
#coding=utf-8
'''
Created on 5/09/17 16:19 PM
@author: Flowsnow
@file: create_subdeployment.py 
@function: wlst创建子部署
'''

import getopt
import sys
from java.io import FileInputStream


# 从create_jms_server.properties文件中加载properties
propInputStream = FileInputStream('create_subdeployment.properties')
configProps = Properties()
configProps.load(propInputStream)

# 获取所有的properties
adminserver_username = configProps.get('adminserver_username')
adminserver_password = configProps.get('adminserver_password')
adminserver_ip = configProps.get('adminserver_ip')
adminserver_port = configProps.get('adminserver_port')

subdeployment_name = configProps.get('subdeployment_name')
subdeployment_target_type = configProps.get('subdeployment_target_type')
subdeployment_target_name = configProps.get('subdeployment_target_name')、
jms_module_name = configProps.get('jms_module_name')


# 输出变量
print 'adminserver_username=', adminserver_username
print 'adminserver_password=', adminserver_password
print 'adminserver_ip=', adminserver_ip
print 'adminserver_port=', adminserver_port

print 'subdeployment_name=', subdeployment_name
print 'subdeployment_target_type=', subdeployment_target_type
print 'subdeployment_target_name=', subdeployment_target_name
print 'jms_module_name=', jms_module_name


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

# 创建子部署
def create_subdeployment(name, target_type, target_name, module):
    cd('/SystemResources')
    theJmsBean = cmo.lookupJMSSystemResource(module)
    if theJmsBean != None:
        cd('/SystemResources/'+module)
        theSubDeploymentBean = cmo.lookupSubDeployment(name)
        if theSubDeploymentBean == None:
            cmo.createSubDeployment(name)
            targets = []
            for target in target_name.split(','):
                s = 'com.bea:Name=' + target.strip() + ',Type=' + target_type
                targets.append(ObjectName(str(s)))
            try:
                cd('/SystemResources/'+module+'/SubDeployments/'+name)
                set('Targets',jarray.array(targets, ObjectName))
            except WLSTException:
                print '\033[1;35m[ERROR] 请检查' + target_name + '中的各个目标在管理节点的config.xml中是否存在 \033[0m'
                sys.exit()
        else:
            print '子部署' + name + '已存在,请确认名称是否正确'
    else:
        print 'JMS模块' + module + '不存在，请先创建好jms模块'

try:
    connectToAdminserver()
    startTransaction()
    # starting to create subdeployment
    create_subdeployment(subdeployment_name, subdeployment_target_type, subdeployment_target_name, jms_module_name)
    endTransaction()
    disconnect()
    exit()
except:
    print '出现异常，执行回滚操作'
    undo(defaultAnswer='y', unactivatedChanges='true')
    stopEdit('y')
    print '回滚操作结束'
