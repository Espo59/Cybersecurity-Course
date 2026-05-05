# 🛰️ SOC Analysis Notes

## Context

This tool simulates a basic endpoint detection scenario where suspicious input monitoring activity is investigated on a Linux system.

---

## Detection Scenario

A security analyst suspects that a system may be compromised by input monitoring malware.

The goal is to identify abnormal behavior related to device-level input access.

---

## Investigation Steps

1. Enumerate running processes
2. Inspect command-line arguments
3. Check open file descriptors
4. Identify access to `/dev/input/`
5. Review loaded kernel modules

---

## Indicators of Suspicious Activity

- Processes accessing `/dev/input/event*`
- Unusual process names or arguments
- Background processes with elevated privileges
- Unknown or suspicious kernel modules

---

## Analyst Interpretation

Access to `/dev/input/` is not inherently malicious.

However, it becomes suspicious when:

- The process is not a known system component
- The behavior is continuous or hidden
- The process originates from an untrusted source

---

## Response Actions

If suspicious activity is confirmed:

- Identify and terminate the process
- Investigate process origin (binary path, hash)
- Check persistence mechanisms
- Perform full system scan

---

## Key Takeaway

Behavior-based detection is a critical component of modern endpoint security.

Even simple indicators can provide early warning signals of compromise.
