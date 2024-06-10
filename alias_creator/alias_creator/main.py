import os
import subprocess

def clear():
    if os.name == 'posix':
        _ = os.system('clear')
    elif os.name == 'nt':
        _ = os.system('cls')

reload="source ~/.bashrc"

def main():
    f=open("~/.bashrc", "a")
    clear()
    print("\n ALIAS CREATOR")
    name=str(input("\n Enter alias name: "))
    command=str(input(" Insert command to replace: "))
    f.write(f"alias {name}='{command}'\n")
    f.close()
    subprocess.run(reload, shell=True, executable='/bin/bash')

if __name__ == '__main__':
    main()
