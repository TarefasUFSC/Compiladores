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
    'void' : 'VOID',
    'char' : 'CHAR',
    'struct' : 'STRUCT',
    'typedef' : 'TYPEDEF',
}

# Demais Tokens
tokens = [
    'ATTRIBUTION', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LESSTHEN', 'LESSEQUAL', 'GREATERTHEN', 'GREATEREQUAL', 'NOTEQUAL', 'EQUALTO', 'LOGICALAND', 'LOGICALOR', 'LOGICALNOT', 'BITWISEAND', 'BITWISEOR', 'BITWISEXOR', 'BITWISENOT', 'LEFTSHIFT', 'RIGHTSHIFT',
    'COMMA', 'SEMICOLON', 'LEFTPAREN', 'RIGHTPAREN', 'RIGHTBRACES', 'LEFTBRACES', 'MODULE', "INCREMENT", "DECREMENT", "POINTER", "DOT",
    'ID', 'INTEGERCONST', 'FLOATCONST', 'STRING' ,
    'INCLUDECONTENT', 'INCLUDE', 'DEFINE'
] + list(reserved.values())

t_ignore = ' \t\n'

def t_ignore_COMMENT(t):
    r'//.*\n'
    pass
def t_ignore_COMMENTBLOCK(t):
    r'/\*(.|\n)*?\*/'
    pass

"""
    Essa função funciona da seguinte maneira: 
    - A função t_ID é responsável por reconhecer identificadores no código fonte.
    - A expressão regular r'[a-zA-Z][a-zA-Z0-9]*' reconhece qualquer sequência de letras seguida ou não de números.
    - A função retorna o token t.
"""
def t_ID(t):
    r'[_a-zA-Z][_a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

"""
    Essa função funciona da seguinte maneira:
    - pega todo o conteudo dentro de <> na linha em que contem a palavra include
"""
def t_INCLUDECONTENT(t):
    r'<.*?>'
    return t

def t_INCLUDE(t):
    r'\#include'
    return t

def t_DEFINE(t):
    r'\#define'
    return t

t_LOGICALAND = r'&&'
t_LOGICALOR = r'\|\|'
t_LOGICALNOT = r'!'
t_EQUALTO = r'=='
t_ATTRIBUTION = r'='
t_BITWISEAND = r'&'
t_BITWISEOR = r'\|'
t_BITWISEXOR = r'\^'
t_BITWISENOT = r'~'
t_LEFTSHIFT = r'<<'
t_RIGHTSHIFT = r'>>'
t_LESSTHEN = r'<'
t_LESSEQUAL = r'<='
t_GREATERTHEN = r'>'
t_GREATEREQUAL = r'>='
t_NOTEQUAL = r'!='
t_MODULE = r'%'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_POINTER = r'->'
t_DOT = r'\.'


t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_LEFTPAREN = r'\('
t_RIGHTPAREN = r'\)'
t_RIGHTBRACES = r'\}'
t_LEFTBRACES = r'\{'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'


t_INTEGERCONST = r'\d+'
t_FLOATCONST = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"'






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