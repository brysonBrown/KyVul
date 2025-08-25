import json
import re

# List of vulnerability categories
vulns = [
    "out-of-bounds access",
]

def fix_code_string(code):
    """Fix irregularities in the code string by correcting backslashes."""
    
    # Handle sequences where two or more slashes are followed by special characters
    # Match two or more backslashes followed by n, ', ", or 0
    fixed_code = re.sub(r'\\{2,}(?=[n\'"0])', lambda m: '\\', code)
    
    # Handle sequences where two or more slashes are not followed by the special characters
    # Match two or more backslashes not followed by n, ', ", or 0, and reduce to two slashes
    fixed_code = re.sub(r'\\{2,}(?![n\'"0])', '\\\\', fixed_code)

    # Handle specific escape sequences
    fixed_code = fixed_code.replace("\\n", "\n").replace("\\\"", "\"").replace("\\'", "\'")

    return fixed_code

def extract_code_from_text(file_path, vuln):
    """Extract code samples from a text file and assign categories."""
    with open(file_path, 'r') as file:
        data = file.read()  # Read the entire file content

    # Step 1: Split the file content on the word 'json'
    tokens = data.split("json")

    # Step 2: Extract code samples from each token, starting after `"code": "` or `"code": [`
    code_samples = []
    for i, token in enumerate(tokens[1:]):  # Skip the first token as it's before the first "code": field
        # Find where the code starts after `"code": "` or `"code": [`
        start_index = token.find('"code": [') + len('"code": [')
        if start_index == -1:
            start_index = token.find('"code": "') + len('"code": "')

        # Find where the code ends at the closing ``` or closing quote
        end_index = token.find("```")
        if end_index == -1:
            end_index = token.find('"', start_index)
        
        if start_index != -1 and end_index != -1:
            # Extract the code sample from the start index to the end index
            code_sample = token[start_index:end_index].strip()

            # Fix the escape sequences and backslashes
            code_sample = fix_code_string(code_sample)

            # Calculate category index using modulo to cycle through categories
            category = "use after free"
            
            # Add the cleaned code sample as a dictionary with "code", "category", and "vulnerable"
            code_samples.append({
                "code": code_sample,
                "category": category,
                "vulnerable": vuln  # Add the "vulnerable" field with value 1
            })

    # Return the list of dictionaries with code samples and their categories
    return code_samples

def save_fixed_data(input_file, output_file, vuln):
    """Extract the fixed code samples with categories and save them to a JSON file."""
    fixed_data = extract_code_from_text(input_file, vuln)

    # Save the cleaned and categorized data into a new JSON file
    with open(output_file, 'w') as f:
        json.dump(fixed_data, f, indent=4)

# Test the function with a file path
inputV_file = 'data.json'  
outputV_file = 'fixed.json' 

v = 1
nv = 0

save_fixed_data(inputV_file, outputV_file, v)
print(f"Fixed data has been saved to {outputV_file}.")
