#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socketserver     # Framework for easily implementing TCP/UDP servers 
import subprocess       # To execute external commands (in this case: openssl) 
import os               # Filesystem operations (checking existence, removing files, etc.) 

class ClientHandler(socketserver.BaseRequestHandler):
    """
    Handler for each individual incoming connection.
    - socketserver.BaseRequestHandler provides:
      * self.request  -> the socket connected to the client 
      * self.client_address -> (ip, port) of the client 
      * handle() -> method called to process the specific request 
    """

    def handle(self):
        """
        Workflow:
        1) Receive an encrypted blob (RSA-OAEP) from the client. 
        2) Save the blob to disk (cipher.bin). 
        3) Convert to Base64 (cipher64.txt) and then back to binary (cipher64.bin). 
        4) Decrypt using 'openssl pkeyutl' with the private key (pub_priv_pair.key). 
        5) Read the plaintext (plainD.txt) and send it back to the client. 
        6) Clean up temporary files. 
        """
        # === 1) Receiving encrypted data from the client ===
        # recv(4096) reads up to 4096 bytes from the TCP stream. 
        encrypted_data = self.request.recv(4096)
        print("Encrypted data received (len={} bytes)".format(len(encrypted_data)))

        # === 2) Persisting to a binary file ===
        # We write the raw data to disk to pass it to the openssl command. 
        with open("cipher.bin", "wb") as f:
            f.write(encrypted_data)

        try:
            # === 3) Base64 conversion via openssl (Optional/Educational) ===
            # Encodes bytes into base64 text. 
            subprocess.run(
                ["openssl", "base64", "-in", "cipher.bin", "-out", "cipher64.txt"],
                check=True  # Raises CalledProcessError if exit code != 0 
            )
            print("Binary file converted to base64 (cipher64.txt).")

            # Decodes base64 representation back into a binary file. 
            subprocess.run(
                ["openssl", "base64", "-d", "-in", "cipher64.txt", "-out", "cipher64.bin"],
                check=True
            )
            print("Base64-decoded file written as binary (cipher64.bin).")

            # === 4) RSA-OAEP Decryption of the content ===
            # Decrypt with -inkey <private_key> and -pkeyopt rsa_padding_mode:oaep. 
            # Security Note: Keep private keys outside the working directory with restricted permissions (600). 
            subprocess.run([
                "openssl", "pkeyutl", "-decrypt",
                "-inkey", "pub_priv_pair.key",         # Private key in PEM format 
                "-in", "cipher64.bin",                 # Encrypted binary input 
                "-out", "plainD.txt",                  # Cleartext output 
                "-pkeyopt", "rsa_padding_mode:oaep"    # OAEP padding (more secure than PKCS#1 v1.5) 
            ], check=True)
            print("Decryption successful (plainD.txt created).")

            # === 5) Reading the plaintext and sending it to the client ===
            # Open in binary mode to ensure data integrity. 
            with open("plainD.txt", "rb") as f:
                decrypted_data = f.read()
                # Send the entire content back to the client. 
                # sendall() blocks until all data is transmitted. 
                self.request.sendall(decrypted_data)
            print("Decrypted file sent to client ({} bytes).".format(len(decrypted_data)))

        except subprocess.CalledProcessError as e:
            # Handle OpenSSL errors: print the exit code and command details. 
            print("An error occurred while running OpenSSL:", e)

        finally:
            # === 6) Cleaning up temporary files ===
            # Remove intermediate files and the plaintext output from the disk. 
            for filename in ["cipher.bin", "cipher64.txt", "cipher64.bin", "plainD.txt"]:
                try:
                    if os.path.exists(filename):
                        os.remove(filename)
                except OSError as e:
                    print(f"Cleanup warning: unable to remove {filename}: {e}")


if __name__ == "__main__":
    # HOST empty = listens on all available interfaces (0.0.0.0). 
    # PORT = 8082. 
    HOST, PORT = "", 8082

    # TCPServer handles connections sequentially (one at a time). 
    with socketserver.TCPServer((HOST, PORT), ClientHandler) as tcpServer:
        print("Server listening on port", PORT)
        try:
            # serve_forever() starts a loop to accept and serve new connections. 
            tcpServer.serve_forever()
        except KeyboardInterrupt:
            # Ctrl+C from terminal: clean exit. 
            print("\nServer interrupted by user")
        except Exception as e:
            print("Server encountered an error:", e)

    # The 'with' context ensures the socket is closed when exiting the block.
