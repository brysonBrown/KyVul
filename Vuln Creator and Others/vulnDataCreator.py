import random
import requests
import json
import os
# Set random seed for reproducibility
#random.seed(39) #stack
random.seed(10)
#random.seed(38) #heap
#random.seed(1) #integer overflow
#random.seed(37) #use after free 
#random.seed(36) #race condition
#random.seed(16) #command injection
#random.seed(21) #out of bounds access
#random.seed(42) #memory leak
#random.seed(40) #double free
#--------------------------------------------------------------#
# vulns contains the vulnerabilities that will be added to the
# data set
#--------------------------------------------------------------#



options = [ "infinite recursion", 
           "gets",
           "memcpy",
           "strncpy with invalid length"
           "scanf",
           "sprintf",
           "invalid bounds checks"]

#had to move backgrounds inside of loop so that it will change the presented options
selected_options = random.sample(options, 3)



#--------------------------------------------------------------#
# get_chatgpt_response contains the code for making API request 
# to chat_gpt and getting the response back.
#--------------------------------------------------------------#

import requests
def get_chatgpt_response(prompt):
    api_key = "INSERT YOUR API KEY HERE"
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

# Example usage:
# response = get_chatgpt_response("Hello, how are you?")
# print(response)

# Generate random variables and lines



#--------------------------------------------------------------#
# data.json is the file that will contain the results for the 
# prompts
#--------------------------------------------------------------#

file_name = 'data.json'
file2_name = 'nonVulnData.json'
# Check if the file exists
if not os.path.isfile(file_name):
    # If not, create it and write an empty JSON array
    with open(file_name, 'w') as file:
        json.dump([], file)
# Load existing responses
with open(file_name, 'r') as file:
    data = json.load(file)

# Check if the file exists
# if not os.path.isfile(file2_name):
#     # If not, create it and write an empty JSON array
#     with open(file2_name, 'w') as file:
#         json.dump([], file)
# Load existing responses
# with open(file2_name, 'r') as file:
#     dataNotVuln = json.load(file)
# are these vulnerabilities enough? look at big vuln for num lines,, according to chat the average is between 30-50
# create non vulnerable part of same #
# what size of vulnerable functions should I do?
# is there a cheaper way to do this?

#--------------------------------------------------------------#
# Below creates the data set with chatGPT. You can change the 
# size of the data set below 
#--------------------------------------------------------------#

