from pyzabbix.api import ZabbixAPI

# Informaçoes sobre o login no servidor zabbix
zapi = ZabbixAPI(url='http://15.228.60.226/', user='nathan.silva', password='S3c77$1Nfr488')

# Pega todos os hosts monitorados
result1 = zapi.host.get(monitored_hosts=1, output='extend')

# Pega todos os hosts desabilitados
result2 = zapi.do_request('host.get',
                            {
                                'filter': {'status': 1},
                                'output': 'extend'
                            })

# Filtra resultados
hostnames1 = [host['host'] for host in result1]
hostnames2 = [host['host'] for host in result2['result']]