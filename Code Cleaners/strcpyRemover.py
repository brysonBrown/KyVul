import json
import re

# Function to replace strcpy with strncpy and append len({dest})
def replace_strcpy_with_strncpy(code):
    # Regex pattern to match strcpy(dest, src)
    pattern = re.compile(r'strcpy\(([^,]+),\s*([^\)]+)\);')

    def replacement(match):
        dest = match.group(1).strip()  # The destination part (dest)
        src = match.group(2).strip()   # The source part (src)

        # Replace strcpy with strncpy and add len(dest)
        return f'strncpy({dest}, {src}, len({dest}));'

    # Apply the regex replacement to the code
    return re.sub(pattern, replacement, code)

# Function to replace scanf with fgets
def replace_scanf_with_fgets(code):
    # Regex pattern to match scanf("%s", <variable>)
    pattern = re.compile(r'scanf\("%s",\s*([^\)]+)\);')

    def replacement(match):
        variable = match.group(1).strip()  # The variable part

        # Replace scanf with fgets and add sizeof(variable)
        return f'fgets({variable}, "%s", sizeof({variable}));'

    # Apply the regex replacement to the code
    return re.sub(pattern, replacement, code)

# Function to replace sprintf with snprintf
def replace_sprintf_with_snprintf(code):
    # Regex pattern to match sprintf(dest, format, args...)
    pattern = re.compile(r'sprintf\(([^,]+),\s*([^\)]+)\);')

    def replacement(match):
        dest = match.group(1).strip()  # The destination part (dest)
        format_string = match.group(2).strip()  # The format string (and arguments)

        # Replace sprintf with snprintf and add sizeof(dest)
        return f'snprintf({dest}, sizeof({dest}), {format_string});'

    # Apply the regex replacement to the code
    return re.sub(pattern, replacement, code)

# Function to process the JSON file and update the code field
def process_json_file(input_file, output_file):
    # Read the JSON data from the file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Process each object in the JSON array
    for item in data:
        if 'code' in item:
            # Replace strcpy with strncpy in the code field
            item['code'] = replace_strcpy_with_strncpy(item['code'])
            # Replace scanf with fgets in the code field
            item['code'] = replace_scanf_with_fgets(item['code'])
            # Replace sprintf with snprintf in the code field
            item['code'] = replace_sprintf_with_snprintf(item['code'])

    # Write the modified JSON back to a new file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
input_file = 'stackFixedNonVuln.json'  # Your input JSON file path
output_file = 'stackFixedNonVuln2.json'  # Output file where updated JSON will be saved

# Process the file
process_json_file(input_file, output_file)

print(f"Updated JSON saved to {output_file}")
