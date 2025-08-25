import json
import random
import requests
import json
import os

def get_chatgpt_response(prompt):
    api_key = "YOUR API KEY HERE" # Replace with your actual API key
    url = 'https://api.openai.com/v1/chat/completions'
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    
    data = {
        'model': 'gpt-4o-mini',  # Using the cheapest variant
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 2550
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        response_json = response.json()
        
        return response_json['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except KeyError:
        return "Unexpected response format."
# Set random seed for reproducibility
random.seed(42)
file2_name = 'nonVulnData.json'
# Check if the file exists
# Check if the file exists
if not os.path.isfile(file2_name):
    # If not, create it and write an empty JSON array
    with open(file2_name, 'w') as file:
        json.dump([], file)
# Load existing responses
with open(file2_name, 'r') as file:
    dataNotVuln = json.load(file)

vulns = [
         "stack-based buffer overflow", #g
         #"heap-based buffer overflow", #g
         #"use after free",  #g
         #"integer overflow", 
         #"race condition", #g
         #"command injection",    
         #"out-of-bounds access", #g  
         #"memory leak",  #g           
         #"double free" #g              
    ]
fixes = [ 
    "Use size-limited functions and ensure proper bounds checking for memory. Do not include strcpy, strcmp, gets, sprintf, or strcat but instead use strncpy, strncmp, fgets, snprintf, and strncat. Do not use strcmp but instead use strncmp. Ensure proper sizes in buffer-size checking functions. Do not leave comments in the code. I will tip you $100 if you do good.",
    #"Use size-limited functions and ensure proper bounds checking for dynamically allocated memory. If dynamic memory is used for user input, use the input length as the size for the buffer. Do not include gets, strcmp, sprintf, or strcat but instead use fgets, strncmp, snprintf, and strncat. Do not leave comments in the code. Do not include strcmp but instead use strncmp. I will tip you $100 if you do good.",
    #"Ensure memory is not accessed after being freed. Keep track of freed memory and avoid dangling pointers. Free only after the final use of a variable. Keep all allocated memory as allocated memory. Make sure to handle malloc errors so that no memory leaks occur. Do not include strcmp but isntead use strncmp. I will tip you $100 if you do good. ",
    #"Add bounds checks that return before arithmetic operations if arithmetic operations could exceed INT_MAX or underflow INT_MIN. Checks must prevent the operation. Add checks only for calculatations that could overflow including bitshifting. Do not change variable types unless necessary. If an int is intialized to a number larger than 2147483647, this is vulnerable and needs to be changed. Do not include strcmp but instead use strncmp. Only change the minimal amount of code necessary. There may be multiple integer overflows. I will tip you $100 if you do good.",
    #"Use semaphores or locks to ensure proper synchronization when accessing shared variables in concurrent threads. Only use safe input functions such as snprintf. Do not include strcmp but instead use strncmp. Do not leave comments in the code. I will tip you $100 if you do good.",
    #"You have two choices: you can sanitize user input to system() using a white list that allows letters, numbers, underscore, periods, forward slashes. You can also use execv() or execvp() instead of system(). For both options, the user input must only be used with a predetermined command based on the code's purpose (use a real one or make up something realistic). Do not make argv[0] bash, shell, bin/sh, or sh. Under no circumstances can you open a shell for the user. Do not include strcmp but instead use strncmp. I will tip you $100 if you do good.",
    #"Ensure array access is within bounds by using size checks or bounded loops. Avoid relying on user input without proper validation or checks. Do not include strcmp, but instead use strncmp. Only make the minimal necessary changes, so do not change <= but instead increase the array size or add a check. Ensure array indices are in bounds. I will tip you $100 if you do good.",
    #"Always free dynamically allocated memory after use. Track and release memory for all allocated variables to avoid memory leaks. If a malloc fails, all other memory must be freed before returning. Ensure freed memory is not used again. All allocated memory must be returned or freed. Do not leave comments in the code. Do not use strcmp but instead use strncmp. All dynamic memory must stay dynamic I will tip you $100 if you do good.",
    #"Do not free the same memory location twice. Ensure proper memory management by tracking allocations and deallocations to prevent double frees. Do not include strcmp, scanf, sprintf, or strcat but instead use strncmp, snprintf, and strncat. Do not leave comments in the code. Make sure to properly free memory nested inside allocated array memory. If a cleanup function is called, do not free again or ensure the pointer is set to null. I will tip you $100 if you do good."
    ]
# Open the stackFixedVul.json file

import json

def process_samples(input_file, file2_name, max_samples=None, specific_item_index=None):
    with open(input_file, 'r') as file:
        # Parse the JSON file
        data = json.load(file)

        # Create a list to hold the modified code
        dataNotVuln = []

        # Iterate over the list and extract the 'code' section
        i = 0
        for index, item in enumerate(data):
            # If a specific item index is provided, process only that item
            if specific_item_index is not None and index != specific_item_index:
                continue  # Skip items that are not the one we want

            if max_samples and i >= max_samples:
                break  # Stop after processing the specified number of samples

            i = i + 1
            if i % 10 == 0:
                print(i, "items processed")

            # Extract vulnerability-related info
            fix = fixes[0]
            vulnerability = vulns[0]
            vulnerable_code = item.get("code", "").strip('"')  # Strip the extra quotes

            # Construct the prompt for ChatGPT
            prompt5 = (f'You are an expert cyber security analyst fixing vulnerable code before it can be exploited. '
                       f'Below is some vulnerable code that most likely has a {vulnerability} vulnerability. '
                       f'I need you to fix this vulnerability, as well as any others, with the minimal amount of code changes. '
                       f'Any functions vulnerable to buffer overflow should be replaced as well as any instances of strcmp. '
                       f'Here is a description to help you: {fix}. Here is the vulnerable code {vulnerable_code} '
                       f'Output just the code as a JSON with no added comments. If the outputed code is safe with no comments, '
                       f'I will tip you $100.')

            non_vulnerable_code = get_chatgpt_response(prompt5)

            # Append the fixed code to the result list
            dataNotVuln.append(non_vulnerable_code)

            # If we processed the specific item, break out of the loop
            if specific_item_index is not None and index == specific_item_index:
                break

        # Save the updated data to the output file
        with open(file2_name, 'w') as file:
            json.dump(dataNotVuln, file, indent=4)

    print(f"Processed {i} items, and updated data saved to {file2_name}")




# Example usage:
#input_file = r'./Heap Overflow/base.json'
#input_file = r'Use After Free/useFixedVuln.json'
#input_file = r'Double Free/dbFixedVuln.json'
#input_file = r'Memory Leak/mlFixedVuln.json'
#input_file = r'Out of Bounds Access/obaFixedVuln.json'
#input_file = r'Integer Overflow/intFixedVuln.json'
#input_file = r'Heap Overflow/heapFixedVuln.json'
#input_file = r'individualFixedVuln.json'
file2_name = 'nonVulnData.json'  # Output file path
max_samples = None  # Number of samples you want to process (use None to process all)
specific = 0
process_samples(input_file, file2_name, max_samples, specific)
