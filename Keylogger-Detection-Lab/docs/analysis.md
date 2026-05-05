# 🔍 Behavioral Analysis

## Overview

This script performs a basic behavioral inspection of a Linux system to identify suspicious processes that may be interacting with input devices.

Instead of relying on signatures, the detection is based on runtime behavior.

---

## Detection Techniques

### 1. Process Inspection

The script iterates through running processes using the `psutil` library and analyzes:

- Process name
- Command-line arguments

Processes containing suspicious keywords such as "input" are flagged.

---

### 2. Device Access Monitoring

The script checks open file descriptors for each process.

If a process is accessing:

`/dev/input/`


it is considered suspicious, as this is where keyboard and input events are handled.

---

### 3. Kernel Module Inspection

The script reads:

`/proc/modules`


to detect potentially malicious kernel modules.

---

## Limitations

- Root privileges are required for full visibility
- Kernel-level rootkits may hide themselves
- False positives may occur (legitimate input-related services)

---

## Key Insight

Monitoring behavior (what a process does) is often more effective than relying only on known malware signatures.