x = 0
tasks = [
    "Develop a data encryption system to protect sensitive information in transit or storage",
    "Create a digital art generator using algorithms and procedural generation techniques",
    "Write a kernel module to manage virtual memory in an operating system",
    "Design a custom protocol for secure data exchange between microcontrollers in an IoT system",
    "Build a chatbot using rule-based algorithms for customer service automation",
    "Create a program to analyze and predict traffic congestion using historical traffic data",
    "Design a real-time multiplayer game server that handles thousands of players playing a game",
    "Develop a home automation system to control lighting, temperature, and appliances remotely",
    "Build a microservice architecture for an e-commerce platform handling inventory and orders",
    "Design and implement a peer-to-peer file-sharing system with encryption and data redundancy",
    "Develop a facial recognition system for access control in secure facilities using traditional algorithms",
    "Implement a distributed file system for cloud storage with fault tolerance and replication",
    "Write a program to perform vulnerability scanning on web applications for security flaws",
    "Create a system for analyzing the performance of distributed systems under heavy load",
    "Build a low-latency network monitoring system to detect anomalies and attacks in real-time",
    "Design an augmented reality (AR) app for virtual home interior design",
    "Develop a video compression algorithm to reduce bandwidth usage without losing quality",
    "Write a program that simulates traffic patterns in urban areas using agent-based modeling",
    "Create a program for detecting fake news and misinformation online using traditional heuristics",
    "Build a self-driving car simulation that uses computer vision to navigate a virtual environment",
    "Develop a cloud-based virtual machine management system for resource allocation and scaling",
    "Design a customizable password manager with multi-factor authentication for added security",
    "Implement a program that generates realistic 3D terrain for game engines using procedural generation",
    "Create a biometric fingerprint recognition system for secure login to mobile devices",
    "Develop a program to detect and classify different types of malware on a network",
    "Design an intelligent traffic light system that optimizes traffic flow using real-time data",
    "Write a program for managing cryptocurrency wallets with secure transaction signing",
    "Develop a program that predicts energy consumption patterns based on historical data and usage behavior",
    "Build a blockchain-based supply chain management system for tracking product authenticity",
    "Create a drone-based surveillance system that streams live footage to a cloud platform",
    "Design an automated system for controlling irrigation in smart agriculture using weather data",
    "Implement a custom firewall to monitor and filter incoming and outgoing network traffic",
    "Build a recommendation engine for personalized content on streaming platforms using traditional algorithms",
    "Write a real-time collaborative whiteboard application for remote team brainstorming",
    "Design a program to monitor and manage hardware components in a data center, including temperature and performance",
    "Create a program for automated code review using static analysis and coding standards",
    "Design a virtual private network (VPN) solution for secure communication over public networks",
    "Develop a high-frequency trading algorithm to execute automated stock trades based on real-time market data",
    "Write a program for automated image recognition and classification for medical imaging diagnostics",
    "Design a custom SQL query optimization tool that improves database performance",
    "Create a system for secure mobile payments using QR codes and blockchain technology",
    "Build a real-time event detection system to identify significant occurrences in large datasets without AI",
    "Develop a system for tracking and managing remote sensors in an industrial setting",
    "Design a digital forensics tool to analyze and recover data from compromised systems",
    "Create a program to calculate and manage the tax liabilities of small businesses",
    "Build a complex database management system with support for multiple users and permissions",
    "Implement a multi-platform text editor with advanced features like syntax highlighting and version control integration",
    "Write a program that simulates and optimizes the flight path of drones for deliveries",
    "Design a system to automatically generate music compositions using traditional algorithmic methods",
    "Build an automatic text summarization tool for news articles using traditional algorithms",
    "Build a program to simulate sports broadcast storage network",
    "Create a remote desktop access tool with end-to-end encryption and session recording",
    "Write a program that simulates human brain neural activities for neuroscience research",
    "Design a system for scheduling drone flights in an agricultural environment to monitor crop health",
    "Build a program to manage and organize scientific research papers, citations, and notes",
    "Create a real-time weather prediction system using satellite data and weather models",
    "Implement a biometric voice recognition system for hands-free authentication in secure systems",
    "Design an intelligent energy management system for optimizing power usage in industrial environments",
    "Develop an automated system for detecting anomalies in network traffic patterns",
    "Create a customizable alert system for tracking server performance and availability in real-time",
    "Write a tool for managing large-scale backups of networked storage systems",
    "Design a system for automating software updates and patch management across a network",
    "Implement a peer-to-peer cryptocurrency exchange with real-time price tracking and transaction history",
    "Develop a GPS-based location tracking system for fleet management in a logistics company",
    "Build an IoT platform for smart device communication in a home automation ecosystem",
    "Create a real-time event-driven application for managing sports team statistics and scores",
    "Develop a network traffic analysis tool for identifying bottlenecks and latency issues",
    "Write a web-based dashboard to monitor server uptime, response times, and resource utilization",
    "Design a program to analyze the impact of various marketing campaigns on customer engagement",
    "Create an automated data entry system for importing financial data into accounting software",
    "Build an application for monitoring and controlling the temperature and humidity in a server room",
    "Write a simulation of a particle system to visualize physical phenomena in computational physics",
    "Develop an electronic voting system with anonymous voting and verifiable results",
    "Design a multi-channel communication system for dispatching messages in a weak network",
    "Create a lightweight, encrypted messaging system for secure communication on mobile devices",
    "Develop an automated video editing tool that combines clips and applies transitions based on user input",
    "Design a robotic arm controller for manufacturing processes using precision movement algorithms"
]




c_coding_styles = [
    "K&R Style (Kernighan and Ritchie)",
    "Allman Style",
    "BSD Style",
    "GNU Style",
    "Linux Kernel Style",
    "Horstmann Style",
    "Compact Style",
    "One True Brace Style (1TBS)",
    "Indent Style (Tabs vs. Spaces)"
]
# 1. Variable Layout
variable_layout = [
    "Grouped by Type",  # Variables of the same type are declared together at the top
    "Grouped by Usage",  # Variables are declared close to where they are first used
    "Declare One Per Line",  # Each variable is declared on its own line
    "Declare Multiple on One Line",  # Multiple variables declared on one line
]

