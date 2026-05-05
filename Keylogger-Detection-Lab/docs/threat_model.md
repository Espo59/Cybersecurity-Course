# 🧠 Threat Model

## Threat: Input Monitoring Malware

### Description

Malicious software may attempt to monitor user input by accessing low-level input devices on Linux systems.

---

## Attack Vector

- Unauthorized process reads from `/dev/input/event*`
- Malicious kernel modules (LKM)
- Privilege escalation to gain device access

---

## Impact

- Credential theft
- Privacy violation
- Data exfiltration

---

## Detection Strategy

- Monitor processes accessing `/dev/input/`
- Inspect command-line anomalies
- Check loaded kernel modules

---

## Mitigation

- Restrict access to input devices
- Use least privilege principle
- Monitor system activity with EDR tools
- Audit kernel modules regularly

---

## Blue Team Perspective

This project demonstrates how even simple monitoring techniques can help identify suspicious behavior early in the attack lifecycle.
