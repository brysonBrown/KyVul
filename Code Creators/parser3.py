import json
import re

def clean_code(code):
    """
    Clean C code by removing extra backslashes and fixing escape sequences.
    """
    code = re.sub(r'\\{2,}(?=[n\'"0])', r'\\', code)
    code = code.replace("\\n", "\n").replace("\\\"", "\"").replace("\\'", "\'")
    code = code.rstrip().rstrip(' }')
    return code

def process_line(line, line_number):
    """
    Process a single JSONL line to clean 'func' and keep 'original'.
    """
    try:
        print(f"Line {line_number}: Length = {len(line)} characters")
        print(f"Line {line_number} raw: {repr(line)}")

        # Parse all JSON objects in the line, handling trailing commas
        objects = []
        remaining = line.strip()
        decoder = json.JSONDecoder()

        while remaining:
            try:
                obj, idx = decoder.raw_decode(remaining)
                objects.append(obj)
                remaining = remaining[idx:].strip()
                if remaining and remaining[0] == ',':
                    remaining = remaining[1:].strip()
            except json.JSONDecodeError as e:
                print(f"Line {line_number}: Parse stopped at {e.pos} with error: {e}")
                break

        if not objects:
            print(f"Line {line_number}: No valid JSON objects found")
            return None

        results = []
        for obj in objects:
            func = obj.get("func", "")
            original = obj.get("original", "")

            # Remove all variations of the prefix between "func": and the last "
            if func:
                # Define a flexible pattern to match all prefix variations
                # Matches "json\n{" or "{" followed by optional whitespace and "\"code\":"
                prefix_pattern = r'(?:json\n)?{\s*\"code\":\\?\"?'
                cleaned_func = func

                # Remove all occurrences of the prefix pattern
                while re.search(prefix_pattern, cleaned_func):
                    match = re.search(prefix_pattern, cleaned_func)
                    if match:
                        cleaned_func = cleaned_func[match.end():]

                # Handle any remaining quotes and extract up to the last "
                if cleaned_func.startswith('"'):
                    cleaned_func = cleaned_func[1:]
                match = re.search(r'^(.*?)(?:\"(?:\\n)?(?:\s*})$', cleaned_func)
                if match:
                    code = match.group(1)
                else:
                    code = cleaned_func
            else:
                code = func

            # Clean the code
            cleaned_func = clean_code(code)
            new_obj = {
                "target": 1,
                "func": cleaned_func,
                "original": original
            }
            results.append(new_obj)

        return results
    except Exception as e:
        print(f"Line {line_number}: Unexpected error: {e}")
        return None

def main(input_file, output_file):
    """
    Read input JSONL, process each line, and write to output JSONL.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    fixed_data = []
    for line_number, line in enumerate(lines, 1):
        processed = process_line(line, line_number)
        if processed:
            if isinstance(processed, list):
                fixed_data.extend(processed)
            else:
                fixed_data.append(processed)
        else:
            print(f"Failed to process line {line_number}")

    with open(output_file, 'w', encoding='utf-8') as f:
        for obj in fixed_data:
            f.write(json.dumps(obj) + '\n')

    print(f"Processed {len(fixed_data)} lines and saved to {output_file}.")

if __name__ == "__main__":
    input_file = "modified_primevul.jsonl"
    output_file = "output.jsonl"
    main(input_file, output_file)