# 🖧 Python MAC Address Changer

A lightweight Linux utility designed to modify the **Media Access Control (MAC) address** of a network interface using the `iproute2` suite.

This tool is intended for educational purposes in network configuration and security testing environments.

---

## 🌟 Features

* **Automatic Interface Management**
  Safely brings network interfaces down and back up during MAC modification

* **Input Validation**
  Ensures MAC address format compliance using regex validation (`XX:XX:XX:XX:XX:XX`)

* **Verification Step**
  Confirms whether the MAC address change was successfully applied

* **Robust Error Handling**
  Handles:

  * Missing root privileges
  * Invalid network interfaces
  * Missing system dependencies

---

## 🚀 Requirements

* **Operating System:** Linux
* **Dependency:** `iproute2` (`ip` command)
* **Python:** 3.6+

No external Python libraries required.

---

## 🛠️ Usage

### 1. Clone the Repository

```bash id="k8m3xp"
git clone https://github.com/yourusername/mac-changer.git
cd mac-changer
```

---

### 2. Configure the Script

Edit the following values in `change_mac.py`:

```python id="p4n7vz"
INTERFACE = "eth0"
NEW_MAC = "00:11:22:33:44:58"
```

* `INTERFACE` → Target network interface
* `NEW_MAC` → Desired MAC address

---

### 3. Run the Tool

```bash id="x2c9ql"
sudo python3 change_mac.py
```

---

## 🔍 How It Works

The script performs a standard MAC address change workflow:

1. **Scan**
   Retrieves the current MAC address of the interface

2. **Disable Interface**
   Brings the interface down using `ip link set dev down`

3. **Modify MAC Address**
   Assigns a new hardware address

4. **Re-enable Interface**
   Restores network connectivity

5. **Verify Change**
   Confirms the updated MAC address

---

## 📖 Learning Objectives

This project demonstrates:

* Network interface configuration in Linux
* Role of MAC addresses in Layer 2 communication
* Use of `iproute2` utilities for system networking
* Basic system automation with Python
* Validation and error handling in system-level scripts

---

## ⚠️ Security & Ethical Notice

This tool is intended strictly for educational and authorized testing purposes.

* MAC address modification may be restricted by network policies
* Unauthorized use on managed networks may violate rules or regulations
* Always use in controlled or personal environments

---

## 📄 License

This project is distributed under the MIT License.
