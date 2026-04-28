# 🌐 MitM Security Automation Lab (Bettercap Orchestration Tool)

This project is a **Python-based automation framework for network security testing using Bettercap**, designed to study how Man-in-the-Middle (MitM) techniques interact with modern web security mechanisms.

It focuses on **traffic interception, protocol downgrade analysis, and defensive security evaluation** in controlled environments.

---

## 🔍 How It Works

The tool automates Bettercap workflows to simulate and analyze different layers of network interception.

---

### 📡 Network Positioning (ARP Simulation)

* Establishes MitM positioning via ARP cache manipulation
* Redirects traffic between victim and gateway through the test machine
* Enables observation of raw network traffic flows

---

### 🔓 Protocol Downgrade Analysis (SSL/TLS Behavior)

* Simulates HTTP/HTTPS downgrade scenarios
* Observes how browsers and services respond to insecure fallback conditions
* Helps analyze encryption enforcement mechanisms

---

### 🛡 HSTS Policy Evaluation

* Interacts with HSTS (HTTP Strict Transport Security) behavior
* Studies how browsers enforce or bypass security policies in controlled tests
* Provides insight into modern web security protections

---

### 📊 Traffic Inspection

Once traffic is routed through the test environment:

* Captures HTTP request metadata (URLs, headers)
* Observes session-level behavior
* Analyzes protocol transitions (HTTPS → HTTP in lab conditions)

---

## 🛠 Features

### ⚙️ Automated Bettercap Orchestration

* Converts manual Bettercap interaction into scripted execution
* Simplifies multi-step network testing workflows

---

### 🧠 HSTS Behavior Testing Support

* Integrates caplet-based workflows for security analysis
* Enables evaluation of browser-level enforcement mechanisms

---

### 🧹 Noise Filtering

* Removes irrelevant system-level events
* Focuses logs on meaningful network traffic

---

### 🖥 Virtual Lab Stability Handling

* Filters virtual machine-generated background traffic
* Improves reproducibility in lab environments

---

### 🧼 Safe Termination Handling

* Ensures clean shutdown of Bettercap modules
* Prevents residual network state after execution

---

## 🧪 Learning Objectives

This project demonstrates:

* ARP-based traffic redirection concepts
* TLS/HTTPS enforcement and downgrade resistance
* HSTS security policy mechanisms
* Network traffic inspection methodologies
* Security tool automation using Python (`subprocess`)
* Behavior of web clients under manipulated network conditions

---

## 🚀 Requirements

* Linux (Kali Linux / Parrot OS recommended)
* Bettercap v2.x
* HSTS-related caplets installed
* Root privileges (required for packet-level operations)

---

## ▶️ Usage

### 1. Update Bettercap environment

```bash id="k7m3vp"
sudo bettercap -eval "caplets.update; q"
```

---

### 2. Configure Script

Set:

* `TARGET_IP`
* `NETWORK_INTERFACE`

---

### 3. Run Automation Tool

```bash id="x4n8ql"
sudo python3 mitm_automator.py
```

---

## 📖 Security Learning Outcomes

This project is designed to help understand:

* Network routing manipulation in controlled environments
* Web security enforcement mechanisms (HTTPS, HSTS)
* Limitations of encryption under misconfigured trust assumptions
* Role of interception in security auditing workflows
* Defensive implications of traffic inspection techniques

---

## 🛡 Security & Ethical Notice

This project is strictly intended for **authorized cybersecurity research and educational use only**.

* Do not use on production or unauthorized networks
* Always operate within isolated lab environments
* Interception of network traffic without permission is illegal

---

## 📄 License

This project is released under the MIT License.
