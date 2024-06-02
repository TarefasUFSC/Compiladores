# ATIVIDADE PRÁTICA - reconhecedor de estruturas em C

from ply import *

# Palavras reservadas <palavra>:<TOKEN>
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'int' : 'INT',
    'main' : 'MAIN',
    'float' : 'FLOAT'
}

# Demais TOKENS
tokens = [
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'LPAREN', 'RPAREN', 'LT', 'LE', 'GT', 'GE', 'NE',
    'COMMA', 'SEMI', 'INTEGER', 'FLOAT_N', 'STRING',
    'ID', 'NEWLINE', 'SEMICOLON', 'RBRACES', 'LBRACES'
] + list(reserved.values())

t_ignore = ' \t'

def t_REM(t):
    r'REM .*'
    return t

# Definição de Identificador com expressão regular r'<expressão>'
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
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RBRACES = r'\}'
t_LBRACES = r'\{'
t_SEMICOLON = r'\;'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'!='
t_COMMA = r'\,'
t_SEMI = r';'
t_INTEGER = r'\d+'
t_FLOAT_N = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# Constroi o analisador léxico
lexer = lex.lex()


filepath = "./teste1.c"
file_text_utf8 = open(filepath, 'r').read()
# converte pra string
file_text_utf8 = str(file_text_utf8)
print(file_text_utf8)
# Construção do analisador léxico
lexer = lex.lex()
lexer.input(file_text_utf8)

# Tokenização
for tok in lexer:
     print(tok)
