import re

# Token specification
token_specification = [
    ('NUMBER',   r'\d+(\.\d*)?'),    # Integer or decimal number
    ('PLUS',     r'\+'),             # Addition operator
    ('MINUS',    r'-'),              # Subtraction operator
    ('TIMES',    r'\*'),             # Multiplication operator
    ('DIVIDE',   r'/'),              # Division operator
    ('LPAREN',   r'\('),             # Left parenthesis
    ('RPAREN',   r'\)'),             # Right parenthesis
    ('NAME',     r'[A-Za-z]+'),      # Identifiers (variable names)
    ('SKIP',     r'[ \t]+'),         # Skip over spaces and tabs
    ('MISMATCH', r'.'),              # Any other character
]

# Tokenizer function
def tokenize(code):
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'NAME':
            pass  # Leave the value as a string
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        print(f'{kind}: {value}')

# Test string sample
sample_code = "x + 3.14 * (y - 5)"

# Run the lexer on the sample string
tokenize(sample_code)
