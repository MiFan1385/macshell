import socket
import getpass
import os

username = getpass.getuser() # 获取当前用户名
hostname = socket.gethostname() # 获取当前主机名
userfolder = os.path.expanduser("~")

while True:
    cwd = os.getcwd()
    if userfolder in cwd:
        cwd = cwd.replace(userfolder, "~")
        prompt = f"{hostname}:{cwd.replace(':', '')} {username}"
    else:
        prompt = f"{hostname}:\\Disk{cwd.replace(':', '')} {username}"
    command = input(f"{prompt}$ ")
    if command.startswith("sudo "):
        os.system(command.replace("sudo ", ""))
    if command == "exit":
        break
    elif command == "":
        continue
    elif command == "clear":
        os.system("cls")
    elif command.startswith("cd "):
        os.chdir(command.split(" ")[1])
    elif command.startswith("ls"):
        if command == "ls":
            os.system("dir")
        else:
            if "-R" in command:
                command = command.replace("-R", "")
                os.system("dir " + command.split(" ")[1] + " /s")
            else:
                os.system("dir " + command.split(" ")[1])
    elif command == "pwd":
        print(f"\\Disk{cwd.replace(':', '')}")
    elif command == "whoami":
        print(username)
    elif command == "su":
        getpass.getpass("Enter password: ")
        username = "root"
    if command == "who":
        print(f"{username} is logged in")
    elif command.startswith("killall "):
        os.system(f"taskkill /f /im {command.split(' ')[1]}.exe")
    else:
        print("Unknown command:", command)