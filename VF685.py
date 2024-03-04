import sys,os 

print("are you root?")
choice = input("y/n: ")
if(choice == "y" or choice == "Y"):
    os.system("msfconsole -r VF685.rc")
else:
    print("\n")
    print("+-----------------------------------------+")
    print("| You must be root to Perform that action |")
    print("+-----------------------------------------+")
    os.system("python3 main.py")