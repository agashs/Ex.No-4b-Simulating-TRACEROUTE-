from scapy.all import *

target = ["www.saveetha.ac.in"]

result, unans = traceroute(target, maxttl=32)

print(result)
print("Unanswered packets:", unans)
