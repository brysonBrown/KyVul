# Code Creation README

The **Code Creation** scripts are used to generate vulnerable code samples and their non-vulnerable counterparts.

## Libraries Used

```python
import json
import random
import requests
import os
```

## 🔹 vulnDataCreator.py

- Creates **vulnerable code samples** for specified categories.
- **Important variables**:
  - `seed`: changed per category to ensure diversity.
  - `size_data_set`: number of samples to generate.
  - `vulns`: list of vulnerabilities to generate.
  - `background`: must uncomment corresponding background for each category.
- **Output**: results saved to `data.json`.

## 🔹 nvDataCreator.py

- Generates **non-vulnerable code** from vulnerable examples.
- **Inputs/variables**:
  - `input_file`: path to preprocessed vulnerable samples.
  - `file2_name`: output file name for fixed functions.
  - `specific`: set to `None` to fix all samples, or provide index to fix a specific one.
  - `vuln` and `fixes` lists: define vulnerability types and their safe replacements.

## ✅ Creating Vulnerable Code

1. Update the required items:
   - Vulnerability category
   - Background
   - Number of examples
   - Random seed
   - Output file name
2. Run:

```bash
python3 vulnDataCreator.py
python3 parser3.py  # makes output JSON-parsable
```

3. Run the **fixer scripts** (see Code Cleaners README) in order to correct formatting.

## ✅ Creating Non-Vulnerable Code

1. Run:

```bash
python3 strcpy_remover.py <vuln_file.json>
```

- Replaces trivial functions like `strcpy` with safer versions.

2. Set the cleaned vulnerable file as the **input** to `nvDataCreator.py`.
3. Update:
   - `file2_name` (output path)
   - `background` and `fix` lists
   - `specific = None` if fixing all
4. Run:

```bash
python3 nvDataCreator.py
python3 parser3.py
```

5. Run the fixers in order to finalize clean JSON.

## 🔹 Merging Datasets

- After generating and cleaning all categories:

```bash
python3 merger.py     # merges fixed vuln and non-vuln jsons separately
python3 kyMerger.py   # zippers vuln + non-vuln into final KyVul.json
```
