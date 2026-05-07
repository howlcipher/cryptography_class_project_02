import pefile
import sys
import os

def analyze_binary(file_path):
    """
    Analyze a PE (Portable Executable) binary file for signs of Go compilation.
    Looks for specific sections that are characteristic of Go binaries.
    """
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    try:
        pe = pefile.PE(file_path)
        print(f"Analyzing Headers for {file_path}...\n")
        
        go_artifact_found = False
        for section in pe.sections:
            section_name = section.Name.decode('utf-8', errors='ignore').strip('\x00')
            print(f"Section Found: {section_name}")
            # Check for Go-specific sections
            if ".gopclntab" in section_name or ".data" in section_name:
                go_artifact_found = True
                
        print("\n--- Analysis Complete ---")
        if go_artifact_found:
            print("[ALERT] Go runtime artifacts detected. Binary likely compiled with Go.")
    except Exception as e:
        print(f"Error parsing executable: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python static_analyzer.py <path_to_executable>")
    else:
        analyze_binary(sys.argv[1])