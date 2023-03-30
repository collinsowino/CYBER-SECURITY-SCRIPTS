#nc -vv -l -p 4444  -- run this command in linux computer
# it is equivalent to listener.py

import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("10.0.0.16", 4444))

connection.send("\n [+] Connection established.\n")

recieved_data = connection.recv(1024)
print(recieved_data)

connection.close()