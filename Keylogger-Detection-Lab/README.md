# 🛡️ Linux Input Monitoring Detection Lab

![Linux](https://img.shields.io/badge/Platform-Linux-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![Security](https://img.shields.io/badge/Focus-Blue%20Team-orange)

---

## 🎯 Objective

This project demonstrates how suspicious input monitoring activity can be identified on Linux systems from a defensive (Blue Team) perspective.

The goal is to simulate detection techniques for behaviors commonly associated with keylogging, focusing on process inspection, device access monitoring, and basic kernel-level visibility.

---

## 🔍 Key Features

* Process inspection using `psutil`
* Detection of processes accessing `/dev/input/` devices
* Command-line anomaly detection
* Kernel module inspection via `/proc/modules`
* User-space and kernel-space visibility

---

## 🧠 Detection Logic

The script identifies suspicious behavior based on:

* Processes interacting with `/dev/input/event*`
* Suspicious process names or command-line arguments
* Unexpected background processes
* Presence of suspicious kernel modules

---

## ⚙️ Requirements

* Linux Operating System
* Python 3.x
* Root privileges (recommended for full visibility)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the script:

```bash
sudo python3 detector.py
```

If not executed as root, the script will still run but may have limited visibility.

---

## 📊 Example Output

```text
PID        | NAME                 | STATUS
--------------------------------------------------
1234       | suspicious_process   | [!] SOSPETTO
```

---

## 🛡️ Security Considerations

This tool highlights how input monitoring activity can be detected, but it also demonstrates limitations:

* Kernel-level rootkits may evade detection
* False positives are possible
* Advanced malware may hide process artifacts

---

## 📚 Educational Value

This project was developed to explore:

* Linux process inspection techniques
* Device-level monitoring (`/dev/input`)
* Behavioral detection vs signature-based detection
* Basic threat modeling for input monitoring attacks

---

## ⚠️ Disclaimer

This project is intended for **educational and defensive cybersecurity purposes only**.

It does not implement any offensive functionality and should only be used in controlled environments.

---

## 📂 Project Structure

```
Keylogger-Detection-Lab/
├── detector.py
├── requirements.txt
├── README.md
└── docs/
    ├── analysis.md
    └── threat_model.md

```

---

## 🚀 Future Improvements

* JSON output export for SIEM integration
* Real-time monitoring (daemon mode)
* Integration with system logs (syslog)
* Alerting system (email / logging)
* Improved anomaly detection logic

---

## 🤝 Contributing

This project is part of a personal cybersecurity learning path. Suggestions and improvements are welcome.

---
