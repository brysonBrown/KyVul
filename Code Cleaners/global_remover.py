import json
import re

def remove_global_keyword(code):
    """Remove 'global' when used as a keyword in C/C++ code."""
    lines = code.splitlines()
    fixed_lines = []
    modified = False

    for line in lines:
        # Check if 'global' appears as a standalone keyword before a type or identifier
        # e.g., "global int x;" or "global struct data_packet *packet;"
        if re.match(r'^\s*global\s+(struct|int|char|float|double|void|[A-Za-z_]\w*\s*\*?)\s*[A-Za-z_]\w*', line):
            # Replace 'global' followed by whitespace with nothing
            fixed_line = re.sub(r'^\s*global\s+', '', line).strip()
            fixed_lines.append(fixed_line)
            modified = True
        else:
            # Keep the line unchanged if 'global' isn't a keyword (e.g., in a variable name or comment)
            fixed_lines.append(line)

    return '\n'.join(fixed_lines), modified

def parse_and_fix_json(input_file, output_file):
    """Parse JSON and remove 'global' keyword from code entries."""
    # Load JSON
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error loading JSON: {e}")
        return

    if not isinstance(data, list):
        print("Error: JSON must be a list of objects.")
        return

    total_entries = len(data)
    print(f"Processing {total_entries} entries...")

    fixed_count = 0

    # Process each entry
    for i, item in enumerate(data):
        if 'code' not in item:
            continue

        original_code = item['code']
        fixed_code, was_modified = remove_global_keyword(original_code)

        if was_modified:
            fixed_count += 1
            item['code'] = fixed_code
            print(f"Fixed entry {i}: Removed 'global' keyword.")
            # Optional: Uncomment to see before/after
            # print(f"Before:\n{original_code}\nAfter:\n{fixed_code}\n")

    # Save the fixed JSON
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Processed {total_entries} entries.")
    print(f"Fixed {fixed_count} instances of 'global' keyword.")
    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    input_file = '/home/bryson/research/research3.0/fixed_nonvuln.json'
    output_file = '/home/bryson/research/research3.0/fixed_nonvuln.json'
    parse_and_fix_json(input_file, output_file)
    input_file = '/home/bryson/research/research3.0/fixed_vuln.json'
    output_file = '/home/bryson/research/research3.0/fixed_vuln.json'
    parse_and_fix_json(input_file, output_file)