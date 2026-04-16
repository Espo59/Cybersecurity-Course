#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket       # Low-level networking API (TCP/IP): handles connection and data transfer
import sys          # Access to command-line arguments and system exit

def get_server_address():
    """
    Prompts the user for the server's IP address and port, then validates the input.
    - Loops until a valid address is provided.
    - Handles Ctrl+C for a clean exit.
    Returns:
        (ip: str, port: int)
    """
    while True:
        try:
            # Ask for the server's IP address
            ip = input("Enter the server IP address: ").strip()
            if not ip:
                print("IP address cannot be empty.")
                continue

            # Ask for the port and ensure it is a numeric value
            port_input = input("Enter the server port number: ").strip()
            if not port_input.isdigit():
                print("Port must be a number.")
                continue

            # Convert to integer and verify it's within the valid TCP port range (1–65535)
            port = int(port_input)
            if not (0 < port < 65536):
                print("Port must be in range 1–65535.")
                continue

            return (ip, port)

        except KeyboardInterrupt:
            # Clean exit if the user interrupts the input process
            print("\nUser interrupted input. Exiting.")
            sys.exit(1)


def main():
    """
    Main client routine:
    1) Get server address from command line arguments or user input.
    2) Load the encrypted file 'cipher.bin' from the current directory.
    3) Establish a TCP connection and send the encrypted file content.
    4) Receive the decrypted results in 4096-byte chunks until the server closes the connection.
    5) Save the received plaintext to 'plainD.txt'.
    """
    
    # === 1) Parsing IP/Port from command line arguments ===
    # Expected format: python client_sender_key.py <server_ip> <server_port>
    if len(sys.argv) == 3:
        server_ip = sys.argv[1]
        try:
            server_port = int(sys.argv[2])
            if not (0 < server_port < 65536):
                raise ValueError
            server_address = (server_ip, server_port)
        except ValueError:
            print("Invalid port number in arguments. Falling back to manual input.")
            server_address = get_server_address()
    else:
        server_address = get_server_address()

    # === 2) Loading the encrypted file ===
    # 'cipher.bin' must be present in the same folder as the script
    try:
        with open("cipher.bin", "rb") as f:
            encrypted_data = f.read()
    except FileNotFoundError:
        print("Error: 'cipher.bin' not found.")
        return

    # === 3) Connecting to the server and sending data ===
    try:
        # socket.create_connection handles DNS resolution and opens the TCP socket
        with socket.create_connection(server_address) as sock:
            print(f"Connected to server {server_address[0]}:{server_address[1]}")

            # Send the entire encrypted buffer
            sock.sendall(encrypted_data)
            print("File 'cipher.bin' sent to the server.")

            # === 4) Receiving the decrypted plaintext ===
            # We read in a loop because the data length might be unknown
            decrypted_data = b""
            while True:
                # Receive in blocks of 4096 bytes
                part = sock.recv(4096)
                if not part:
                    # Server closed the connection (EOF)
                    break
                decrypted_data += part

            print("Decrypted file received from the server.")

            # === 5) Saving the result to disk ===
            # Write the received data to 'plainD.txt' in binary mode
            with open("plainD.txt", "wb") as f:
                f.write(decrypted_data)
            print("File 'plainD.txt' saved locally.")

    # === Error Handling ===
    except ConnectionRefusedError:
        print("Error: Connection refused. Check if the server is running.")
    except TimeoutError:
        print("Error: Connection timed out.")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
