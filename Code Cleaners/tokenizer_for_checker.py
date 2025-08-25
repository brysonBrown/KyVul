import os
import gzip
import json
from pygments import lex
from pygments.lexers import CLexer
from pygments.token import Token

# Function to tokenize a single C file
def tokenize_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
        
        # Tokenize the C code using pygments C lexer
        tokens = []
        for token in lex(code, CLexer()):
            # Skip whitespace and optionally comments
            if token[0] in (Token.Text, Token.Text.Whitespace):
                continue
            # Uncomment the line below to exclude comments too
            # if token[0] in (Token.Comment, Token.Comment.Multiline, Token.Comment.Single):
            #     continue
            tokens.append(token[1])  # Add only the token string
        
        if not tokens:
            print(f"Warning: {file_path} produced no tokens (empty or whitespace-only)")
        return tokens
    except Exception as e:
        print(f"Error tokenizing {file_path}: {e}")
        return []

# Function to create JSONL file from code files
def create_jsonl_from_code_files(code_files_dir, output_jsonl_path, expected_count=9999):
    # Get and sort .c files numerically
    c_files = [f for f in os.listdir(code_files_dir) if f.endswith('.c')]
    c_files.sort(key=lambda x: int(x.replace('code_', '').replace('.c', '')))
    total_files = len(c_files)
    print(f"Found {total_files} .c files in {code_files_dir}")

    # Check against expected count
    if total_files != expected_count:
        print(f"Warning: Expected {expected_count} files, but found {total_files}")

    skipped_files = []  # Track files that weren’t written

    with gzip.open(output_jsonl_path, 'wt', encoding='utf-8') as jsonl_file:
        processed_count = 0
        written_count = 0
        for i, filename in enumerate(c_files, 1):
            file_path = os.path.join(code_files_dir, filename)
            tokens = tokenize_file(file_path)
            processed_count += 1
            
            if tokens:
                file_entry = {
                    "filename": filename,
                    "tokens": tokens
                }
                jsonl_file.write(json.dumps(file_entry) + '\n')
                written_count += 1
            else:
                skipped_files.append(filename)
                print(f"Skipped writing {filename}: No tokens produced")

    print(f"Processed {processed_count} files, wrote {written_count} entries to JSONL.")
    if processed_count != expected_count:
        print(f"Warning: Expected to process {expected_count} files, but processed {processed_count}")
    if written_count != expected_count:
        print(f"Warning: Expected to write {expected_count} entries, but wrote {written_count}")
        print(f"Missed {expected_count - written_count} file(s). Skipped files: {', '.join(skipped_files)}")
    else:
        print(f"Success: Wrote all {expected_count} expected entries to JSONL")
    print(f"Tokenization complete. Output saved to {output_jsonl_path}")

# Set the directory of C files and the output JSONL file
code_files_directory = r'/home/bryson/research/research3.0/Code Cleaners/code_files'
output_jsonl_gz = '/home/bryson/research/research3.0/output_data.jsonl.gz'

# Create the compressed JSONL file
create_jsonl_from_code_files(code_files_directory, output_jsonl_gz)