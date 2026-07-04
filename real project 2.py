import socket
def scan_port(host,port):
    scanner = socket.socket()
    scanner. settimeout(1)
    result = scanner.connect_ex((host,port))
    scanner.close()
    return result == 0
host = input("enter host to scan")
start_port = int(input("enter port to can"))
end_port = int(input("enter end port to scan"))
print (f"/nScanning {host} from port {start_port} to {end_port}.../n")

for port in range(start_port,end_port + 1):
    if scan_port(host, port):
        name = port_names.get(port,"unknown")
        print(f"port{port}({name}) is open")
else:
    print(f"port {port} is close")






import socket
def scan_port(host,port):
    scanner = socket.socket()
    scanner.settimeout(1)
    result = scanner.connect_ex((host,port))
    scanner.close()
    if result == 0:
        return"open"
    else:
        return"closed"

host = input("enter host to scan")
port = int(input("enter port"))

status = scan_port(host,port)
print(f"port{ port } is { status}")













