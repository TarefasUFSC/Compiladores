from ply import *

class TokenRules():
    def __init__(self):
        self.reserved = {
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

        self.tokens = [
            'ATTRIBUTION', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
            'LESSTHEN', 'LESSEQUAL', 'GREATERTHEN', 'GREATEREQUAL', 'NOTEQUAL', 'EQUALTO', 'LOGICALAND', 'LOGICALOR', 'LOGICALNOT', 'BITWISEAND', 'BITWISEOR', 'BITWISEXOR', 'BITWISENOT', 'LEFTSHIFT', 'RIGHTSHIFT',
            'COMMA', 'SEMICOLON', 'LEFTPAREN', 'RIGHTPAREN', 'RIGHTBRACES', 'LEFTBRACES', 'MODULE', "INCREMENT", "DECREMENT", "POINTER", "DOT",
            'ID', 'INTEGERCONST', 'FLOATCONST', 'CHARCONST', 'STRING' ,
            'INCLUDECONTENT', 'INCLUDE', 'DEFINE'
        ] + list(self.reserved.values())

    
    t_ignore = ' \t'

    def t_ignore_LINEBREAK(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        pass

    def t_ignore_COMMENT(self,t):
        r'//.*'
        pass

    def t_ignore_COMMENTBLOCK(self,t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')
        pass


    """
        Essa função funciona da seguinte maneira: 
        - A função t_ID é responsável por reconhecer identificadores no código fonte.
        - A expressão regular r'[a-zA-Z][a-zA-Z0-9]*' reconhece qualquer sequência de letras seguida ou não de números.
        - A função retorna o token t.
    """
    def t_ID(self,t):
        r'[_a-zA-Z][_a-zA-Z0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t

    """
        Essa função funciona da seguinte maneira:
        - pega todo o conteudo dentro de <> na linha em que contem a palavra include
    """
    def t_INCLUDECONTENT(self,t):
        r'<.*?>'
        return t

    def t_INCLUDE(self,t):
        r'\#include'
        return t

    def t_DEFINE(self,t):
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
    t_CHARCONST = r'\'[a-zA-Z0-9]\''
    """
        Essa função funciona da seguinte maneira: 
        - A função t_error é responsável por tratar erros léxicos no código fonte.
        - A função imprime uma mensagem de erro e retorna None.
    """
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
