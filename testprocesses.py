import os

os.system("sudo tailscale status > tsstatus")
os.system("hostname > hostname")
f = open("hostname")
hostname = f.readline()
f.close()
f = open("tsstatus")
print(hostname)
for line in f.readlines():
    string = str(line)
    print(string)
    if hostname in string:
        print(string)