# Scapy IP Packet Inspector
A fundamental Python utility designed to demonstrate the internal structure of an Internet Protocol (IP) packet using the Scapy library.
This tool is purely analytical; it creates and inspects packet objects in memory without transmitting any data over the network.

---

# 🔍 How It Works
Scapy treats network protocols as Python objects, allowing for granular inspection of header fields that are usually handled automatically 
by the operating system's TCP/IP stack.

- **Layer Instantiation:** The script initializes an IP class instance, which represents the Layer 3 header of the OSI model.

- **Field Mapping:** By setting the dst (destination) parameter, the script overrides the default loopback address while leaving other critical fields (like TTL, Flags, and Checksum) at their default or uncalculated states.

- **Introspection (ls):** It utilizes Scapy's ls() (list) function to perform a deep inspection of the object, revealing the underlying structure of the IP header.

- **Summary Generation:** It demonstrates how Scapy provides human-readable summaries of complex binary structures.

---

# 🛠 Features
**Zero-Packet Transmission:** Safe to run in any environment as it performs no network I/O or raw socket operations.

**Header Introspection:** Provides a clear view of all 14 fields of the IPv4 header (Version, IHL, TOS, Len, ID, etc.).

**Field Access Demonstration:** Shows how to programmatically access and manipulate specific packet attributes.

**Lightweight:** Minimal code footprint, focusing strictly on the educational aspect of Scapy's object-oriented approach.

---

# 🧪 Educational Objectives
This project was developed to explore:

The anatomy of an IPv4 Header as defined in RFC 791.

How Scapy abstracts complex network protocols into Pythonic objects.

The difference between a default protocol state and a customized packet.

Basic debugging techniques for network scripts using the ls() and summary() methods.

---

# 🚀 Usage
*Prerequisites:*
Python 3.x

*Scapy library installed:*

Bash
pip install scapy

*Execution:*
Since this script does not interact with the network interface, it does not require root/sudo privileges.

Bash
python3 ip_inspector.py

---

# 📋 Example Output
The script will output the field breakdown of the IP layer, including:

version: 4 (IPv4)

ihl: Header length

ttl: Time to Live

proto: Protocol (default: hopopt)

dst: Your specified destination IP

---

# ⚠️ Disclaimer
FOR EDUCATIONAL PURPOSES ONLY. This tool is intended for learning the basics of packet construction and the Scapy library. It is a foundational script for students and security researchers starting with network programming.
