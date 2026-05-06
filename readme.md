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
1. **Dynamic Monitoring**:
   Open a terminal and start the monitor from `scripts/python`:
   ```bash
   cd scripts/python
   python dynamic_monitor.py
   ```

2. **Execute Simulation**:
   Open a separate terminal and run the simulator from `scripts/go`:
   ```bash
   cd scripts/go
   ./simulator.exe
   ```

   The simulator now writes encrypted files into the repository root `victim_files/` directory, which is the same location monitored by `dynamic_monitor.py`.

3. **Static Analysis**:
   From `scripts/python`, analyze the compiled binary to inspect Go runtime section artifacts:
   ```bash
   cd scripts/python
   python static_analyzer.py ../go/simulator.exe
   ```

## Configuration
Adjust `scripts/python/config.json` to change the monitored directory or the entropy detection threshold.
