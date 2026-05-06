# 🛡️ Go-Python Defense Project

This project demonstrates a **defensive pipeline** for detecting Go-based ransomware activity through static analysis and behavioral monitoring. It combines real-time file entropy monitoring with binary analysis to detect and respond to encryption-based attacks.

---

## 📁 Folder Structure

| Directory | Purpose |
|-----------|---------|
| `scripts/go/` | Ransomware simulator written in Golang |
| `scripts/python/` | Detection scripts (Python) and configuration files |
| `victim_files/` | Monitored directory for simulated encrypted output |
| `logs/` | Placeholder for system logs |

---

## 🚀 Setup

### 1️⃣ Install Python Dependencies
```bash
pip install pefile scipy numpy
```
**Required packages**: `pefile`, `scipy`, `numpy` for file analysis and entropy calculation.

### 2️⃣ Compile Go Simulator
```bash
cd scripts/go
go build -ldflags="-s -w" -o simulator.exe simulator.go
```
This builds the stripped ransomware simulator for testing defenses.

---

## 🎯 Usage

### 1️⃣ **Baseline Testing** (Normal Activity)
Open a monitor in one terminal and run the baseline script in another:
```bash
uv run create_normal_file.py
```
✅ **Expected Result**: Monitor detects low-entropy file with no alert

### 2️⃣ **Attack Simulation** (High Entropy)
Execute the Go simulator to trigger the concurrent encryption loop:
```bash
./simulator.exe
```
⚠️ **Expected Result**: Monitor detects files with entropy near 8.0 and triggers critical alerts

### 3️⃣ **Static Analysis** (Language Identification)
Analyze the binary to identify the Go runtime signature:
```bash
uv run static_analyzer.py ../go/simulator.exe
```
🔍 **Expected Result**: Script identifies `.gopclntab` section header despite the binary being stripped

---

## ⚙️ Configuration

Modify `scripts/python/config.json` to customize:
- **Monitored directory path**
- **Entropy detection threshold** (for alerting)
- Other behavioral parameters
