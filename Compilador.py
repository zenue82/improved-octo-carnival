import re

token_patterns = {
    'NUM': r'\b\d+\b',
    'ID': r'\b[a-zA-Z_][a-zA-Z_0-9]*\b',
    'OP': r'[+\-*/=]',
    'DELIM': r'[;,]',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'WHITESPACE': r'\s+',
    'INVALID': r'.',
}

def lexical_analysis(code):
    position = 0
    tokens = []
    while position < len(code):
        match = None
        for token_type, pattern in token_patterns.items():
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                if token_type != 'WHITESPACE':
                    tokens.append((token_type, match.group(0)))
                position = match.end()
                break
        if not match:
            tokens.append(('INVALID', code[position]))
            position += 1
    return tokens

def syntactic_analysis(tokens):
    stack = []
    for token in tokens:
        token_type, value = token
        if token_type == 'NUM' or token_type == 'ID':
            stack.append(value)
        elif token_type == 'OP':
            if len(stack) < 2:
                return False
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f"({operand1} {value} {operand2})")
        elif token_type == 'DELIM' or token_type in ['LPAREN', 'RPAREN']:
            pass
        elif token_type == 'INVALID':
            return False
    return len(stack) == 1

def main():
    code = "x = 10 + 20; y = x * 2;"
    print("Análise Léxica:")
    tokens = lexical_analysis(code)
    for token in tokens:
        print(token)
    print("\nAnálise Sintática:")
    is_valid = syntactic_analysis(tokens)
    print("Código sintaticamente válido:", is_valid)

if __name__ == "__main__":
    main()
