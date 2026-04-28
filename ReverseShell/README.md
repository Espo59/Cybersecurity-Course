# 🔁 Python-Based Remote Command Execution Lab (Reverse Connection Simulation)

This repository implements a **client-server socket communication system** designed to study reverse connection mechanisms and remote command execution in a controlled cybersecurity environment.

It is intended for educational purposes to demonstrate how TCP-based remote control systems operate at a low level.

---

## 🔍 Overview

A reverse connection model is a network architecture where the **client initiates the connection to the server**, enabling bidirectional communication over TCP.

This design is commonly used in real-world remote administration systems and provides a strong foundation for understanding:

* Network traversal behaviors (NAT/firewall considerations)
* Persistent socket communication
* Remote process execution models

---

## 🛠 Features

### 📦 Reliable Data Framing

Implements a custom protocol using a **4-byte big-endian length header** to ensure:

* Proper message reconstruction
* Prevention of TCP stream fragmentation issues

---

### 🔄 Persistent Connection Handling

* Automatic reconnection logic
* Exponential backoff strategy for stability
* Resilient communication channel design

---

### 🧵 Multi-Threaded Server

* Handles multiple simultaneous client connections
* Non-blocking architecture using Python threading

---

### 📁 Stateful Command Execution

* Internal handling of directory state (`cd` support)
* Maintains session context across commands

---

### ⚙️ Dynamic Configuration

* Runtime configuration of IP address and port
* Flexible deployment in different lab environments

---

## 🚀 Lab Setup & Usage

### 🧪 Requirements

* Python 3.x
* Cross-platform compatibility (Linux / Windows / macOS)
* Standard Python libraries only

---

### ▶️ Step 1 — Start the Server (Controller)

Run on the control machine:

```bash id="k7m3vp"
python3 reverse_shell_server.py
```

* Bind address example: `0.0.0.0`
* Default port: `8000`

The server will wait for incoming connections.

---

### ▶️ Step 2 — Start the Client (Worker Node)

Run on the target machine:

```bash id="x4n8ql"
python3 reverse_shell_client.py
```

Enter:

* Server IP address
* Port (default: 8000)

---

### 💻 Command Execution

Once connected, the server interface will display a prompt:

```
[ip address]$
```

Supported commands:

* `ls` / `dir` → list files
* `whoami` → user identity
* `ipconfig` / `ifconfig` → network info
* `cd` → directory navigation
* `exit` → terminate session

---

## 🧠 Learning Objectives

This project demonstrates:

* TCP socket programming fundamentals
* Bidirectional client-server architectures
* Binary data serialization using `struct`
* Process execution via `subprocess`
* State management in remote sessions
* Security implications of remote command execution systems

---

## 🛡 Defensive Security Perspective

This lab also highlights why modern security systems detect and monitor:

* Unencrypted remote command channels
* Suspicious outbound connections
* Persistent reverse communication patterns
* Endpoint behavior consistent with remote administration tools

It provides insight into how **EDR and network monitoring systems** identify abnormal activity.

---

## ⚠️ Security Disclaimer

This project is intended strictly for **educational and authorized cybersecurity research**.

* Do not use on systems without explicit permission
* Always operate in isolated lab environments
* Unauthorized remote access is illegal

---

## 📄 License

This project is released under the MIT License.
