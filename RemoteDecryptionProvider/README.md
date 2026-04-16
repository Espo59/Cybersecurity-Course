# RSA Remote Decryption Service (Python Sockets)
This project implements a Client-Server architecture designed to perform remote RSA decryption. 
It demonstrates how to handle binary data transmission over TCP/IP sockets and integrate Python with OpenSSL for cryptographic operations.

---

# 📌 Project Overview
The system allows a client to send an RSA-encrypted binary file to a server. 
The server uses a stored private key to decrypt the file and sends the original plaintext back to the client.

- **Components:**

`server_sender_key.py:` A TCP server that listens for encrypted data, processes it via OpenSSL, and returns the decrypted message.

`client_sender_key.py:` A client utility that reads a local encrypted file, transmits it to the server, and saves the received plaintext.

`pub_priv_pair.key:` The RSA private key used by the server for decryption.

`cipher.bin:` A sample encrypted binary file used for testing the communication.

---

# 🛠️ Cryptographic Details

### 1. The Private Key (pub_priv_pair.key)
This file contains the RSA Private Key. In this workflow, the server must possess this key to reverse the encryption applied to the data.

*Warning: The included key is for educational purposes only. Never share real private keys on public repositories.*

### 2. The Cipher File (cipher.bin)
This is a binary "blob" containing data encrypted with the corresponding RSA Public Key. It is unreadable without the decryption process.

---

# 🚀 How to Create Your Own Keys and Cipher

If you want to generate a new pair of keys or a new encrypted file, you can use the following OpenSSL commands in your terminal:

- **A. Generate a new RSA Private Key**

`bash openssl genrsa -out pub_priv_pair.key 1024`

- **B. Extract the Public Key (to share with others)**

`bash openssl rsa -in pub_priv_pair.key -pubout -out public_key.pem`

- **C. Create an encrypted file (cipher.bin)**

Create a secret text file:

`bash echo "This is a secret message" > secret.txt`

Encrypt it using the Public Key and OAEP padding:

`bash openssl pkeyutl -encrypt -pubin -inkey public_key.pem -in secret.txt -out cipher.bin -pkeyopt rsa_padding_mode:oaep`

---

# 💻 Usage Instructions

- ### 1. Start the Server

Place server_sender_key.py and pub_priv_pair.key in the same directory and run:

`bash python3 server_sender_key.py`

The server will start listening on port 8082.

- ### 2. Run the Client

Ensure cipher.bin is in the client's directory and run:

`bash python3 client_sender_key.py <SERVER_IP> 8082`

The client will send the file, and once the process is complete, a new file named plainD.txt will appear in your folder containing the decrypted text.

---

# ⚠️ Disclaimer
This software is intended for educational and research purposes in the field of cybersecurity. Unauthorized access to computer systems is illegal. Always test in controlled lab environments like Metasploitable.
