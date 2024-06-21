import os
import psutil


def getStatus(systemServices):
    os.system("sudo tailscale status > tsstatus")
    statuses = []
    for service in systemServices:
        os.system("sudo systemctl status " + service + " | grep Active > " + service)
        f = open(service)
        statuses.append(service + f.readline()[11:-1])
        f.close
        os.system("rm " + service)
    return statuses

def getCPUFreq():
    return str(round(psutil.cpu_freq()[0]))

def getCPUUsage():
    return str(psutil.cpu_percent(.25))

def getRAMUsage():
    return str(psutil.virtual_memory()[2])

def getUptime_Days():
    with open('/proc/uptime', 'r') as f:
        return str(round(float(f.readline().split()[0])/86400, 2))