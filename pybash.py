import subprocess
import os, time

def pybash(command):
    if command == "help":
        return "discbash: a simple shell written in Python for discord"
    else:
        if "|" in command:
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            fdin = os.dup(s_in)

            for cmd in command.split("|"):

                os.dup2(fdin, 0)
                os.close(fdin)

                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                os.dup2(fdout, 1)
                os.close(fdout)
                if 'cd' in cmd.strip().split(' '):
                    path = cmd.strip().split(' ')[1]
                    try:
                        os.chdir(os.path.abspath(path))
                        return
                    except Exception:
                        return "cd: no such file or directory: " + path
                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    return "psh: command not found: " + cmd.strip()
            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)      
        if 'cd' in command.split(' '):
            path = command.split(' ')[1]
            try:
                os.chdir(os.path.abspath(path))
                return
            except Exception:
                return "cd: no such file or directory: " + path
        try:
            subprocess.run(command.split())
        except Exception:
            return "psh: command not found: " + command

while True:
    command = input("$ ")
    print(pybash(command))
    time.sleep(.01)        