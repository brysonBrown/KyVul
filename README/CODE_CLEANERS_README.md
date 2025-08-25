# Code Cleaners README

The **Code Cleaners** scripts correct formatting, JSON errors, and trivial vulnerabilities introduced during generation.

## 🔹 Fixer Scripts

Run these in order after creating vulnerable/non-vulnerable code:

```bash
python3 parser3.py                  # fixes JSON formatting issues
python3 removes_unnecessary_code.py # removes duplicate "code" entries
python3 vuln_fixer.py               # removes stray '}' and extra newlines
python3 global_remover.py           # removes erroneous "global" keywords
python3 newline_adder.py            # adds missing \n to JSON objects
```

### What They Do

- **parser3.py** → Corrects malformed JSON.  
- **removes_unnecessary_code.py** → Removes redundant `code` entries.  
- **vuln_fixer.py** → Removes extra `}` and newlines.  
- **newline_adder.py** → Ensures each JSON object is newline-terminated.  
- **global_remover.py** → Cleans invalid `global` keywords inserted by LLMs.  

## 🔹 Preprocessing Scripts

- **strcpyRemove.py** → Replaces trivial vulnerabilities (`strcpy`, `sprintf`, etc.) with safer versions.  
- **comment_remover.py** → Strips comments from code to prevent noise.  

## 🔹 Duplicate Detection

After fully cleaning your dataset with the fixer scripts, you can run duplicate detection using [Microsoft’s Duplicate Code Detector](https://github.com/microsoft/DuplicateCodeDetector).

### Steps

1. Run the following commands in order:

```bash
python3 extractor2.py
python3 tokenizer_for_checker.py
dotnet run --project FILEPATH/DuplicateCodeDetector/DuplicateCodeDetector/DuplicateCodeDetector.csproj --dir=. results
```

2. **Important notes:**
   - In `extractor2.py`, you must update the **path variable** to match your dataset location.  
   - Duplicate detection can **only be run on the fully cleaned code** produced after the fixers pipeline.  
   - Results will be written to the `results` directory.  

### Example `extractor2.py` Path Change

```python
# Before
input_path = "/default/path/to/data.json"

# After (customized for your system)
input_path = "C:/Users/YourName/Desktop/AI/game/data/final_cleaned.json"
```

## 🔹 Workflow Example

1. Generate vulnerable code with `vulnDataCreator.py`.  
2. Run **parser3 + fixers** in sequence.  
3. Apply `strcpyRemove.py` and `comment_remover.py` if needed.  
4. Use `nvDataCreator.py` for non-vulnerable code.  
5. Re-run parser + fixers.  
6. Run **duplicate detection** on the fully cleaned output.  
7. Merge files with `merger.py` and `kyMerger.py`.  

---

✅ With these tools, you can generate new vulnerable/non-vulnerable pairs, clean them, detect duplicates, and integrate them into **KyVul.json** for research and experimentation.
