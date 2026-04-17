# SMTP Automation Tool for Metasploitable

A lightweight Python utility designed for security testing and educational purposes. This tool automates the process of sending emails via an SMTP service, specifically tailored for environments like **Metasploitable** where SMTP (Port 25) might be open and lacks strict authentication.

---

# 📌 Overview

This tool allows users to interactively construct and send emails through a target SMTP server. It is particularly useful for demonstrating:
* How the SMTP protocol works without authentication.
* Email spoofing concepts in vulnerable environments.
* Basic network communication using Python's `smtplib`.

---

# 🚀 Features

* **Interactive CLI**: Prompts for Sender, Receiver, Subject, and multi-line Body.
* **MIME Support**: Uses `MIMEMultipart` to ensure emails are correctly formatted and readable by mail clients.
* **Multi-line Input**: Supports entering complex message bodies until an EOF character is received.
* **Error Handling**: Gracefully manages connection refusals and network timeouts.

---

# 🛠 Prerequisites

* Python 3.x
* A target environment (e.g., a Metasploitable VM or a local lab) with an SMTP service running on port 25.

No external libraries are required as it uses standard Python modules (`smtplib`, `email`).

---

# 📋 Usage

### 1. Configure the Target: 

Open `mail_meta.py` and update the `target_ip` variable with the IP address of your Metasploitable machine.

   ```python
   target_ip = "192.168.23.138"  # Change this to your target IP
   ```

Run the Script:

```Bash
python3 mail_meta.py
```

Follow the Prompts:

* From: Enter the sender's address (e.g., admin@internal.lab).

* To: Enter the recipient's username (e.g., root or sys).

* Subject: Enter a clear subject line.

* Message: Type your message. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) followed by Enter to send.

---

# 🛡 Security Warning

### IMPORTANT: This tool is for educational and authorized security testing purposes only.

Never use this tool on networks or systems you do not own or have explicit permission to test.

Sending spoofed emails can be illegal and unethical depending on the context.

It is intended to be used in isolated lab environments (like Metasploitable) to understand service vulnerabilities.

---

# 📖 How it Works

The script establishes a raw TCP connection to the target on port 25. It follows the standard SMTP handshake:

Connects to the server.

Packages the user input into a MIME-compliant string.

Issues the MAIL FROM, RCPT TO, and DATA commands via smtplib.

Closes the session with QUIT.
