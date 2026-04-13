# ICMP Forensic & Protocol Analysis Tool
This Python script is a specialized network diagnostic tool that performs Deep Packet Inspection (DPI) on ICMP traffic. It is designed to help cybersecurity students and network administrators understand the exact structure of the IPv4 and ICMP headers.

---

# 🛠 Features
- **Manual Packet Crafting:** Uses Scapy to bypass the OS stack and build raw IP/ICMP layers.

- **Forensic Breakdown:** Instead of a simple "reply received" message, the script decomposes the response and explains every field:

- **IP Layer:** Version, IHL, TOS/DSCP, Fragmentation Flags (DF/MF), TTL, and Checksum.

- **ICMP Layer:** Type (Request/Reply), Code, ID, and Sequence numbers.

- **Payload Inspection:** Extracts and decodes the data payload, providing both a text preview and a hex sample.

- **Binary Hexdump:** Displays the complete packet in hexadecimal format, allowing for bit-level analysis of the network traffic.

---

# 🧪 Use Cases for Cybersecurity Students
**Header Analysis:** Learn how flags like Don't Fragment (DF) behave in a real exchange.

**OS Fingerprinting:** Observe how different Operating Systems set default TTL values or IP ID patterns in their responses.

**Security Auditing:** Test if network devices (Firewalls/IDPS) correctly handle spoofed packets or specific ICMP types.

**Learning Hexadecimal Representation:** Use the final hexdump to map the human-readable explanation back to the raw binary data.

---

# 🚀 How to Run
**Install Scapy:**

Bash
pip install scapy

**Configure:** 
Update SRC_IP, DST_IP, and IFACE in the script.

**Execute with Root Privileges:**

Bash
sudo python3 ping_spoofed_explain.py

---

# ⚠️ Important Note on Spoofing
When spoofing the source IP, the script will likely show a timeout. This is a successful result from a technical standpoint: it confirms the target sent the reply to the spoofed address instead of yours. Use a network sniffer (like Wireshark) on the target or spoofed machine to confirm the packet arrival.

---

# 📜 License
Distributed under the MIT License.
