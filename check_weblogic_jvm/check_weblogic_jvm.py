# 管理服务器控控制台用户名
adminserver_username = 'weblogic'
# 管理服务器控制台密码
adminserver_password = 'servyou2017'
# 管理服务器ip
adminserver_ip = '10.199.129.73'
# 管理服务器端口
adminserver_port = 7600

# jvm报警百分比 
jvm_warning_percent = 70

def monitor_jvm_heap_size_of_server(server_name):
    domainConfig()
    serverNames = cmo.getServers()
    domainRuntime()
    for server in serverNames:
        if server.getName() == server_name:
            print 'Now checking ' + server_name
            try:
                cd('/ServerRuntimes/' + server_name + '/JVMRuntime/' + server_name)
            except WLSTException,e:
                # 通常意味着尚未启动服务器，忽略即可
                pass
            # 获取jvm堆空闲比例
            used_percent = 100 - cmo.getHeapFreePercent()
            if used_percent >= jvm_warning_percent:
                print 'WARNING: Jvm heap usage ' + str(used_percent) + '% exceeds ' + str(jvm_warning_percent) + '%'
            else:
                print 'INFO: Jvm heap usage: ' + str(used_percent)
            break
    else:
        print server + 'not exist'

def monitor_jvm_heap_size_of_cluster():
    domainConfig()
    serverNames = cmo.getServers()
    domainRuntime()
    for server in serverNames:
        print 'INFO: Now checking ' + server.getName()
        try:
            cd('/ServerRuntimes/' + server.getName() + '/JVMRuntime/' + server.getName())
        except WLSTException,e:
            # 通常意味着尚未启动服务器，忽略即可
            pass
        # 获取jvm堆空闲比例
        used_percent = 100 - cmo.getHeapFreePercent()
        if used_percent >= jvm_warning_percent:
            print 'WARNING: Jvm heap usage ' + str(used_percent) + '% exceeds ' + str(jvm_warning_percent) + '%'
        else:
            print 'INFO: Jvm heap usage: ' + str(used_percent)

connect(adminserver_username, adminserver_password, 't3://' + adminserver_ip + ':' + str(adminserver_port))
server_name = 'gscgjs01_Server'
monitor_jvm_heap_size_of_server(server_name)
# monitor_jvm_heap_size_of_cluster()