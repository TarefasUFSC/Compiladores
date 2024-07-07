from ply import *


class Variable():
    def __init__(self, value, type, context):
        self.type = type
        self.value = value
        self.context = str(context)

class VariableTable():
    def __init__(self):
        self.variables = []
        self.col_size = 10
        self.cols = ["Nome".ljust(self.col_size) ,"Tipo".ljust(self.col_size), "Contexto".ljust(self.col_size)]

    def append(self, variable):
        for var in self.variables:
            if var.value == variable.value:
                print(f"\033[91mErro: Variável {p[2]} já foi declarada\033[0m")
                exit(1)
        self.variables.append(variable)
    
    def __str__(self):
        col_size = 10
        content = ""
        for col in self.cols:
            content = content + col + " | "
        content = content + "\n"
        content = content+ ("-" * (col_size * 3 +8)) + "\n"
        for variable in self.variables:
            content += variable.value.ljust(col_size) + " | " + variable.type.ljust(col_size) + " | " + variable.context.ljust(col_size) + " |\n"

        return content

class SyntaxRules():
    variables_table = VariableTable()
    context_level = 0

    def print_variables_table(self):
        print("\n\nTabela de variáveis:")
        print(self.variables_table)

    def p_inicial(self,p):
        '''inicial : declaracoes_func inicial
                    | includes inicial
                    | defines inicial
                    | declaracoes inicial
                    | empty'''
        
        
    def p_includes(self,p):
        '''includes : INCLUDE INCLUDECONTENT includes
                    | INCLUDE STRING includes
                    | empty'''
        
        

    def p_defines(self,p):
        '''defines : DEFINE ID constants defines
                    | empty'''
        


    def p_declaracoes_func(self,p):
        '''declaracoes_func : tipos func_name LEFTPAREN declaracao_parametros RIGHTPAREN contexto declaracoes_func
                            | tipos func_name LEFTPAREN declaracao_parametros RIGHTPAREN contexto SEMICOLON declaracoes_func
                            | empty'''
        

    
    
    def p_func_name(self,p):
        '''func_name : ID
                    | MAIN'''
        
        

    def p_tipos(self,p):
        '''tipos : INT 
                | CHAR 
                | FLOAT
                | VOID
                | STRING
                | ID'''
        p[0] = p[1]
        
        

    def p_declaracao_parametros(self,p):
        '''declaracao_parametros : tipos ID COMMA declaracao_parametros
                    | tipos ID 
                    | empty'''
        
        

    def p_contexto(self,p):
        '''contexto : LEFTBRACES context_content RIGHTBRACES'''
        print("diminuindo contexto")
        context_counter = 0
        for i in p.stack:
            if i.type == "LEFTBRACES":
                context_counter += 1
            if i.type == "RIGHTBRACES":
                context_counter -= 1
        
        self.context_level = context_counter
        print(f"Contexto: {context_counter}")
        # remove variáveis do contexto que são maior que o contexto atual
        self.variables_table.variables = [var for var in self.variables_table.variables if int(var.context) <= self.context_level]
        self.print_variables_table()
        

    def p_context_content(self,p):
        '''context_content : conteudo
                            | conteudo retorno'''

    def p_retorno(self,p):
        '''retorno : RETURN valor SEMICOLON
                    | RETURN SEMICOLON
                    | RETURN func_call SEMICOLON'''
        
        

    def p_empty(self,p):
        '''empty :'''
        

    def p_conteudo(self,p):
        '''conteudo : declaracoes conteudo
                    | comandos conteudo
                    | empty'''
        

    def p_declaracoes(self,p):
        '''declaracoes : tipos definicoes SEMICOLON
                        | TYPEDEF STRUCT contexto ID SEMICOLON'''
        context_counter = 0
        for i in p.stack:
            if i.type == "LEFTBRACES":
                context_counter += 1
        self.context_level = context_counter
        print(f"Contexto: {context_counter}")
        if(len(p) == 4):
            self.variables_table.append(Variable(p[2], p[1], self.context_level))
        # else:
        # TODO: Implementar criação de tipos
        #     self.variables_table.append(Variable(p[4], "STRUCT", self.context_level))
        self.print_variables_table()

        
        
    def p_definicoes(self,p):
        '''definicoes : ID 
                    | ID ATTRIBUTION operacao
                    | ID ATTRIBUTION LEFTBRACES valores RIGHTBRACES
                    | ID COMMA definicoes
                    | ID ATTRIBUTION func_call
                    | ID ATTRIBUTION valor COMMA definicoes'''
        
        p[0] = p[1]


    def p_valor(self,p):
        '''valor : constants
                | ID
                | atributo'''
        
        p[0] = p[1]     
        

    
    def p_operadores(self,p):
        '''operadores : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | MODULE'''
    
        p[0] = p[1]

    def p_operacao(self,p):
        '''operacao : valor operadores operacao
                    | valor '''
        
        
        

    def p_operacao_especial(self,p):
        '''operacao_especial : ID INCREMENT
                            | ID DECREMENT'''

        

    def p_atributo(self,p):
        '''atributo : ID DOT ID
                    | ID POINTER ID
                    | ID DOT atributo
                    | ID POINTER atributo'''

           
        

    def p_constants(self,p):
        '''constants : INTEGERCONST
                    | FLOATCONST
                    | STRING
                    | CHARCONST'''
        
        



        

    def p_comandos(self,p):
        '''comandos : atribuicao SEMICOLON
                    | operacao_especial SEMICOLON
                    | loop
                    | condicional
                    | func_call SEMICOLON
                    | palavra_reservada SEMICOLON'''
        
    
    def p_valores(self,p):
        '''valores : valor COMMA valores
                    | valor'''
        

    def p_atribuicao(self,p):
        '''atribuicao : ID ATTRIBUTION operacao
                    | ID ATTRIBUTION valor
                    | ID ATTRIBUTION LEFTBRACES valores RIGHTBRACES
                    | ID ATTRIBUTION func_call
                    | operacao_especial'''
        
    

    def p_loop(self,p):
        '''loop : while
                | for'''
        

    def p_while(self,p):
        '''while : WHILE LEFTPAREN condicao RIGHTPAREN contexto'''
        

    def p_for(self,p):
        '''for : FOR LEFTPAREN tipos ID SEMICOLON condicao SEMICOLON atribuicao RIGHTPAREN contexto
                | FOR LEFTPAREN tipos ID ATTRIBUTION valor SEMICOLON condicao SEMICOLON atribuicao RIGHTPAREN contexto'''
        

    def p_condicional(self,p):
        '''condicional : IF LEFTPAREN condicao RIGHTPAREN contexto
                        | IF LEFTPAREN condicao RIGHTPAREN contexto ELSE contexto'''
        

    def p_condicao(self,p):
        '''condicao : operacao comparador valor
                    | LEFTPAREN condicao RIGHTPAREN
                    | condicao comparador condicao'''
        

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
        

    def p_func_call(self,p):
        '''func_call : ID LEFTPAREN parametros_chamada RIGHTPAREN'''

    def p_parametros_chamada(self,p):
        '''parametros_chamada : valor
                            | ID
                            | operacao
                            | valor COMMA parametros_chamada
                            | operacao COMMA parametros_chamada
                            | empty'''
    
        
        

    def p_palavra_reservada(self,p):
        '''palavra_reservada : BREAK
                            | CONTINUE'''
        

    def p_error(self,p):
        if p:
            # print com cor vermelha
            print(f"\033[91mSyntax error at line {p.lineno} at '{p}'\033[0m")
        else:
            print(f"\033[91mSyntax error at EOF\033[0m")


