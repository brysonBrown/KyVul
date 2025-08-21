Howdy! This C/C++ Vulnerability dataset consists of 10K vulnerable/non-vulnerable pairs for a total of 20K vulnerabilities. These vulnerabilities fall across the following 13 CWEs:
CWE - 119, CWE – 121
CWE – 122
CWE – 416
CWE – 190
CWE – 362
CWE - 78, CWE - 20
CWE - 125, CWE - 129, CWE – 787
CWE – 401
CWE – 415

Preprocessing
--------------
All code was preprocessed to remove comments and to fix json errors created by ChatGPT. All code was also preprocessed in order to remove the keyword "global" that was sometimes erroniously added to global variables.

Besides the vulnerable Stack and Heap buffer overflow categories, all other code was preprocessed to replace scanf for strings with fgets, sprintf with snprintf, and strcpy with strncpy. This was done to reduce the amount of trivial vulnerabilities that could compromise the rest of the dataset. 
