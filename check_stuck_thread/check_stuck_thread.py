# 管理服务器控控制台用户名
adminserver_username = 'weblogic'
# 管理服务器控制台密码
adminserver_password = 'servyou2017'
# 管理服务器ip
adminserver_ip = '10.199.129.73'
# 管理服务器端口
adminserver_port = 7600

# 阻塞线程上限，超出此上限报警
stuck_thread_limit = 5

def monitor_stuck_thread_of_server(server):
    # 阻止print的内容输出到屏幕
    redirect('/dev/null', 'false')
    
    domainRuntime()
    # servers = ls('/ServerRuntimes', 'true', 'c')
    # todo(clg): 判断server是否在servers中
    
    deployments = ls('/ServerRuntimes/' + server + '/ApplicationRuntimes', 'true', 'c')
    cnt = 0
    for deployment in deployments:
        # 如果只关注具体的deployment，可以加if判断
        # if(deployment.getName() == "MyApplication"):
        # 遍历所有的workmanagers
        wms = ls('/ServerRuntimes/'  + server + '/ApplicationRuntimes/' + deployment + '/WorkManagerRuntimes','true','c')
        for wm in wms:
            cd('/ServerRuntimes/' + server + '/ApplicationRuntimes/' + deployment + '/WorkManagerRuntimes/' + wm) 
            cnt = cnt + get('StuckThreadCount')
    
    ## 开启到屏幕的输出
    redirect('/dev/null','true')
    
    ## 判断是否超过阻塞线程上限，并输出相应的信息，信息可用于nagios监控
    if cnt >= stuck_thread_limit:
        print(server + " has "  + str(cnt) + " stuck threads, exceeds " + stuck_thread_limit)
    else:
        print(server + " has "  + str(cnt) + " stuck threads.")

def monitor_stuck_thread_of_cluster():
    # 阻止print的内容输出到屏幕
    redirect('/dev/null', 'false')
    
    domainRuntime()
    servers = ls('/ServerRuntimes', 'true', 'c')
    
    # 使用字典存储每一个server对应的stuck线程数，server_name为键 
    result = dict()
    for server in servers:
        deployments = ls('/ServerRuntimes/' + server + '/ApplicationRuntimes', 'true', 'c')
        result[server] = 0
        for deployment in deployments:
            # 如果只关注具体的deployment，可以加if判断
            # if(deployment.getName() == "MyApplication"):
            # 遍历所有的workmanagers
            wms = ls('/ServerRuntimes/'  + server + '/ApplicationRuntimes/' + deployment + '/WorkManagerRuntimes','true','c')
            for wm in wms:
                cd('/ServerRuntimes/' + server + '/ApplicationRuntimes/' + deployment + '/WorkManagerRuntimes/' + wm) 
                result[server] = result[server] + get('StuckThreadCount')
    
    ## 开启到屏幕的输出
    redirect('/dev/null','true')
    
    ## 判断每一个server是否超过阻塞线程上限，并输出相应的信息，信息可用于nagios监控
    for key in result:
        if result[key] >= stuck_thread_limit:
            print(key + " has "  + str(result[key]) + " stuck threads, exceeds " + stuck_thread_limit)
        else:
            print(key + " has "  + str(result[key]) + " stuck threads.")
        
redirect('/dev/null', 'false')
connect(adminserver_username, adminserver_password, 't3://' + adminserver_ip + ':' + str(adminserver_port))
redirect('/dev/null','true')

# 第一种方式：监控指定server
server_name = 'gscgjs01_Server'
monitor_stuck_thread_of_server(server_name)

# 第二种方式：监控cluster里面的所有server
# monitor_stuck_thread_of_cluster()

disconnect()
