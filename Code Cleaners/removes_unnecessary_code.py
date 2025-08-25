import json

# Input and output file paths
# Removes the "code" from the beginning of each of the json's
input_file = "/home/bryson/research/research3.0/vuln.json"  # The merged file from earlier
output_file = "/home/bryson/research/research3.0/vuln_cleaned.json"

# Load the JSON data
with open(input_file, 'r') as f:
    data = json.load(f)  # Expecting an array of JSON objects

# Process each object to clean the 'code' field
for obj in data:
    if "code" in obj:
        # Remove the '"code": "' prefix from the code field
        original_code = obj["code"]
        if original_code.startswith('"code": "'):
            # Strip the prefix and keep the rest, removing the trailing quote if present
            cleaned_code = original_code[len('"code": "'):]
            if cleaned_code.endswith('"'):
                cleaned_code = cleaned_code[:-1]
            obj["code"] = cleaned_code

# Save the modified data to a new file
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)  # Use indent=4 for readability

print(f"Cleaned JSON data saved to {output_file}")