from zabbix_api import ZabbixAPI

server = "http://15.228.60.226/"
UserName = input("Digite o nome de usário: ")
Password = input("Digite a sua senha: ")


# Instanciando a API
zapi = ZabbixAPI(server = server, path = "", log_level = 0)
zapi.login(UserName, Password)

# Obtendo uma lista com os hosts que ja estão no zabbix
hosts = zapi.host.get({"output":"extend"})
for host in hosts:
    hostID = host[u'hostid']
    HostName = host[u'name']
    print ("Host: ", HostName, "HostID: ", hostID)