import os

ip_v4 = str(input("Enter the ip address to scan : "))

ping_host = os.popen(f"ping {ip_v4}").read()

print(f" *** Ping host is successful ***\n {ping_host}")