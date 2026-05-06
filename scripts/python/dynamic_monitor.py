import os
import time
import json
import numpy as np
from scipy.stats import entropy

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_path, "r") as f:
    config = json.load(f)

MONITOR_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), config["monitor_dir"]))
ENTROPY_THRESHOLD = config["entropy_threshold"]

def calculate_shannon_entropy(file_path):
    try:
        with open(file_path, 'rb') as f:
            byte_arr = list(f.read())
            
        if not byte_arr:
            return 0.0
            
        # Calculate the frequency of each byte (0 to 255)
        counts = np.bincount(byte_arr, minlength=256)
        probabilities = counts / len(byte_arr)
        
        # Calculate entropy using SciPy base 2
        file_entropy = entropy(probabilities, base=2)
        return file_entropy
    except Exception:
        return 0.0

def monitor_directory():
    print(f"Monitoring directory: {MONITOR_DIR}")
    seen_files = set(os.listdir(MONITOR_DIR)) if os.path.exists(MONITOR_DIR) else set()
    
    if not os.path.exists(MONITOR_DIR):
        os.makedirs(MONITOR_DIR)

    while True:
        current_files = set(os.listdir(MONITOR_DIR))
        new_files = current_files - seen_files
        
        for file in new_files:
            file_path = os.path.join(MONITOR_DIR, file)
            # Short sleep to allow write to complete
            time.sleep(0.1) 
            
            ent_value = calculate_shannon_entropy(file_path)
            print(f"Analyzed {file} | Entropy: {ent_value:.4f}")
            
            if ent_value >= ENTROPY_THRESHOLD:
                print(f"[CRITICAL ALERT] High entropy detected in {file}!")
                
        seen_files = current_files
        time.sleep(1)

if __name__ == "__main__":
    monitor_directory()