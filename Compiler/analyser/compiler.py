from ply import *
from analyser.lexer import TokenRules
from analyser.syntaxer import SyntaxRules

class Compiler(TokenRules, SyntaxRules):
    def __init__(self):
        TokenRules.__init__(self)
        self._build()
        
    def _build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.yacc = yacc.yacc(module=self, 
                              debug=0,
                              debugfile="yacc_debug.txt")

    def input(self,data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()
    
    def tokenize(self):
        """yield tokens"""
        while True:
            tok = self.token()
            if not tok:
                break
            yield tok
    def parse(self,data):
        self.yacc.parse(data)

    