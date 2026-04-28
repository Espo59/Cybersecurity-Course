# 🌐 Simple Python TCP Client-Server Communication Lab

A minimal implementation of a **TCP client-server architecture** using Python’s built-in `socket` library.

This project demonstrates the foundational concepts of **network programming** and the **TCP/IP communication model**.

---

## 📌 Overview

The system consists of two components:

### 🖥️ Server (`server.py`)

* Acts as a TCP listener
* Waits for incoming client connections on a specified port
* Accepts connections and sends a basic response message
* Demonstrates the server-side socket lifecycle

---

### 💻 Client (`client.py`)

* Initiates a TCP connection to the server
* Connects using IP address and port
* Receives and displays data from the server
* Demonstrates client-side connection handling

---

## 🛠 Features

### 🌐 TCP/IP Communication

* Reliable, connection-oriented data transfer using TCP
* Demonstrates handshake-based communication

---

### 📚 Socket Lifecycle Understanding

Fully documented flow including:

* `socket()` → create endpoint
* `bind()` → assign address (server)
* `listen()` → wait for connections
* `accept()` → accept incoming client
* `connect()` → establish client connection

---

### ⚡ Lightweight Implementation

* No external dependencies
* Uses only Python standard library
* Designed for clarity and educational use

---

## 🚀 Usage

### 📦 Requirements

* Python 3.x on both client and server machines
* Network connectivity between machines (same LAN or routed network)

---

### ▶️ Step 1 — Start Server

On the server machine:

```bash id="k7m2vp"
python3 server.py
```

Expected output:

```text id="x3n8ql"
--------- listening for connection on port 4444 ---------
```

---

### ▶️ Step 2 — Start Client

On the client machine:

```bash id="m9c4vz"
python3 client.py
```

The client will connect to the server and receive a response message.

---

## 📖 Learning Objectives

This project demonstrates:

* Fundamentals of TCP/IP networking
* Client-server architecture design
* Socket programming in Python
* Connection lifecycle management
* Basic inter-process communication over networks

---

## 🧪 Educational Context

This implementation is intended to help understand:

* How data is transmitted over TCP connections
* How servers handle multiple connection states
* How clients initiate and maintain communication
* The role of ports and IP addresses in networking

---

## ⚠️ Security Notice

This project is intended strictly for **educational and controlled environments**.

* Do not expose on public networks
* Use only in local or authorized lab environments
* Not intended for production use

---

## 📄 License

This project is released under the MIT License.