# 3. Conditionals (if vs switch)
conditionals = [
    "If-Else Style",  # Relying on 'if' and 'else' for decision-making
    "Switch Style",  # Using 'switch' over 'if-else' chains for multiple conditions
    "Nested Conditionals",  # Using nested 'if' statements vs separating into functions
    "Ternary Operator",  # Using ternary ('? :') operators for compact conditional expressions
]

# 4. Loops (For vs While)
loops = [
    "For Loops",  # Using 'for' loops for ranges or collections
    "While Loops",  # Using 'while' loops when the number of iterations is unknown
    "Do-While Loops",  # Using 'do-while' for at least one iteration
    "For-Each Loops",  # Using 'for-each' loops for collections or arrays
]

# 5. Function Structure
function_structure = [
    "Function Length",  # Keeping functions small and focused or allowing larger functions
    "Return Value Type",  # Whether functions return values or just perform operations
    "Parameter Passing",  # Passing by value or by reference
]


# 7. Commenting Style
commenting_style = [
    "Inline Comments",  # Comments at the end of lines for explanation
    "Block Comments",  # Block comments to describe logic
    "Documenting Functions",  # Including documentation for functions or minimal comments
]

# 8. Naming Conventions
naming_conventions = [
    "CamelCase",  # Using camelCase for variable and function names
    "Snake_case",  # Using snake_case for variable and function names
    "Uppercase for Constants",  # Defining constants in uppercase
    "Prefix/Suffix Conventions",  # Prefixes like 'str_' or 'get_' to define variable roles
]


# 11. Code Block Size
code_block_size = [
    "Small Blocks",  # Breaking logic into small, manageable blocks
    "Large Blocks",  # Grouping related operations together
]


# 13. Variable Scope
variable_scope = [
    "Global Variables",  # Avoiding or minimizing global variables
    "Local Variables",  # Focusing on local variables to limit scope
    "Block Scoped Variables",  # Using block-scoped variables for better encapsulation
]

structs = [
    "Add structs",
    "Don't add structs",
    "Don't add structs",
]

