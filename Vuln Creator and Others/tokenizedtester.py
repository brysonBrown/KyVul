import gzip
import json

with gzip.open('output_data.jsonl.gz', 'rt', encoding='utf-8') as f:
    valid_count = 0
    for line_num, line in enumerate(f, 1):
        try:
            entry = json.loads(line.strip())
            if not isinstance(entry, dict):
                print(f"Line {line_num}: Not a JSON object: {line.strip()}")
                continue
            if "filename" not in entry or "tokens" not in entry:
                print(f"Line {line_num}: Missing 'filename' or 'tokens': {line.strip()}")
                continue
            if not isinstance(entry["tokens"], list):
                print(f"Line {line_num}: 'tokens' is not a list: {line.strip()}")
                continue
            if not entry["tokens"]:
                print(f"Line {line_num}: 'tokens' is empty: {line.strip()}")
                continue
            if not isinstance(entry["filename"], str) or not entry["filename"]:
                print(f"Line {line_num}: 'filename' is invalid: {line.strip()}")
                continue
            valid_count += 1
        except json.JSONDecodeError as e:
            print(f"Line {line_num}: Invalid JSON - {e}: {line.strip()}")
    print(f"Total valid entries with non-empty tokens: {valid_count}")

with gzip.open('output_data.jsonl.gz', 'rt', encoding='utf-8') as f:
    count = 0
    for line_num, line in enumerate(f, 1):
        entry = json.loads(line.strip())
        token_count = len(entry["tokens"])
        if token_count < 10:  # Adjust threshold as needed
            count = count + 1
            print(f"Line {line_num}: {entry['filename']} has {token_count} tokens")
print(count)