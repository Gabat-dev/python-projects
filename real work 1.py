import socket
dangerous_ports ={
    22:"remote access port",
    21:"file transfer port",
    23:"telnet- ver secure",
    3306:"database exposed",
    3389:"remote desktop expose"
}
port_name ={
    21:"ftp",
    22:"SSH",
    80:"HTTP",
    4443:"HTTPS",
    3306:"MySQL",
    3389:"RDP"
}

def scanport (host,port):
    scanner = socket.socket()
    scanner.settimeout(.5)
    result = scanner.connect_ex((host,port))
    scanner.close()
    return result == 0

host = input("enter your host:")
port = int(input("enter your port:"))
print(f"/nScanning {host} fron port {port}.../n")

if scanport(host, port):
    name = port_name.get(port, "unknown")
    print(f"port {port}({name}) is open")

if port in dangerous_ports:
    warning = dangerous_ports[port]
    print(f"warning:{warning}")
    