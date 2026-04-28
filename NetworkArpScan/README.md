# 🌐 Network Discovery & ARP Scanner (Scapy-based)

A high-performance network reconnaissance tool designed to discover active hosts within a Local Area Network (LAN) using the **Address Resolution Protocol (ARP)**.

This project demonstrates how Layer 2 communication can be used for reliable host discovery, even in environments where ICMP (ping) is restricted.

---

## 🔍 How It Works

Unlike traditional ICMP-based scanners, this tool operates at the **Data Link Layer (Layer 2)** using ARP requests.

### 📦 Packet Construction

* Builds a custom **Ethernet frame**
* Uses broadcast MAC address: `ff:ff:ff:ff:ff:ff`
* Encapsulates an ARP request (`who-has`, opcode 1)

---

### 📡 Network Discovery Process

1. Sends ARP broadcast requests to all IPs in the target range
2. Hosts that are active respond with ARP replies (`is-at`, opcode 2)
3. The script captures and parses responses
4. Maps IP addresses to MAC addresses

---

## 🛠 Features

* **CIDR Range Scanning**
  Supports full subnet scanning (e.g., `192.168.1.0/24`)

* **Interface Selection**
  Allows scanning through specific interfaces (`eth0`, `wlan0`, etc.)

* **Custom Timeout Control**
  Adjust response waiting time for speed vs accuracy

* **Interface Validation**
  Automatically checks if the selected network interface exists

* **Clean Output Formatting**
  Displays results as:
  `IP Address → MAC Address`

---

## 🧪 Educational Objectives

This project helps understand:

* Layer 2 broadcasting mechanisms
* How ARP is used for local network communication
* Role of the ARP cache in LAN environments
* Packet crafting using Scapy
* Differences between ICMP-based and ARP-based discovery

---

## 🚀 Requirements

* Linux (Kali Linux, Parrot OS, or Ubuntu recommended)
* Python 3.x
* Scapy

Install dependency:

```bash id="n7k2vp"
pip install scapy
```

---

## ▶️ Usage

### Run the Scanner

```bash id="c3m8xn"
sudo python3 arp_sweep.py -n 192.168.1.0/24 -i eth0
```

### Parameters

* `-n` → Target network range (CIDR notation)
* `-i` → Network interface

---

## 📖 Learning Outcomes

This tool demonstrates:

* Practical use of ARP in LAN environments
* Ethernet frame structure and Layer 2 communication
* Network reconnaissance techniques
* Scapy-based packet manipulation
* Host discovery without ICMP dependency

---

## ⚠️ Security & Ethical Notice

This tool is intended strictly for educational and authorized testing purposes.

* Do not scan networks without explicit permission
* Unauthorized reconnaissance may be illegal
* Always use within controlled lab environments

---

## 📄 License

This project is released under the MIT License.
