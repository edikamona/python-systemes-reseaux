import platform
import socket

print("=== SYSTEM INFORMATION ===")

print(f"Operating System : {platform.system()}")
print(f"OS Version       : {platform.version()}")
print(f"Machine          : {platform.machine()}")
print(f"Processor        : {platform.processor()}")

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname         : {hostname}")
print(f"IP Address       : {ip_address}")
