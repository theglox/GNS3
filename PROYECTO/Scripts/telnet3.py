import getpass
import telnetlib

#CONFIGURACIÓN DE SWITCH Y VLAN
HOST = "localhost"
user = input("Ingrese su cuenta Telnet: ")
password = getpass.getpass()

f = open('IPs')

for IP in f:
    IP = IP.strip()
    print("Configurando el Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    #ingresamos los comandos que vayan a ejecutarse en el router
    tn.write(b"enable\n")
    tn.write(b"cisco\n") #password
    tn.write(b"configure terminal\n")

    for i in range (2,5):
        tn.write(b"vlan "+ str(n).encode('ascii') +b"\n")
        tn.write(b"name Python_VLAN_"+ str(n).encode('ascii') +b"\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))