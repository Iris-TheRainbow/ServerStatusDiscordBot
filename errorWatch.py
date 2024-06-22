import time
import importantServices
import os
def watchdog():
    while True:
        inactives = []
        inactive = False
        message = ''
        for service in importantServices.services():
            os.system('sudo systemctl status ' + service + ' | grep Active > active')
            active = ''
            with open('active', "r") as f:
                active = f.readline()
                f.close()
            if 'inactive' in active:
                inactives.append(service)
                inactive = True
        if inactive:
            for service in inactives:
                message += service
                if service != inactives[-1]:
                    message += ', '
            message += ' are down!'
            with open('trigger', 'w') as f:
                f.write('1\n'+ message)