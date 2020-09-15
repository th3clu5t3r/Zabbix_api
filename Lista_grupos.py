from zabbix_api import ZabbixAPI

server = "http://15.228.60.226/"
UserName = input("Digite o nome de usário: ")
Password = input("Digite a sua senha: ")


# Instanciando a API
zapi = ZabbixAPI(server = server, path = "", log_level = 0)
zapi.login(UserName, Password)

# Obtendo uma lista com os grupos que ja estão no zabbix
grupos = zapi.hostgroup.get({"output":"extend"})
for q in grupos:
    GoupID = q[u'groupid']
    GroupName = q[u'name']
    print ("Grupo: %s " %(GroupName))