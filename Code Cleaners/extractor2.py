import json
import os

def extract_json_code(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    os.makedirs('code_files', exist_ok=True)
    for i, item in enumerate(data):
        if 'code' in item:
            code = item['code']
            print(f"Extracting entry {i+1}: {repr(code[:50])}...")
            with open(f'code_files/code_{i+1}.c', 'w', newline='') as f:
                f.write(code)
    print(f"Extracted {len(data)} files to 'code_files/'.")

if __name__ == "__main__":
    extract_json_code('/home/bryson/research/research3.0/fixed_nonvuln.json')