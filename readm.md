# Go-Python Defense Project

This project demonstrates a defensive pipeline for detecting Go-based ransomware activity through static analysis and behavioral monitoring.

## Folder Structure
- `scripts/go/`: Ransomware simulator (Golang).
- `scripts/python/`: Detection scripts (Python) and configuration.
- `victim_files/`: Target directory for simulated encryption/random file creation.
- `logs/`: Placeholder for system logs.

## Setup
1. **Python Dependencies**:
   ```bash
   pip install pefile scipy numpy
   ```
2. **Compile Go Simulator**:
   ```bash
   cd scripts/go
   go build -ldflags="-s -w" simulator.go
   ```

## Usage
1. **Dynamic Monitoring**:
   Open a terminal and start the monitor:
   ```bash
   cd scripts/python
   python dynamic_monitor.py
   ```
2. **Execute Simulation**:
   Open a separate terminal and run the compiled binary:
   ```bash
   cd scripts/go
   ./simulator
   ```
3. **Static Analysis**:
   Analyze the generated binary to see Go-specific section headers:
   ```bash
   cd scripts/python
   python static_analyzer.py ../go/simulator
   ```

## Configuration
Adjust `scripts/python/config.json` to change the target directory or the entropy sensitivity threshold.
