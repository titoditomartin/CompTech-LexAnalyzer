import re

# Define token types
token_specification = [
    ('NUMBER',   r'\d+(\.\d*)?'),    # Integer or decimal number
    ('ID',       r'[A-Za-z]+'),      # Identifiers
    ('ASSIGN',   r'='),              # Assignment operator
    ('END',      r';'),              # Statement terminator
    ('OP',       r'[+\-*/]'),        # Arithmetic operators
    ('LPAREN',   r'\('),             # Left parenthesis
    ('RPAREN',   r'\)'),             # Right parenthesis
    ('LBRACE',   r'\{'),             # Left brace
    ('RBRACE',   r'\}'),             # Right brace
    ('SKIP',     r'[ \t]+'),         # Skip over spaces and tabs
    ('MISMATCH', r'.'),              # Any other character
]

# Sample input
code = '''INT x = 5; IF (x > 0) { RETURN x + 1; }'''

# Tokenize input
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
line_num = 1
for mo in re.finditer(token_regex, code):
    kind = mo.lastgroup
    value = mo.group()
    if kind == 'NUMBER':
        value = float(value) if '.' in value else int(value)
    elif kind == 'ID':
        value = value
    elif kind == 'SKIP':
        continue
    print(f'{kind}: {value}')
