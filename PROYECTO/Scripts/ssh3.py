from netmiko import ConnectHandler
#Configuración de Dispositivo y credenciales
iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.84',
    'username': 'cisco',
    'password': 'cisco',
}

#Lectura de comandos usando un archivo externo
with open('Conf-S4') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s4]

#iniciamos la conexión SSH e ingresamos comandos
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

