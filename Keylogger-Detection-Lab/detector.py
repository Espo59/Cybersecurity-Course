import psutil
import os

def check_process_keyloggers():
    """
    Scans active processes for suspicious activity based on names 
    and open file descriptors related to input devices.
    """
    print(f"{'PID':<10} | {'NAME':<20} | {'STATUS'}")
    print("-" * 50)
    
    found_suspicious_proc = False
    
    # Iterate through all running processes and fetch PID, name, and command line arguments
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # 1. Name-based check: Looks for the keyword "input" in process name or startup command
            cmdline_str = " ".join(proc.info['cmdline'] or [])
            is_suspicious = False
            
            if "input" in proc.info['name'].lower() or "input" in cmdline_str.lower():
                is_suspicious = True
            
            # 2. Behavioral check: Check if the process has open files in /dev/input/
            # In Linux, keyboard/mouse events are handled via files in this directory.
            open_files = proc.open_files()
            for f in open_files:
                if '/dev/input/' in f.path:
                    is_suspicious = True
                    break
            
            if is_suspicious:
                print(f"{proc.info['pid']:<10} | {proc.info['name']:<20} | [!] SUSPICIOUS")
                found_suspicious_proc = True
                
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            # Skip system processes that deny access or processes that closed during the scan
            continue
            
    if not found_suspicious_proc:
        print("No suspicious processes detected in User Space.")

def check_kernel_keyloggers():
    """
    Scans loaded Loadable Kernel Modules (LKM). 
    This is necessary because rootkits and kernel-level keyloggers 
    do not appear in the standard process list.
    """
    print("\n--- Kernel Module (LKM) Analysis ---")
    try:
        # /proc/modules contains the list of all modules currently loaded in the Linux Kernel
        with open('/proc/modules', 'r') as f:
            modules_content = f.read()
            
            # Search for "keylogger" or other known malicious module names
            if "keylogger" in modules_content.lower():
                print("[!!!] ALERT: 'keylogger' module detected in the kernel!")
                
                # Extract and print the specific line containing the module details
                for line in modules_content.split('\n'):
                    if "keylogger" in line.lower():
                        print(f"Details: {line}")
            else:
                print("No 'keylogger' module visible in /proc/modules.")
    except Exception as e:
        print(f"Error during kernel analysis: {e}")

if __name__ == "__main__":
    # Security check: The script requires root (sudo) privileges to read 
    # process file descriptors and kernel module information.
    if os.geteuid() != 0:
        print("WARNING: Please run this script with 'sudo' for a full system analysis!")
        print("-" * 50)
    
    # Run User Space analysis (Processes)
    check_process_keyloggers()
    
    # Run Kernel Space analysis (Modules)
    check_kernel_keyloggers()
