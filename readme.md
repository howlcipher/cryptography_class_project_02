# Go-Python Defense Project

This project demonstrates a defensive pipeline for detecting Go-based ransomware activity through static analysis and behavioral monitoring.

## Folder Structure
- `scripts/go/`: Ransomware simulator (Golang).
- `scripts/python/`: Detection scripts (Python) and configuration.
- `victim_files/`: Monitored target directory for simulated encrypted output.
- `logs/`: Placeholder for system logs.

## Setup
1. **Python Dependencies**:
   ```bash
   pip install pefile scipy numpy
   ```
2. **Compile Go Simulator**:
   ```bash
   cd scripts/go
   go build -ldflags="-s -w" -o simulator.exe simulator.go
   ```

## Usage
Step 1: Baseline Testing (Normal Activity)
Open your monitor in one terminal and run the baseline script in another:
uv run create_normal_file.py
Expected Result: Monitor detects the file with low entropy and triggers no alert.

Step 2: Attack Simulation (High Entropy)
Execute the Go simulator to trigger the concurrent encryption loop:
./simulator.exe
Expected Result: Monitor detects multiple files with entropy near 8.0 and triggers critical alerts.

Step 3: Language Identification (Static Analysis)
Analyze the binary to identify the Go runtime:
uv run static_analyzer.py ../go/simulator.exe
Expected Result: Script identifies the .gopclntab section header despite the binary being stripped.

## Configuration
Adjust `scripts/python/config.json` to change the monitored directory or the entropy detection threshold.