size_data_set = 1
for i in range(0, size_data_set):
    task = random.choice(tasks)
    
    vulns = [
         "stack-based buffer overflow", #GG
         #"heap-based buffer overflow", #GG
         #"use after free", #GG 
         #"integer overflow", 
         #"race condition", #GG
         #"command injection",#G    
         #"out-of-bounds access",  
         #"memory leak", #GG             
         #"double free" #G             
    ]
    #"When memory is allocated but is not properly deallocated anywhere. Malloc a variable, and then do not use the free call anywhere and do not return it. Do not include strcpy, scanf, sprintf, or strcat but instead use strncpy, snprintf, snprintf, and strncat. There must be at least two memory leaks. I will tip you $150 if you do good.",
    backgrounds = [
     f"When data written to stack buffer exceeds its allocated size. Infinite recursion, user input with scanf, gets, sprintf, and large sizes for non-vulnerable functions can all cause this. Size checking parameters must be much bigger than buffer size or they will not work. Do not have less than 2 vulnerabilities. Do not use malloc to cause the overflow. There must be multiple stack overflow vulnerabilities. The students need to learn so don't hint at the vulnerability. I will tip you $150 if you do good.",
     #f"When data written to heap buffer exceeds its allocated size. Overflow a dynamically created variable using user input. Do this by using a function without a size parameter such as scanf, gets, sprintf. You can also use a larger size parameter for a buffer size-checking function such as fgets, strncpy or snprintf, but do not have the size parameter be smaller or equal to the buffer size. There must be multiple heap overflow vulnerabilities. The overflowed variable must by a dynamically created string. The students need to learn so don't hint at the vulnerability.I will tip you $150 if you do good.",
     #f"Accessing memory after it has been freed. Dynamically allocate a variable, free the variable, and then attempt to use the variable by assigning, or another manipulation. Do not include vulnerable functions such as strcpy, sprintf, or strcat but instead use strncpy, snprintf, and strncat. Use string buffer format specifiers for scanf or use fgets. No scanf for numbers due to int overflows use strtok. Do not set to NULL. Moving up a free call from its proper spot causes this. I will tip you $100 if the code has the vulnerability without hints in print statements, variable names, or function names.",
     #f"Integer overflows results from math operations that exceed bounds of type. Do this by downcasting values that are over 2147483647, bit shifting too far left on signed integers, user input in operations, incorrect accumulation in very large loops, multiplying very large numbers, or large exponentials. Ensure numbers are sufficiently large as integer overflows only occur if values become greater than 2147483647 without any overflow checks. Code must still perform given task. If the code does not have an overflow the students won't learn and I'll lose my job. I will tip you $120 if you do good.", 
     #f"When multiple threads or processes access shared data without proper synchronization. Modify shared variables in threads to complete the given task. Do not add semaphores or mutexes. Do not include strcpy, sprintf, or strcat but instead use strncpy, snprintf, and strncat. Use string buffer format specifiers for scanf or fgets. No scanf for numbers due to int overflows use strtok. Thread functions must do more than incrementing/decrementing shared variables. Must create multiple threads with functions that use shared variable. I will tip you $100 if you do good.",
     #f"Occurs when untrusted input is passed as a command. Requirements: 1) Make user input for the command a string, not an integer. 2) Mix in this vulnerability from using fork() and execlp(), popen(), execvp() or system() with vulnerable input into other functions for the task and not a command only function. 3)Do not include strcpy, sprintf, or strcat but instead use strncpy, snprintf, and strncat. Use string buffer format specifiers for scanf or fgets. No scanf for numbers due to int overflows use strtok. 4) Code must be compileable 5) Follow all previous structure requirments. 6) Do not use scanf. 7) The code must accomplish the previously given task, so incorporate this vulnerability into the solution. I will tip you $150 if you do good.",
     #f"Writing or reading memory outside the defined limits of an array. Off by one errors in array accesses are a common way to cause this as well as incorrect loop exit conditions. The program must be able to get to the access without out of bounds checks. I will tip you $100 if you do good.",
     #f"When memory is allocated but is not properly deallocated anywhere. Malloc a variable, and then do not use the free call anywhere and do not return it. Do not include strcpy, sprintf, or strcat but instead use strncpy, snprintf, snprintf, and strncat. Use string buffer format specifiers for scanf or fgets. No scanf for numbers due to int overflows use strtok. There must be at least two memory leaks. The code still needs to accomplish the previously given task, so incorporate this memory leak into the solution. The students need to learn so don't hint at the vulnerability. I will tip you $150 if you do good.",
     #f"When a program mistakenly frees the same memory location more than once. Add lines of code before you double free to hide the vulnerability. Do not include strcpy, sprintf, or strcat but instead use strncpy, snprintf, and strncat. Use string buffer format specifiers for scanf or fgets. No scanf for numbers due to int overflows use strtok. Freed variables that are then allocated again and freed are not double frees. Do not set freed variables to NULL or it will  prevent the vulnerability. The code still needs to accomplish the previously given task, so incorporate this double free into the solution. The students need to learn so don't hint at the vulnerability. There must be at least one double free. I will tip you $150 if you do good."
    ]

    #top 1 good, command injection could use some work in diversifying the cleaning method
    fixes = [ 
    #"Use size-limited functions and ensure proper bounds checking for memory. If taking numbers from user, ensure integer overflows do not occur. Do not include scanf, strcpy, gets, sprintf, or strcat but instead use strncpy, fgets, fgets, snprintf, and strncat. Do not leave comments in the code. Do not include scanf or fscanf. I will tip you $150 if you do good.",
    #"Use size-limited functions and ensure proper bounds checking for dynamically allocated memory. If dynamic memory is used for user input, use the input length as the size for the buffer. Do not include scanf, strcpy, gets, sprintf, or strcat but instead use strncpy, fgets, fgets, snprintf, and strncat. Do not leave comments in the code. Do not include scanf or fscanf. I will tip you $150 if you do good.",
    #"Ensure memory is not accessed after being freed. Use proper checks before referencing freed memory, and avoid dangling pointers. Keep all allocated memory as allocated memory. Make sure to handle malloc errors so that no memory leaks occur.",
    #"Check user input against the valid range of integers before performing arithmetic operations or printing. Use bounds checks to avoid exceeding the int range before calculations are made or results printed. Do not include strcpy, gets, scanf, sprintf, or strcat but instead use strncpy, fgets, fgets, snprintf, and strncat. replace all atoi() with strtol(). User input must be checked before being a loop condition. Do not leave comments in the code. I will tip you $200 if you do good.",
    #"Use mutexes or locks to ensure proper synchronization when accessing shared variables in concurrent threads. Modify the same variable from multiple threads. Only use safe input functions such as snprintf. Do not truncate variables. Do not leave comments in the code.",
    #"Sanitize user input by escaping/quoting the input to avoid passing untrusted input to system calls. Do not include strcpy, scanf, sprintf, or strcat but instead use strncpy, fgets, snprintf, and strncat. Use execv() or execvp() instead of system(). Do not leave comments in the code. Pass user arguments as part of an array to execvp or popen, such as *args[] = {<command>, user_input}; execvp(args[0], args). Do not make argv[0] bash, shell, or sh as this will cause vulnerabilities, but instead pick a command such as echo or ls. Do not open a shell for the user. I will tip you $175 if you do good.",
    #"Ensure array access is within bounds by using size checks or bounded loops. Avoid relying on user input without proper validation or checks. Do not include strcpy, scanf, sprintf, or strcat but instead use strncpy, snprintf, and strncat. Try to vary array sizes. Do not leave comments in the code. Ensure array indices are in bounds. I will tip you $150 if you do good.",
    #"Always free dynamically allocated memory after use. Track and release memory for all allocated variables to avoid memory leaks. If a malloc fails, all other memory must be freed before returning. Ensure freed memory is not used again. All allocated memory must be returned or freed. Do not leave comments in the code. I will tip you $150 if you do good.",
    #"Do not free the same memory location twice. Ensure proper memory management by tracking allocations and deallocations to prevent double frees. Do not include strcpy, scanf, sprintf, or strcat but instead use strncpy, snprintf, and strncat. Do not leave comments in the code. Make sure to properly free memory nested inside allocated array memory. If a cleanup function is called, do not free again. I will tip you $150 if you do good."
    ]

    if i % 50 == 0:
        print(i,"items created")
    selected_variable_layout = random.choice(variable_layout)
    selected_conditionals = random.choice(conditionals)
    selected_loops = random.choice(loops)
    selected_function_structure = random.choice(function_structure)
    selected_commenting_style = random.choice(commenting_style)
    selected_naming_conventions = random.choice(naming_conventions)
    selected_code_block_size = random.choice(code_block_size)
    selected_variable_scope = random.choice(variable_scope)
    struct_choice = random.choice(structs)
    code_style = random.choice(c_coding_styles)
    num_lines = random.randint(15, 60)
    vulnerability = vulns[x]
    background = backgrounds[x]
    #fix = fixes[x]
    x = x + 1
    if x % len(vulns) == 0:
        x = 0
    #prompt1 = f"Reword this task . Make it more complex and add details, but keep it under 25 words: {task}"
    #task = get_chatgpt_response(prompt1)
    if vulnerability == "command injection":
        num_lines = random.randint(30, 70) 
    if vulnerability == "race condition":
        num_lines = random.randint(30, 70)
    if vulnerability == "out-of-bounds access":
        num_lines = random.randint(20, 60)
    num_libraries = random.randint(2, 7)
    #if vulnerability != "integer overflow":
    prompt3 = (f'You are a coding and cyber security expert creating hidden, realistic vulnerable C/C++ code samples to teach students.'
                f'Here is your task: {task}. Here are your structural requirements: Variable layout: {selected_variable_layout}, Variable scope: {selected_variable_scope}.'
                f'Conditionals: {selected_conditionals}. Format of Loops: {selected_loops}. Code block size: {selected_code_block_size}. {struct_choice}.' 
                f'Naming conventions: {selected_naming_conventions}. Use functions from: {num_libraries} libraries. It must be exactly {num_lines} of lines. Must contain one {vulnerability} vulnerability or the code is worthless.'
                f'Background on the vulnerability: {background}. Code must look human written, and function. No empty conditions or loops. No comments. Function names must not hint at vulnerabilities.' 
                f'Output only the code as a JSON, nothing else. Code must have the specific vulnerability to teach the students. I will tip you $150 if you do good.')
    vulnerable_code = get_chatgpt_response(prompt3)

    # else:
    #     prompt1 = (f'You are a coding and cyber security expert creating hidden, realistic C/C++ code samples to teach students.'
    #             f'Here is your task: {task}. Here are your structural requirements: Variable layout: {selected_variable_layout}, Variable scope: {selected_variable_scope}.'
    #             f'Conditionals: {selected_conditionals}. Format of Loops: {selected_loops}. Code block size: {selected_code_block_size}. {struct_choice}.' 
    #             f'Naming conventions: {selected_naming_conventions}. Use functions from: {num_libraries} libraries. It must be exactly {num_lines} of lines. It must not contain a {vulnerability} vulnerability.'  
    #             f'Output only the code as a JSON, nothing else. I will tip you $150 if you do good.')
        
    #     non_vulnerable_code = get_chatgpt_response(prompt1)
    #     prompt2 = (f' You are a coding a cyber security expert creating hidden, vulnerable code to teach students. You must put a {vulnerability} into the following code.'
    #                f' Here is non-vulnerable code {non_vulnerable_code}. Must contain one {vulnerability} vulnerability or the code is worthless. Background on the vulnerability: {background}. '
    #                f' Code must look human written, and function. Do not add comments. Function names must not hint at vulnerabilities. Output only the code as a JSON, nothing else. I will tip you $100 if you do good')
    #     vulnerable_code = get_chatgpt_response(prompt2)

    #prompt4 = (f'Remove all comments. Do not change the code. Return just the code as a json. I will tip you $200 if you do well. {vulnerable_code}')
    #vulnerable_code = get_chatgpt_response(prompt4)

    # Append the new response
    # vulnerable_code = vulnerable_code + vulnerability
    #prompt4 = (f'You are a cyber security teacher. Inject an integer overflow into the code to teach students. Make the minimal changes required, and do not leave hints for the students. Background: {background}. Return only the code as a JSON. I will tip you $100 if you do good. Code: {vulnerable_code}')

    prompt4 = (f'You are a cyber security teacher. Inject an integer overflow into the code to teach students. First, increase the order of magnitude of every value used in operations, as maximum values, or as loop exit criteria. All long and long long must be changed to int. Make the minimal changes required, and use variable names that make sense in the code (do not mention overflow). Return only the code as a JSON. Ways to creat the vulnerability: downcasting longs to ints that are over 2147483647, left shifting by a lot on signed integers, multiplying large numbers (over 1,000,000), very large accumulation (must have user input or be for over 100,000,000), and adding user input all can cause without overflow checks, so no switch statements that check. No commments. I will tip you $100 if you do good. Code: {vulnerable_code}')
    vulnerable_code = get_chatgpt_response(prompt4)
    data.append(vulnerable_code)
    
    # prompt5 = (f'You are an expert cyber security analyst. Below is some vulnerable code that most likely has a {vulnerability} vulnerability.'
    #            f'I need you to fix this vulnerability, as well as others. Any functions vulnerable to buffer overflow should be replaced such as strcpy, scanf, gets, strcmp, and any other functions that read or modify buffers without size checks.'
    #             f'Size-checking functions should never have hard coded sizes to avoid buffer overflows. You must replace instances of all scanf, gets, strcmp, strcpy, sscanf with a safe function.'
    #             f'Here is a description to help you: {fix}. Here is the vulnerable code {vulnerable_code} Output just the code as a JSON with no comments.If the outputed code is safe with no comments, I will tip you $100.')
    

    # non_vulnerable_code = get_chatgpt_response(prompt5)

    # prompt6 = (f'You are an expert at fixing code vulnerabilities, and I need you to make this code even safer. Scanf, gets, strcmp, strcpy, and sscanf are all very vulnerable and must be replaced. '
    #           f'It may still have a {vulnerability} vulnerability. Output just the code as a JSON with no comments. If the outputed code is safe with no comments, I will tip you $100. Delete all comments. Here is the code {non_vulnerable_code}'
    #           )
    # if vulnerability == "stack-based buffer overflow" or vulnerability == "heap-based buffer overflow":
    #     prompt6 = (f'The following code has buffer overflows. Replace all scanf and fscanf with fgets. I will tip you $150 if you do well. Output just the code as a JSON with no comments. {non_vulnerable_code}')
    #     non_vulnerable_code = get_chatgpt_response(prompt6)


    #dataNotVuln.append(non_vulnerable_code)

# Write the updated data back to the file
with open(file_name, 'w') as file:
    json.dump(data, file, indent=4)

# with open(file2_name, 'w') as file:
#     json.dump(dataNotVuln, file, indent=4)




