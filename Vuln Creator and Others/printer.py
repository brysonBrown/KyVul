import json
import os

def print_entries_2439_and_3304(json_file_path):
    print(f"Attempting to open file: {json_file_path}")
    
    # Check if file exists
    if not os.path.exists(json_file_path):
        print(f"Error: File {json_file_path} does not exist!")
        return

    # Load JSON
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Verify data is a list
    if not isinstance(data, list):
        print("Error: JSON data is not a list!")
        return

    # Check length
    total_entries = len(data)
    print(f"Loaded JSON data. Total entries: {total_entries}")
    
    target_index1 = 9969  # 2439th entry (0-based index)
    target_index2 = 9891  # 3304th entry (0-based index)
    
    # Check if both indices are accessible
    if total_entries <= target_index1:
        print(f"Error: File has only {total_entries} entries, cannot access entry 2439 (index {target_index1})")
        return
    if total_entries <= target_index2:
        print(f"Error: File has only {total_entries} entries, cannot access entry 3304 (index {target_index2})")
        return

    # Print the 2439th entry
    entry1 = data[target_index1]
    print(f"\nEntry 9969 (index {target_index1}):")
    print(json.dumps(entry1, indent=4, ensure_ascii=False))

    # Print the 3304th entry
    entry2 = data[target_index2]
    print(f"\nEntry 9891 (index {target_index2}):")
    print(json.dumps(entry2, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    json_file_path = 'fixed_vuln.json'
    print_entries_2439_and_3304(json_file_path)