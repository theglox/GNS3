# Configuración de dispositivos
![IP](\img\ipv4.jpg)
## Routers (g0/0)
```
enable
configure terminal
host R#
int g0/0
ip address 192.168.122.# 255.255.255.0
no shutdown
end
wr
```

## Switches (vlan 1)
```
enable
configure terminal
host S#
int vlan 1
ip address 192.168.122.# 255.255.255.0
no shutdown
end
wr
```

---
---
---

![telnet](\img\telnet.jpeg)

## Routers & Switches (Telnet)

```
enable
configure terminal
username cisco password cisco
enable password cisco
line vty 0 4
 login local
 transport input telnet
end
```

---

![SSH](\img\ssh.jpg)

## Routers & Switches (SSH)
```
enable 
configure terminal
username cisco password cisco
username cisco priv 15

line vty 0 4
 login local
 transport input ssh
end
conf t

ip domain-name cciepython.com
crypto key generate rsa
1024

end
```

---
---
---

![GNS3](https://gns3.com/assets/custom/gns3/images/logo-colour.png)

## Topologías

* [Topología 1](Topologías\Topología1.gns3project)
    ![Topología 1](\img\Topología_1.png)   
* [Topología 2](Topologías\Topología2.gns3project)
    ![Topología 2](\img\Topología_2.png)   


---

![python](\img\python.png)

## Scripts

* Telnet
    * [Topología 1 - Router](Scripts\telnet.py)
    * [Topología 1 - Switch](Scripts\telnet2.py)
    * [Topología 2 - 4 Switches](Scripts\telnet3.py)
        * [IPs](Scripts\IPs)

* SSH
    * [Topología 2 - Switch S1](Scripts\ssh.py)
    * [Topología 2 - 3 Switches](Scripts\ssh2.py)
    * [Topología 2 - Switch S4](Scripts\ssh3.py)
        * [Comandos](Scripts\Conf-S4)


## IPS

```
192.168.122.71
192.168.122.72
192.168.122.82
192.168.122.83
192.168.122.84
192.168.122.85
192.168.122.86
```
