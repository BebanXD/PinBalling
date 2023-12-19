ip_address="192.168.1.10"

substrings = ip_address.split(".")

a= [int(part) for part in substrings]
print(a)