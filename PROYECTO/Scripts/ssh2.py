from netmiko import ConnectHandler
#Configuración de Dispositivos y credenciales
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.82',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.83',
    'username': 'cisco',
    'password': 'cisco'
}

#especificamos los dispositivos que se van a configurar
all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

#iniciamos la conexión SSH e ingresamos comandos
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print ("Creating VLAN " + str(n))
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print (output)
