from ply import *

class SyntaxRules():
    def p_inicial(self,p):
        '''inicial : declaracoes_func inicial
                    | includes inicial
                    | defines inicial
                    | declaracoes
                    | empty'''
        print(f"Reconheci INICIAL: p=", end="")
        for i in p:
            print(i, end=" ")
        print()
        pass
    def p_includes(self,p):
        '''includes : INCLUDE INCLUDECONTENT includes
                    | INCLUDE STRING includes
                    | empty'''
        print(f"Reconheci Includes: p=", end="")
        for i in p:
            print(i, end=" ")
        print()
        pass

    def p_defines(self,p):
        '''defines : DEFINE ID constants defines
                    | empty'''
        pass


    def p_declaracoes_func(self,p):
        '''declaracoes_func : tipos func_name LEFTPAREN declaracao_parametros RIGHTPAREN contexto SEMICOLON declaracoes_func
                            | empty'''
        print(f"Reconheci Declarações Func: p=", end="")
        for i in p:
            print(i, end=" ")
        print()
        pass

    
    
    def p_func_name(self,p):
        '''func_name : ID
                    | MAIN'''
        print(f"Reconheci Func Name: p=", end="")
        for i in p:
            print(i, end=" ")
        print()
        pass

    def p_tipos(self,p):
        '''tipos : INT 
                | CHAR 
                | FLOAT
                | VOID
                | STRING'''
        pass

    def p_declaracao_parametros(self,p):
        '''declaracao_parametros : tipos ID
                    | tipos ID COMMA declaracao_parametros
                    | empty'''
        print(f"Reconheci declaracao_Parametros:")
        pass

    def p_contexto(self,p):
        '''contexto : LEFTBRACES conteudo RIGHTBRACES
                    | LEFTBRACES conteudo retorno RIGHTBRACES'''
        print(f"Reconheci Contexto", p)
        pass

    def p_retorno(self,p):
        '''retorno : RETURN valor SEMICOLON
                    | RETURN SEMICOLON'''
        print(f"Reconheci Retorno: p=", end="")
        for i in p:
            print(i, end=" ")
        print()
        pass

    def p_empty(self,p):
        '''empty :'''
        pass

    def p_conteudo(self,p):
        '''conteudo : declaracoes conteudo
                    | comandos conteudo
                    | empty'''
        print(f"Reconheci Conteudo. p=", end="")
        for i in p:
            print(i, end=" ")
        print()
        pass

    def p_declaracoes(self,p):
        '''declaracoes : tipos definicoes SEMICOLON
                        | TYPEDEF STRUCT contexto ID SEMICOLON'''
        print(f"Reconheci Declarações")
        pass
    def p_definicoes(self,p):
        '''definicoes : ID 
                    | ID ATTRIBUTION valor
                    | ID COMMA definicoes
                    | ID ATTRIBUTION valor COMMA definicoes'''
        print(f"Reconheci Definições")
        pass

    def p_valor(self,p):
        '''valor : constants
                | ID
                | atributo'''
        pass
    def p_atributo(self,p):
        '''atributo : ID DOT ID
                    | ID POINTER ID
                    | ID DOT atributo
                    | ID POINTER atributo'''
        pass

    def p_constants(self,p):
        '''constants : INTEGERCONST
                    | FLOATCONST
                    | STRING
                    | CHARCONST'''
        pass

    def p_comandos(self,p):
        '''comandos : atribuicao SEMICOLON
                    | loop
                    | condicional SEMICOLON
                    | func_call SEMICOLON
                    | palavra_reservada SEMICOLON'''
        print(f"Reconheci Comandos")
        pass

    def p_atribuicao(self,p):
        '''atribuicao : ID ATTRIBUTION valor'''
        pass

    def p_loop(self,p):
        '''loop : while
                | for'''
        print(f"Reconheci Loop")
        pass

    def p_while(self,p):
        '''while : WHILE LEFTPAREN condicao RIGHTPAREN contexto'''
        print(f"Reconheci While")
        pass

    def p_for(self,p):
        '''for : FOR LEFTPAREN tipos ID SEMICOLON condicao SEMICOLON atribuicao RIGHTPAREN contexto
                | FOR LEFTPAREN tipos ID ATTRIBUTION valor SEMICOLON condicao SEMICOLON atribuicao RIGHTPAREN contexto'''
        pass

    def p_condicional(self,p):
        '''condicional : IF LEFTPAREN condicao RIGHTPAREN contexto
                        | IF LEFTPAREN condicao RIGHTPAREN contexto ELSE contexto'''
        pass

    def p_condicao(self,p):
        '''condicao : valor comparador valor
                    | LEFTPAREN condicao RIGHTPAREN
                    | condicao comparador condicao'''
        pass

    def p_comparador(self,p):
        '''comparador : EQUALTO
                    | LESSTHEN
                    | GREATERTHEN
                    | LESSEQUAL
                    | GREATEREQUAL
                    | NOTEQUAL
                    | LOGICALAND
                    | LOGICALOR
                    | LOGICALNOT'''
        pass

    def p_func_call(self,p):
        '''func_call : ID LEFTPAREN parametros_chamada RIGHTPAREN'''
        print(f"Reconheci Func Call")
        pass

    def p_parametros_chamada(self,p):
        '''parametros_chamada : valor
                            | ID
                            | valor COMMA parametros_chamada
                            | empty'''
        pass

    def p_palavra_reservada(self,p):
        '''palavra_reservada : BREAK
                            | CONTINUE'''
        print(f"Reconheci Palavra Reservada")
        pass

    def p_error(self,p):
        if p:
            print(f"Syntax error at line {p.lineno}, token={p.type}")
        else:
            print("Syntax error at EOF")


