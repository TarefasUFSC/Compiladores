'''
Analisador lexico deve reconhecer as seguintes estruturas da linguagem de programação C:

declaração de variáveis (tipos);
estruturas condicionais 'if', 'if-else';
estruturas de repetição 'for' e 'while';
bloco principal 'main()'
'''



from ply import *
import argparse

# Palavras Reservadas
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'int' : 'INT',
    'main' : 'MAIN',
    'float' : 'FLOAT',
    'for' : 'FOR',
    'while' : 'WHILE',
    'do' : 'DO',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'void' : 'VOID'
}

# Demais Tokens
tokens = [
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'LEFTPAREN', 'RIGHTPAREN', 'LESSTHEN', 'LESSEQUAL', 'GREATERTHEN', 'GREATEREQUAL', 'NOTEQUAL',
    'COMMA', 'SEMICOLON', 'INTEGERCONST', 'FLOATCONST', 'STRING',
    'ID', 'NEWLINE', 'RIGHTBRACES', 'LEFTBRACES'
] + list(reserved.values())

t_ignore = ' \t'

"""
    Essa função funciona da seguinte maneira: 
    - A função t_REM é responsável por reconhecer comentários no código fonte.
    - A expressão regular deve reconhecer qualquer sequencia de texto de 1 linha que comece com '//'.
    - A função retorna o token t.

    - REM é uma abreviação de REMARK, que é uma palavra reservada utilizada em BASIC para comentários.
    """
def t_REM(t):
    r'//.*'
    return t

"""
    Essa função funciona da seguinte maneira: 
    - A função t_ID é responsável por reconhecer identificadores no código fonte.
    - A expressão regular r'[a-zA-Z][a-zA-Z0-9]*' reconhece qualquer sequência de letras seguida ou não de números.
    - A função retorna o token t.
"""
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'
t_RIGHTBRACES = r'\}'
t_LEFTBRACES = r'\{'
t_SEMICOLON = r'\;'
t_LESSTHEN = r'<'
t_LESSEQUAL = r'<='
t_GREATERTHEN = r'>'
t_GREATEREQUAL = r'>='
t_NOTEQUAL = r'!='
t_COMMA = r'\,'
t_INTEGERCONST = r'\d+'
t_FLOATCONST = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"'


"""
    Essa função funciona da seguinte maneira: 
    - A função t_NEWLINE é responsável por reconhecer quebra de linha no código fonte.
    - A expressão regular r'\n' reconhece qualquer quebra de linha.
    - A função incrementa o contador de linhas e retorna o token t.
"""
def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    print("Nova linha")
    return t

"""
    Essa função funciona da seguinte maneira: 
    - A função t_error é responsável por tratar erros léxicos no código fonte.
    - A função imprime uma mensagem de erro e retorna None.
"""
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# entrada do arquivo com o código fonte como argumento usando argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analisador Léxico')
    parser.add_argument('arquivo', type=argparse.FileType('r'), help='Arquivo de entrada')
    args = parser.parse_args()
    file_text_utf8 = args.arquivo.read()
    # converte pra string
    file_text_utf8 = str(file_text_utf8)
    print(file_text_utf8)
    # Construção do analisador léxico
    lexer = lex.lex()
    lexer.input(file_text_utf8)

    # Tokenização
    for tok in lexer:
        print(tok)