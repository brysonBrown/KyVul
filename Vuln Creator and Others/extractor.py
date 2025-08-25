import json
import os

# Load the stackVul.json file
with open('vuln.json', 'r') as file:
    data = json.load(file)

# Create a directory for the code files
os.makedirs('code_files', exist_ok=True)

# Save each code segment as a separate .c file
for i, item in enumerate(data):
    if 'code' in item:
        file_path = os.path.join('code_files', f'code_{i+1}.c')
        with open(file_path, 'w') as code_file:
            code_file.write(item['code'])

print("Code segments saved to 'code_files' directory.")
