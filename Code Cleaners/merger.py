import json

# List of input JSON filenames
vuln_files = [
    "/home/bryson/research/research3.0/Use After Free/useFixedVuln.json",
    "/home/bryson/research/research3.0/Command Injection/cmdFixedVuln.json",
    "/home/bryson/research/research3.0/Double Free/dbFixedVuln.json",
    "/home/bryson/research/research3.0/Heap Overflow/heapFixedVuln.json",
    "/home/bryson/research/research3.0/Integer Overflow/intFixedVuln.json",
    "/home/bryson/research/research3.0/Memory Leak/mlFixedVuln.json",
    "/home/bryson/research/research3.0/Out of Bounds Access/obaFixedVuln.json",
    "/home/bryson/research/research3.0/Race Condition/raceFixedVuln.json",
    "/home/bryson/research/research3.0/Stack Overflow/stackFixedVuln.json"
]

nonvuln_files = [
    "/home/bryson/research/research3.0/Use After Free/useFixedNonVuln.json",
    "/home/bryson/research/research3.0/Command Injection/cmdFixedNonVuln.json",
    "/home/bryson/research/research3.0/Double Free/dbFixedNonVuln.json",
    "/home/bryson/research/research3.0/Heap Overflow/heapFixedNonVuln.json",
    "/home/bryson/research/research3.0/Integer Overflow/intFixedNonVuln.json",
    "/home/bryson/research/research3.0/Memory Leak/mlFixedNonVuln.json",
    "/home/bryson/research/research3.0/Out of Bounds Access/obaFixedNonVuln.json",
    "/home/bryson/research/research3.0/Race Condition/raceFixedNonVuln.json",
    "/home/bryson/research/research3.0/Stack Overflow/stackFixedNonVuln.json"
]
# Initialize an empty list to hold all JSON data
combined_data = []
combined2_data = []
# Process each file
for file in nonvuln_files:
    try:
        # Open and read the JSON file
        with open(file, 'r') as f:
            data = json.load(f)  # Parse JSON array into a Python list
            num_examples = len(data)  # Count the number of examples in this file
            combined_data.extend(data)  # Add all elements to combined_data
        print(f"Successfully merged {file} with {num_examples} examples")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {file}")
    except FileNotFoundError:
        print(f"File not found: {file}")

# Write the combined data to vuln.json
with open("/home/bryson/research/research3.0/nonvuln.json", 'w') as f:
    json.dump(combined_data, f, indent=4)  # Use indent=4 for readability

for file in vuln_files:
    try:
        # Open and read the JSON file
        with open(file, 'r') as f:
            data = json.load(f)  # Parse JSON array into a Python list
            num_examples = len(data)  # Count the number of examples in this file
            combined2_data.extend(data)  # Add all elements to combined_data
        print(f"Successfully merged {file} with {num_examples} examples")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {file}")
    except FileNotFoundError:
        print(f"File not found: {file}")

# Write the combined data to vuln.json
with open("/home/bryson/research/research3.0/vuln.json", 'w') as f:
    json.dump(combined2_data, f, indent=4)  # Use indent=4 for readability
# Print total number of examples merged
total_examples = len(combined_data)
print(f"Merged all files into nonvuln.json and vuln.json successfully with a total of {total_examples} examples.")