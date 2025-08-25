import json
import random

# Load the JSON data from files

#with open('stackFixedNonVuln.json', 'r') as non_vuln_file:
#    non_vuln_data = json.load(non_vuln_file)

with open('cmdFixedNonVuln.json', 'r') as vuln_file:
     vuln_data = json.load(vuln_file)

# Randomly sample 100 items from each dataset
#non_vuln_sample = random.sample(non_vuln_data, 112)
vuln_sample = random.sample(vuln_data, 112)

# Write the sampled data to new JSON files
#with open('stackNonVulnSamples.json', 'w') as non_vuln_sample_file:
#    json.dump(non_vuln_sample, non_vuln_sample_file, indent=4)

with open('cmdNonVulnSamples.json', 'a') as vuln_sample_file:
     json.dump(vuln_sample, vuln_sample_file, indent=4)

print("Samples have been saved to stackNonVulnSamples.json and stackVulnSamples.json.")


