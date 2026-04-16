# Simple Python TCP Socket Communication

A minimalist implementation of a Client-Server architecture using Python's built-in `socket` library. 
This project demonstrates the fundamental concepts of network programming, specifically the Transmission Control Protocol (TCP).

---

# 📌 Overview

This project consists of two main components:
- **Server (`server.py`)**: Acts as a listener that waits for incoming connections on a specified port. Once a connection is established, it sends a welcome message to the client.
- **Client (`client.py`)**: Acts as the initiator that connects to the server's IP address and port to retrieve the transmitted data.

---

# 🚀 Features

- **TCP/IP Networking**: Reliable, connection-oriented data transfer.
- **Detailed Documentation**: Code is commented in English to explain every step of the socket lifecycle (Bind, Listen, Accept, Connect).
- **Lightweight**: No external dependencies required, uses standard Python libraries.

---

# 🛠️ Usage

### 1. Prerequisites
Ensure you have Python 3.x installed on both the server and client machines.

### 2. Running the Server
On the host machine (e.g., your Kali Linux instance), execute:
```bash python3 server.py```

The server will display:

```---------listening for connection on port-----------4444```


Ecco una proposta di file README.md professionale e ben strutturato per il tuo repository GitHub. È scritto interamente in inglese, come richiesto, ed è ottimizzato per spiegare chiaramente il progetto a chiunque visiti la tua pagina.

Ti ho preparato anche un'anteprima PDF del contenuto per vedere come apparirebbe graficamente.

README.md
Markdown
# Simple Python TCP Socket Communication

A minimalist implementation of a Client-Server architecture using Python's built-in `socket` library. This project demonstrates the fundamental concepts of network programming, specifically the Transmission Control Protocol (TCP).

## 📌 Overview

This project consists of two main components:
1.  **Server (`server.py`)**: Acts as a listener that waits for incoming connections on a specified port. Once a connection is established, it sends a welcome message to the client.
2.  **Client (`client.py`)**: Acts as the initiator that connects to the server's IP address and port to retrieve the transmitted data.

## 🚀 Features

* **TCP/IP Networking**: Reliable, connection-oriented data transfer.
* **Detailed Documentation**: Code is commented in English to explain every step of the socket lifecycle (Bind, Listen, Accept, Connect).
* **Lightweight**: No external dependencies required, uses standard Python libraries.

## 🛠️ Usage

### 1. Prerequisites
Ensure you have Python 3.x installed on both the server and client machines.

### 2. Running the Server
On the host machine (e.g., your Kali Linux instance), execute:
```bash python3 server.py```

The server will display: 

```---------listening for connection on port-----------4444```

### 3. Running the Client

Open `client.py` and update the ip variable with the server's IP address:

`ip = "YOUR_SERVER_IP"`

Run the client script:

`python3 client.py`

---

# 📂 Project Structure
*server.py* - The server-side script (previously main.py).

*client.py* - The client-side script.

---

# ⚠️ Disclaimer
This project is for educational purposes only. It was created to understand the basics of network sockets and should 
only be used on networks and systems where you have explicit permission to perform testing.
