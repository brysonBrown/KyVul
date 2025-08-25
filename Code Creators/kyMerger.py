import json

def load_json_file(file_path):
    """Load a JSON file and return its contents."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError(f"{file_path} must contain a list of objects")
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return []
    except json.JSONDecodeError:
        print(f"Error: File {file_path} is not a valid JSON file")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []

def zipper_merge(list1, list2):
    """Merge two lists in a zipper pattern: list1, list2, list1, list2, etc."""
    merged = []
    max_length = max(len(list1), len(list2))
    
    for i in range(max_length):
        # Add from list1 if available
        if i < len(list1):
            merged.append(list1[i])
        # Add from list2 if available
        if i < len(list2):
            merged.append(list2[i])
    
    return merged

def save_json_file(data, output_file):
    """Save the merged data to a JSON file."""
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Merged data saved to {output_file}")

def merge_json_files(file1_path, file2_path, output_path):
    """Merge two JSON files into one with a zipper pattern."""
    # Load the JSON files
    file1_data = load_json_file(file1_path)
    file2_data = load_json_file(file2_path)
    
    # Check if either file failed to load
    if not file1_data and not file2_data:
        print("Both files failed to load. Exiting.")
        return
    
    # Merge the data in a zipper pattern
    merged_data = zipper_merge(file1_data, file2_data)
    
    # Save the merged data
    save_json_file(merged_data, output_path)

# File paths
file1_path = "fixed_vuln.json"
file2_path = "fixed_nonvuln.json"
output_path = "kyVul.json"

# Run the merge
merge_json_files(file1_path, file2_path, output_path)