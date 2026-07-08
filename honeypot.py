import socket
import datetime
import logging

logging.basicConfig(filename="honeypot.log", level=logging.INFO, format="%(message)s")
def start_honeypot(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0",port))
    server.listen(5)
    print(f"honeypot running on port {port}...")
    print("waiting for attackers....\n")

    while True:
        client, address = server.accept()
        client.send("welcome to SSH server v1.0\r\n".encode())
        time = datetime.datetime.now()
        logging.info(f"connect from {address[0]} at {time}")
        client.close()

start_honeypot(9999)