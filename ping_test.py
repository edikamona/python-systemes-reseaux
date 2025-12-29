import os

host = input("Enter a host or IP address to ping: ")

response = os.system(f"ping {host}")

if response == 0:
    print(f"{host} is reachable")
else:
    print(f"{host} is not reachable")