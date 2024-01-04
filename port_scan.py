import socket

s = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)

target = input("Enter site to scan: ")

for port in range(1000):
    print(f"Ckecking Port {port}", end=" : ")
    try:
        con = s.connect((target, port))
        print("open!")
    except:
        print("closed!")
