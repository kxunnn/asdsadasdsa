import socket
def ip():
    ip = input("IP : ")
    if ip =="127.0.0.1":
        for ip in range(100000):
            print("DDOS ATTACK SUCCUSS ---------->")
        else:
            print("DDOS ATTACK FAIL ----------->")
ip()