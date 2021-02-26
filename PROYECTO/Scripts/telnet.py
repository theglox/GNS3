import getpass
import telnetlib

#CONFIGURACIÓN BÁSICA DE ROUTER
HOST = "192.168.122.71"
user = input("Ingrese su cuenta Telnet: ")
password = getpass.getpass()

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
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))