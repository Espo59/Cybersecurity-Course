# 🔌 Python Reverse TCP Client

A simple Python-based reverse TCP client that connects to a remote listener, receives commands, executes them on the host machine, and sends back the output.

> ⚠️ **Disclaimer**: This project is for educational purposes and authorized security testing only. Do not use it on systems without explicit permission.

---

## 📌 Features

* Reverse TCP connection to a remote host
* Remote command execution
* Captures both `stdout` and `stderr`
* Persistent command loop
* Silent error handling

---

## 🛠️ Requirements

* Python 3.x
* A listener (e.g., Netcat or Metasploit) running on the remote machine

---

## ⚙️ Configuration

Before running the script, update the following variables:

```python
KALI_IP = "192.168.23.137"
KALI_PORT = 443
```

* `KALI_IP`: IP address of your listener machine
* `KALI_PORT`: Port your listener is using

---

## 🚀 Usage

### 1. Start a Listener

#### Using Netcat:

```bash
nc -lvnp 443
```

#### Using Metasploit:

Make sure `LHOST` and `LPORT` match the script configuration.

---

### 2. Run the Script

```bash
python3 reverse_client.py
```

---

### 3. Execute Commands

Once the connection is established, you can execute commands remotely from your listener:

```bash
whoami
pwd
ls
```

To terminate the session:

```bash
exit
```

---

## 📂 Project Structure

```
.
├── reverse_client.py
└── README.md
```

---

## ⚠️ Security Notice

This script executes shell commands with `shell=True`, which allows:

* Command chaining
* Pipes
* Execution of system-level commands

This is **dangerous** if misused. Only run in controlled environments.

---

## 📖 How It Works

1. Creates a TCP socket connection to the configured host
2. Waits for incoming commands
3. Executes commands using `subprocess.Popen`
4. Sends back the combined output (`stdout + stderr`)
5. Repeats until `exit` is received

---

## 🧪 Educational Purpose

This project can help you understand:

* Networking with Python sockets
* Remote command execution
* Basic post-exploitation concepts
* How reverse shells work under the hood

---

## ❗ Legal Disclaimer

You are responsible for your actions. Misuse of this software may violate laws and regulations. Use only in:

* Lab environments
* Capture The Flag (CTF) challenges
* Authorized penetration testing engagements

---

## 📄 License

This project is released under the MIT License.
