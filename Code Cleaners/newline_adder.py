import json

def process_code(s):
    """
    Process a string to:
    - Add newlines: before '#' (if not first and no prior newline), after ';', '{', '}' (if no following newline)
    - Remove '#' if not part of '#include' or '#define'
    - Avoid adding extra newlines when they already exist
    - Skip newlines before 'for(...){' and 'while(...){'
    - Skip newline between '}' and 'while' in do-while loops
    - Skip newlines after ';' within 'for (...)' parentheses
    """
    result = []
    i = 0
    in_for_parens = False
    paren_depth = 0

    while i < len(s):
        if s[i] == '#':
            if (i + 7 < len(s) and s[i:i+8] == '#include') or \
               (i + 6 < len(s) and s[i:i+7] == '#define'):
                if i > 0 and s[i-1] != '\n' and (not result or result[-1] != '\n'):
                    result.append('\n')
                if s[i:i+8] == '#include':
                    result.append('#include')
                    i += 8
                else:  # '#define'
                    result.append('#define')
                    i += 7
            else:
                if i > 0 and s[i-1] != '\n' and (not result or result[-1] != '\n'):
                    result.append('\n')
                i += 1  # Skip the '#'
                continue
        else:
            # Track if we're inside 'for (...)' parentheses
            if i > 3 and s[i-3:i].lower() == 'for' and s[i] == '(':
                in_for_parens = True
                paren_depth = 1
            elif in_for_parens and s[i] == '(':
                paren_depth += 1
            elif in_for_parens and s[i] == ')':
                paren_depth -= 1
                if paren_depth == 0:
                    in_for_parens = False

            result.append(s[i])
            if s[i] in {';', '{', '}'} and (i == len(s) - 1 or s[i+1] != '\n') and (not result or result[-1] != '\n'):
                skip_newline = False
                if i + 1 < len(s):
                    lookahead = s[i+1:].lower().strip()[:20]
                    # Skip newline before 'for(...){' or 'while(...){'
                    if s[i] in {';', '{', '}'} and (lookahead.startswith('for') and '(' in lookahead and '{' in lookahead or \
                                                   lookahead.startswith('while') and '(' in lookahead and '{' in lookahead):
                        skip_newline = True
                    # Skip newline between '}' and 'while' in do-while
                    elif s[i] == '}' and lookahead.startswith('while'):
                        skip_newline = True
                    # Skip newline after ';' inside 'for (...)' parentheses
                    elif s[i] == ';' and in_for_parens:
                        skip_newline = True
                
                if not skip_newline:
                    result.append('\n')
            i += 1
    
    return ''.join(result)

def remove_duplicate_newlines(s):
    """
    Replace all instances of '\n\n' with '\n' in the string.
    """
    while '\n\n' in s:
        s = s.replace('\n\n', '\n')
    return s

def remove_newlines_before_and_in_control(s):
    """
    Remove newlines before 'for(...){', 'while(...){', between '} while' in do-while loops,
    and after ';' within 'for (...)' parentheses.
    """
    lines = s.split('\n')
    result = []
    i = 0
    in_for_parens = False
    paren_depth = 0

    while i < len(lines):
        current_line = lines[i].rstrip()
        next_line = lines[i + 1].lstrip().lower() if i + 1 < len(lines) else ''
        
        # Track 'for (...)' state across lines
        if 'for' in current_line.lower() and '(' in current_line:
            in_for_parens = True
            paren_depth = current_line.count('(') - current_line.count(')')
        elif in_for_parens:
            paren_depth += current_line.count('(') - current_line.count(')')
            if paren_depth <= 0:
                in_for_parens = False

        # Handle do-while: merge '} while' onto same line
        if current_line.endswith('}') and next_line.startswith('while'):
            result.append(f"{current_line} while {next_line[len('while'):].lstrip()}")
            i += 2
        # Handle 'for(...){' or 'while(...){'
        elif next_line and (next_line.startswith('for') and '(' in next_line and '{' in next_line or \
                            next_line.startswith('while') and '(' in next_line and '{' in next_line):
            result.append(current_line)
            i += 1
        # Handle ';' in 'for (...)' - remove newline if present
        elif in_for_parens and current_line.endswith(';') and next_line:
            result.append(f"{current_line} {next_line}")
            i += 2
        else:
            result.append(current_line + '\n')
            i += 1
    
    return ''.join(result).rstrip('\n')

def process_json_file(input_file, output_file):
    """
    Read JSON from input_file, process the 'code' field(s), clean up newlines, and write to output_file.
    """
    with open(input_file, 'r') as f:
        data = json.load(f)

    if isinstance(data, dict) and 'code' in data:
        processed = process_code(data['code'])
        no_duplicates = remove_duplicate_newlines(processed)
        data['code'] = remove_newlines_before_and_in_control(no_duplicates)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and 'code' in item:
                processed = process_code(item['code'])
                no_duplicates = remove_duplicate_newlines(processed)
                item['code'] = remove_newlines_before_and_in_control(no_duplicates)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

# Use the same file for input and output
file_name = '/home/bryson/research/research3.0/fixed_nonvuln.json'
process_json_file(file_name, file_name)

print(f"Processed and updated {file_name}")
file_name = '/home/bryson/research/research3.0/fixed_vuln.json'
process_json_file(file_name, file_name)

print(f"Processed and updated {file_name}")