#!/usr/bin/env python 
#coding=utf-8
'''
Created on 5/04/17 16:13 PM
@author: Flowsnow
@file: create_data_source.py 
@function: wlst创建数据源指向集群
'''

import getopt
import sys
from java.io import FileInputStream


# 从create_data_source.properties文件中加载properties
propInputStream = FileInputStream('create_data_source.properties')
configProps = Properties()
configProps.load(propInputStream)

# 获取所有的properties
adminserver_username = configProps.get('adminserver_username')
adminserver_password = configProps.get('adminserver_password')
adminserver_ip = configProps.get('adminserver_ip')
adminserver_port = configProps.get('adminserver_port')
datasource_name = configProps.get('datasource_name')
datasource_jndi_name = configProps.get('datasource_jndi_name')
datasource_url = configProps.get('datasource_url')
datasource_driver = configProps.get('datasource_driver')
datasource_username = configProps.get('datasource_username')
datasource_password = configProps.get('datasource_password')
datasource_target_type = configProps.get('datasource_target_type')
datasource_target_name = configProps.get('datasource_target_name')
datasource_MaxCapacity = configProps.get('datasource_MaxCapacity')
datasource_InitialCapacity = configProps.get('datasource_InitialCapacity')
datasource_CapacityIncrement = configProps.get('datasource_CapacityIncrement')

# 输出变量
print 'adminserver_username=', adminserver_username
print 'adminserver_password=', adminserver_password
print 'adminserver_ip=', adminserver_ip
print 'adminserver_port=', adminserver_port
print 'datasource_name=', datasource_name
print 'datasource_jndi_name=', datasource_jndi_name
print 'datasource_url=', datasource_url
print 'datasource_driver=', datasource_driver
print 'datasource_username=', datasource_username
print 'datasource_password=', datasource_password
print 'datasource_target_type=', datasource_target_type
print 'datasource_target_name=', datasource_target_name
print 'datasource_MaxCapacity=', datasource_MaxCapacity
print 'datasource_InitialCapacity=', datasource_InitialCapacity
print 'datasource_CapacityIncrement=', datasource_CapacityIncrement


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
    try:
        activate()
    except weblogic.common.resourcepool.ResourceSystemException:
        print '\033[1;35m[ERROR] 请检查数据源的url，用户名，密码是否正确 \033[0m'

# 创建JDBC系统资源
def create_JDBCSystemResource(path, beanName):
      cd(path)
      try:
            print '[INFO] creating mbean of type JDBCSystemResource ... '
            theBean = cmo.lookupJDBCSystemResource(beanName)
            if theBean == None:
                  cmo.createJDBCSystemResource(beanName)
      except java.lang.UnsupportedOperationException, usoe:
            pass
      except weblogic.descriptor.BeanAlreadyExistsException,bae:
            pass
      except java.lang.reflect.UndeclaredThrowableException,udt:
            pass

# 创建属性
def create_Property(path, beanName):
    cd(path)
    try:
        print '[INFO] creating mbean of type Property ... '
        theBean = cmo.lookupProperty(beanName)
        if theBean == None:
            cmo.createProperty(beanName)
    except java.lang.UnsupportedOperationException, usoe:
        pass
    except weblogic.descriptor.BeanAlreadyExistsException,bae:
        pass
    except java.lang.reflect.UndeclaredThrowableException,udt:
        pass
    except TypeError:
        prop = cmo.createProperty()
        prop.setName(beanName)

def setAttributes_JDBCResource():
    cd('/JDBCSystemResources/' + datasource_name + '/JDBCResource/' + datasource_name)
    print '[INFO] setting attributes for JDBCResource'
    cmo.setName('' + datasource_name)

def setAttributes_JDBCDataSourceParams():
    cd('/JDBCSystemResources/' + datasource_name + '/JDBCResource/' + datasource_name + '/JDBCDataSourceParams/' + datasource_name)
    print '[INFO] setting attributes for mbean type JDBCDataSourceParams'
    set('GlobalTransactionsProtocol', 'TwoPhaseCommit')
    set('JNDINames', jarray.array([datasource_name], String))

def setAttributes_JDBCDriverParams():
    cd('/JDBCSystemResources/' + datasource_name + '/JDBCResource/' + datasource_name + '/JDBCDriverParams/' + datasource_name)
    print '[INFO] setting attributes for mbean type JDBCDriverParams'
    set('DriverName', datasource_driver)
    set('Url', datasource_url)
    set('Password',datasource_password)

def setAttributes_JDBCConnectionPoolParams():
    cd('/JDBCSystemResources/' + datasource_name + '/JDBCResource/' + datasource_name + '/JDBCConnectionPoolParams/' + datasource_name)
    print '[INFO] setting attributes for mbean type JDBCConnectionPoolParams'
    set('TestTableName', 'SQL SELECT 1 FROM DUAL')
    try:
        set('MaxCapacity', datasource_MaxCapacity)
    except java.lang.IllegalArgumentException:
        # java.lang.IllegalArgumentException: argument type mismatch
        print '\033[1;35m[ERROR] 请检查datasource_MaxCapacity是否为整形（整数后面不能有空格） \033[0m'
    try:
        set('InitialCapacity', datasource_InitialCapacity)
    except:
        print '\033[1;35m[ERROR] 请检查datasource_InitialCapacity是否为整形（整数后面不能有空格） \033[0m'
    try:
        set('CapacityIncrement', datasource_CapacityIncrement)
    except:
        print '\033[1;35m[ERROR] 请检查datasource_InitialCapacity是否为整形（整数后面不能有空格） \033[0m'

def setAttributesFor_user():
    cd('/JDBCSystemResources/' + datasource_name + '/JDBCResource/' + datasource_name + '/JDBCDriverParams/' + datasource_name + '/Properties/' + datasource_name + '/Properties/user')
    print '[INFO] setting attributes for mbean type JDBCProperty'
    set('Value', datasource_username)
    # set('Name', 'user')

def setAttributesFor_jdbc():
    cd('/SystemResources/' + datasource_name)
    print '[INFO] setting attributes for mbean type JDBCSystemResource'
    targets = []
    for target in datasource_target_name.split(','):
        s = 'com.bea:Name=' + target.strip() + ',Type=' + datasource_target_type
        targets.append(ObjectName(str(s)))
    try:
        set('Targets',jarray.array(targets, ObjectName))
    except WLSTException:
        print '\033[1;35m[ERROR] 请检查' + datasource_target_name + '中的各个目标在管理节点的config.xml中是否存在 \033[0m'
        sys.exit()

try:
    connectToAdminserver()
    startTransaction()
    create_JDBCSystemResource('/', datasource_name)
    setAttributes_JDBCResource()
    setAttributes_JDBCDataSourceParams()
    setAttributes_JDBCDriverParams()
    setAttributes_JDBCConnectionPoolParams()
    create_Property('/JDBCSystemResources/' + datasource_name + '/JDBCResource/' + datasource_name + '/JDBCDriverParams/' + datasource_name + '/Properties/' + datasource_name, 'user')
    setAttributesFor_user()
    setAttributesFor_jdbc()
    endTransaction()
    disconnect()
    exit()
except:
    print '出现异常，执行回滚操作'
    undo(defaultAnswer='y', unactivatedChanges='true')
    stopEdit('y')
    print '回滚操作结束'
