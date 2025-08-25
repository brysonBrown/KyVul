import json
import os

def clean_code(code):
    # Remove erroneous trailing patterns
    patterns = ['"\n}\n', '}"\n}\n', '\n"\n}\n']
    for pattern in patterns:
        if code.endswith(pattern):
            code = code[:-len(pattern)]
            break
    # Find the last line with only '}'
    lines = code.split('\n')
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip() == '}':
            cleaned_lines = lines[:i + 1]
            return '\n'.join(cleaned_lines) + '\n'
    print("Warning: No closing '}' found on its own line.")
    return code.rstrip() + '\n'

def fix_newlines_in_code(code):
    """Replace newlines inside C string literals with \\n."""
    result = []
    in_string = False
    i = 0
    while i < len(code):
        char = code[i]
        # Toggle in_string on unescaped quotation marks
        if char == '"' and (i == 0 or code[i-1] != '\\' or (i > 1 and code[i-2] == '\\')):
            in_string = not in_string
            result.append(char)
        # Replace newline with \\n inside strings
        elif char == '\n' and in_string:
            result.append('\\n')
        else:
            result.append(char)
        i += 1
    return ''.join(result)

def fix_json_file(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Input JSON must be an array of objects.")

    fixed_data = []
    problematic_count = 0

    for i, item in enumerate(data):
        if 'code' in item:
            original_code = item['code']
            # Step 1: Clean trailing issues
            cleaned_code = clean_code(original_code)
            # Step 2: Fix newlines in string literals
            fixed_code = fix_newlines_in_code(cleaned_code)
            # Check for remaining issues (e.g., extra characters after last '}')
            lines = fixed_code.split('\n')
            last_brace_idx = -1
            for j in range(len(lines) - 1, -1, -1):
                if lines[j].strip() == '}':
                    last_brace_idx = j
                    break
            if last_brace_idx != -1 and any(line.strip() for line in lines[last_brace_idx + 1:]):
                problematic_count += 1
                print(f"Entry {i}: ...{fixed_code[-10:]}")
            item['code'] = fixed_code
            fixed_data.append(item)

    with open(output_file, 'w') as file:
        json.dump(fixed_data, file, indent=4)

    print(f"Processed {len(fixed_data)} JSON objects.")
    print(f"Found {problematic_count} problematic entries after cleaning.")

# Run the script
if __name__ == "__main__":
    input_file = '/home/bryson/research/research3.0/vuln_cleaned.json'  # Your input file
    output_file = '/home/bryson/research/research3.0/fixed_vuln.json'   # Your output file
    fix_json_file(input_file, output_file)