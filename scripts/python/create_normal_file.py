import os
import json

# Load configuration file
config_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_path, "r") as f:
    config = json.load(f)

# Resolve victim directory path
VICTIM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), config["monitor_dir"]))

def create_baseline_file():
    # Create the victim directory if needed
    if not os.path.exists(VICTIM_DIR):
        os.makedirs(VICTIM_DIR)
        
    file_path = os.path.join(VICTIM_DIR, "normal.txt")
    
    # Normal low-entropy content for comparison
    content = (
        "This is a standard baseline document for the cryptography project. "
        "It contains normal English prose with predictable patterns and low randomness. "
        "The goal is to demonstrate that the detection script recognizes this as safe data."
    )
    
    try:
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Successfully created baseline file at: {file_path}")
    except Exception as e:
        print(f"Error creating file: {e}")

if __name__ == "__main__":
    # Run when executed directly
    create_baseline_file()