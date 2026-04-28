# 🔗 P2P Distributed Network Management & Communication Toolkit

This project implements a **peer-to-peer (P2P) distributed network simulation** designed to study network communication, remote administration concepts, and multi-node coordination between heterogeneous systems.

It includes interoperability between modern Linux environments (Kali / Ubuntu) and legacy systems (Metasploitable 2).

---

## ⚠️ Educational Purpose & Legal Disclaimer

This project is intended strictly for **educational and authorized security testing environments**.

* Do not deploy on production systems or unauthorized networks
* One component is intentionally designed to execute remote commands in a controlled lab setting
* Use only in isolated or permissioned environments

---

## 🏗️ Architecture Overview

The system consists of two main components:

### 🖥️ P2P Controller (`p2p_node.py`)

A Python 3.x application running on modern Linux systems (Kali / Ubuntu).

Capabilities:

* Acts as a network node and control interface
* Supports multi-peer communication
* Enables command broadcasting across connected nodes
* Supports script transfer and execution in lab environments
* Provides interactive CLI for node management

---

### 🧾 P2P Worker Node (`p2p_victim.py`)

A Python 2.7-compatible node designed for legacy environments (e.g., Metasploitable 2).

Capabilities:

* Passive listening mode for incoming controller connections
* Executes received commands in a controlled environment
* Maintains persistent connection with the controller node

---

## 🚀 Getting Started

### 🧪 Setup on Metasploitable 2 (Worker Node)

Run using Python 2:

```bash id="p2q8mn"
python p2p_victim.py 8082
```

The node will start listening for incoming connections.

---

### 🖥️ Setup on Kali Linux / Ubuntu (Controller)

Run the controller on Python 3:

```bash id="x7c3vz"
sudo python3 p2p_node.py 8080
```

Optional secondary node (e.g., Lubuntu):

```bash id="m4n9ql"
sudo python3 p2p_node.py 8081
```

---

## 🔌 Establishing Connections

Once both nodes are running:

### From Controller → Worker

```bash id="k8v2xp"
connect 192.168.1.15 8082
```

### From Worker → Controller (reverse connection)

```bash id="r3m7zn"
connect <kali-ip> <kali-port>
```

---

## 📋 Available CLI Commands

Once connected, the controller supports the following commands:

* `list` → Show connected nodes
* `exec` → Execute command on all nodes
* `status` → Retrieve node status
* `send_script` → Transfer scripts to nodes
* `send` → Broadcast message
* `exit` → Close connection

---

## 🧪 Technical Features

* **Peer-to-Peer Architecture**
  Decentralized communication model between nodes

* **Multi-Threaded Networking**
  Each connection is handled in an independent thread

* **Legacy Compatibility Layer**
  Supports Python 2.7 environments for older systems

* **Remote Script Deployment (Lab Use)**
  Enables controlled transfer and execution of scripts in testing environments

* **Robust Packet Handling**
  Improves stability against malformed or incomplete network messages

---

## 📖 Learning Objectives

This project demonstrates:

* Fundamentals of P2P network architecture
* Distributed system communication patterns
* Cross-version Python interoperability (2.7 vs 3.x)
* Multi-threaded socket programming
* Remote administration concepts in controlled environments

---

## 🛡️ Security Notice

This system is intended for **authorized laboratory environments only**.

* Unauthorized use on external networks is strictly prohibited
* Always isolate test environments (VMs or virtual networks)
* Ensure explicit permission before any testing activity

---

## 📄 License

This project is released under the MIT License.

