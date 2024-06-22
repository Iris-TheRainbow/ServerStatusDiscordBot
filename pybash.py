import subprocess
import os, time

def shell(command):
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
                    try:
                        path = cmd.strip().split(' ')[1]
                        os.chdir(os.path.abspath(path))
                        continue
                    except Exception:
                        continue
                try:
                    subprocess.run(cmd.strip().split(), capture_output=True)
                    return 
                except Exception:
                    return "psh: command not found: " + cmd.strip()
            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)    
            return 
        if 'cd' == command.split(' ')[0]:
            path = ''
            try:
                path = command.split(' ')[1]
                os.chdir(os.path.abspath(path))
                return
            except Exception:
                return "cd: no such file or directory: " + path
        process = subprocess.Popen(command.split(' '),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
        stdoutdata,stderrdata=process.communicate()
        return stdoutdata.decode('utf-8')
        return "psh: command not found: " + command

if __name__ == '__main__':    
    while True:
        command = input("$ ")
        print(shell(command))