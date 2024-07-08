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
                print(f"\033[91mErro: Variável {var.value} já foi declarada\033[0m")
                exit(1)
        self.variables.append(variable)

    def get_by_name(self, name):
        for var in self.variables:
            if var.value == name:
                return var
        return None
    
    def __str__(self):
        content = ""
        for col in self.cols:
            content = content + col + " | "
        content = content + "\n"
        content = content+ ("-" * (self.col_size * 3 +8)) + "\n"
        for variable in self.variables:
            content += variable.value.ljust(self.col_size) + " | " + variable.type.ljust(self.col_size) + " | " + variable.context.ljust(self.col_size) + " |\n"
        return content


class StructAttribute():
    def __init__(self, attr_name, attr_type):
        self.attr_name = attr_name
        self.attr_type = attr_type
class Struct():
    def __init__(self, value, attributes):
        self.value = value
        self.attributes = attributes
    def attr_list_str(self):
        content = "{"
        for attr in self.attributes:
            content += attr.attr_name + ":" + attr.attr_type + ", "
        content = content[:-2] + "}"
        return content
    
    def get_attr_by_name(self, name):
        for attr in self.attributes:
            if attr.attr_name == name:
                return attr
        return None
    
    def check_attr(self, name):
        for attr in self.attributes:
            if attr.attr_name == name:
                return True
        return False
    
    def get_types_list(self):
        types = []
        for attr in self.attributes:
            types.append(attr.attr_type)
        return types

class StructsTable():
    def __init__(self):
        self.structs = []
        self.col_size = 10
        self.cols = ["Nome".ljust(self.col_size) ,"Atributos".ljust(self.col_size)]

    def append(self, struct):
        for strct in self.structs:
            if strct.value == struct.value:
                print(f"\033[91mErro: Struct {strct.value} já foi declarada\033[0m")
                exit(1)
        self.structs.append(struct)

    def get_by_name(self, name):
        for struct in self.structs:
            if struct.value == name:
                return struct
        return None
    
    def __str__(self):
        biggest_len = 0
        for struct in self.structs:
            if len(struct.attr_list_str()) > biggest_len:
                biggest_len = len(struct.attr_list_str())
        self.col_size = biggest_len + 2
        content = ""
        for col in self.cols:
            content = content + col.ljust(self.col_size) + " | "
        content = content + "\n"
        content = content+ ("-" * (self.col_size * 2 +5)) + "\n"
        for struct in self.structs:
            content += struct.value.ljust(self.col_size) + " | " + struct.attr_list_str().ljust(self.col_size) + " |\n"
        return content
    

class Funtion():
    def __init__(self, name, type, params):
        self.type = type
        self.name = name
        self.params = params
        print(f"Função {name} com tipo {type} e parâmetros {params}")
    def get_params_str(self):
        content = ""
        for param in self.params:
            content += param + ", "
        content = content[:-2]
        return content

class Functionstable():
    def __init__(self):
        self.functions = []
        self.col_size = 10
        self.cols = ["Nome".ljust(self.col_size), "Tipo".ljust(self.col_size), "Parâmetros".ljust(self.col_size)]
    def append(self, function):
        for func in self.functions:
            if func.name == function.name:
                print(f"\033[91mErro: Função {function.name} já foi declarada\033[0m")
                exit(1)
        self.functions.append(function)
    
    def __str__(self):
        biggest_len = self.col_size
        for function in self.functions:
            if len(function.get_params_str()) > biggest_len:
                biggest_len = len(function.get_params_str())
            if len(function.name) > biggest_len:
                biggest_len = len(function.name)
        self.col_size = biggest_len + 2
        content = ""
        for col in self.cols:
            content = content + col.ljust(self.col_size) + " | "
        content = content + "\n"
        content = content+ ("-" * (self.col_size * 3 +8)) + "\n"
        for function in self.functions:
            content += function.name.ljust(self.col_size) + " | " + function.type.ljust(self.col_size) + " | " + function.get_params_str().ljust(self.col_size) + " |\n"
        return content

    def get_by_name(self, name):
        for function in self.functions:
            if function.name == name:
                return function
        return None


class SyntaxRules():
    variables_table = VariableTable()
    structs_table = StructsTable()
    funtions_table = Functionstable()
    context_level = 0

    def print_variables_table(self):
        print("\n\nTabela de variáveis:")
        print(self.variables_table)
    
    def print_structs_table(self):
        print("\n\nTabela de structs:")
        print(self.structs_table)

    def print_functions_table(self):
        print("\n\nTabela de funções:")
        print(self.funtions_table)

    def p_inicial(self,p):
        '''inicial : declaracoes_func inicial
                    | includes inicial
                    | defines inicial
                    | declaracoes inicial
                    | empty'''
        print("inicial")
        
    def p_includes(self,p):
        '''includes : INCLUDE INCLUDECONTENT includes
                    | INCLUDE STRING includes
                    | empty'''
        
        

    def p_defines(self,p):
        '''defines : DEFINE ID constants defines
                    | empty'''
        


    def p_declaracoes_func(self,p):
        '''declaracoes_func : tipos func_name LEFTPAREN declaracao_parametros RIGHTPAREN contexto'''
        # print em amaerelo
        print(f"Declarando função {p[2]} com tipo {p[1]} e parâmetros {p[4]}")
        function = Funtion(p[2], p[1], p[4]["type"])
        self.funtions_table.append(function)

        self.print_functions_table()

    
    
    def p_func_name(self,p):
        '''func_name : ID
                    | MAIN'''
        # print em amarelo
        p[0] = p[1]
        
        

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
        self.context_level += 1
        if(len(p) == 3):
            self.variables_table.append(Variable(p[2], p[1], self.context_level))
            p[0] = {"type": [p[1]]}
        elif(len(p) == 5):
            p_0_types = [p[1]]
            # checa se é uma lista de tipos
            if isinstance(p[4]["type"], list):
                for type in p[4]["type"]:
                    p_0_types.append(type)
            self.variables_table.append(Variable(p[2], p[1], self.context_level))
            p[0] = {"type":  p_0_types}   
        else:
            p[0] = {"type": []}
        

    def p_contexto(self,p):
        '''contexto : LEFTBRACES context_content RIGHTBRACES'''
        context_counter = 0
        for i in p.stack:
            if i.type == "LEFTBRACES":
                context_counter += 1
            if i.type == "RIGHTBRACES":
                context_counter -= 1
        
        self.context_level = context_counter
        # remove variáveis do contexto que são maior que o contexto atual
        self.variables_table.variables = [var for var in self.variables_table.variables if int(var.context) <= self.context_level]
        # self.print_variables_table()
        

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
                        | TYPEDEF STRUCT contexto_struct ID SEMICOLON'''
        context_counter = 0
        for i in p.stack:
            if i.type == "LEFTBRACES":
                context_counter += 1
        self.context_level = context_counter
        if(len(p) == 4):
            # checa o tipo
            if(isinstance(p[2]["type"],list)):
                for new_var in p[2]["type"]:
                    if new_var["name"] is not None:
                        p2_type = self.get_value_type(new_var["type"])
                        p1_type = p[1]
                        if(self.structs_table.get_by_name(p1_type) is not None):
                            p1_type = self.structs_table.get_by_name(p1_type).get_types_list()
                        
                        if p2_type is not None:
                            if p1_type != p2_type:
                                print(f"\033[91mErro: Tipo {p[1]} não é compatível com {p2_type}. Erro na linha {p.lineno(3)}\033[0m")
                                exit(1)
                    self.variables_table.append(Variable(new_var["name"], p[1], self.context_level))
        # else:
        else:
            attributes = []
            for attr in p[3]["attr"]:
                attributes.append(StructAttribute(attr["name"], attr["type"]))
            self.structs_table.append(Struct(p[4], attributes))



    def p_contexto_struct(self,p):
        '''contexto_struct : LEFTBRACES struct_content RIGHTBRACES'''
        p[0] = p[2]

    def p_struct_content(self,p):
        '''struct_content : tipos ID SEMICOLON struct_content
                        | tipos ID SEMICOLON
                        | empty'''
        if len(p) == 4:
            p[0] = {"attr": [{"name": p[2], "type": p[1]}]}
        elif len(p) == 5:
            attrs_p4 = [{"name": p[2], "type": p[1]}]
            if p[4] is not None:
                for attr in p[4]["attr"]:
                    attrs_p4.append(attr)
            p[0] = {"attr": attrs_p4}           



    def p_definicoes(self,p):
        '''definicoes : ID 
                    | ID atribuicao
                    | ID COMMA definicoes
                    | ID atribuicao COMMA definicoes'''
        
        types = []
        if len(p) == 4:
            types = p[3]["type"]
            types.append({"name": p[1], "type": None})
        elif len(p) == 5:
            types = p[4]["type"]
            types.append({"name": p[1], "type": None})
        else:
            types.append({"name": p[1], "type": None})
        
        p[0] = {"type": types}


    def p_comandos(self,p):
        '''comandos : ID atribuicao SEMICOLON
                    | operacao_especial SEMICOLON
                    | loop
                    | condicional
                    | func_call SEMICOLON
                    | palavra_reservada SEMICOLON'''
        print("COMANDOS")
        
    
    def p_valores(self,p):
        '''valores : valor COMMA valores
                    | valor'''
        
        if len(p) == 2:
            p[0] = {"type": p[1]["type"]}
        else:
            p_0_types = [p[1]["type"]]
            # checa se é uma lista de tipos
            if isinstance(p[3]["type"], list):
                for type in p[3]["type"]:
                    p_0_types.append(type)
            else:
                p_0_types.append(p[3]["type"])


            p[0] = {"type":  [p_0_types]}
        

    def p_atribuicao(self,p):
        '''atribuicao : ATTRIBUTION operacao
                    | ATTRIBUTION valor
                    | ATTRIBUTION LEFTBRACES valores RIGHTBRACES
                    | ATTRIBUTION func_call'''
        
        if len(p) == 5:
            if(p[3] is None):
                print(f"\033[91mErro: Atribuição de valores nulos. Erro na linha {p.lineno(1)}\033[0m")
                exit(1)
            p[0] = {"type": p[3]["type"]}
        else:
            p[0] = {"type": p[2]["type"]}


    def p_valor(self,p):
        '''valor : constants
                | ID
                | atributo'''
        
        if p.slice[1].type == "ID":
            var = self.variables_table.get_by_name(p[1])
            if var is None:
                print(f"\033[91mErro: Variável {p[1]} não foi declarada (valor). Erro na linha {p.lineno(1)}\033[0m")
                exit(1)
            p[0] = {"type": var.type}
        else:
            p[0] = {"type": p[1]["type"]}

    
    def p_operadores(self,p):
        '''operadores : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | MODULE'''
    
        p[0] = p[1]

    def get_value_type(self, value):
        if (isinstance(value, list)):
            struct_name = ""
            for i in range(len(value)):
                value_name = self.variables_table.get_by_name(value[i])
                if(isinstance(value[i], list)):
                    return value[i]
                if(value_name is None):
                    attr_name = value[i]
                    value_name = self.structs_table.get_by_name(struct_name)
                    if(value_name is None):
                        print(f"\033[91mErro: variável {attr_name} não encontrada\033[0m")
                        exit(1)
                    value_name = value_name.get_attr_by_name(attr_name)
                    if(value_name is None):
                        print(f"\033[91mErro: Atributo {attr_name} não encontrado na struct {struct_name}\033[0m")
                        exit(1)
                    value_name = value_name.attr_type
                    return value_name
                else:
                    struct_name = value_name.type
        else:
            
            return value


    def p_operacao(self,p):
        '''operacao : valor operadores operacao
                    | valor '''
        print("OPERACAO")
    
        if len(p) == 2:
            p[0] = {"type": p[1]["type"]}
        else:

            p1_type = self.get_value_type(p[1]["type"])
            p3_type = self.get_value_type(p[3]["type"])
            
            

            if p1_type != p3_type:
                print(f"\033[91mErro: Operação entre tipos incompatíveis {p[1]['type']} e {p[3]['type']} na linha {p.lineno(3)}\033[0m")
                print(f"DEV COMMENT: Só pode operação com o mesmo tipo de variável por enquanto")
                exit(1)
            p[0] = {"type": p[1]["type"]}
        
        
        

    def p_operacao_especial(self,p):
        '''operacao_especial : ID INCREMENT
                            | ID DECREMENT'''

        

    def p_atributo(self,p):
        '''atributo : ID DOT ID
                    | ID POINTER ID
                    | ID DOT atributo
                    | ID POINTER atributo'''

        
        p[0] = {"type": [p[1], p[3]]}
        

    def p_constants(self,p):
        '''constants : INTEGERCONST
                    | FLOATCONST
                    | STRING
                    | CHARCONST'''
        
        match p.slice[1].type:
            case "INTEGERCONST":
                p[0] = {"type": "int"}
            case "FLOATCONST":
                p[0] = {"type": "float"}
            case "STRING":
                p[0] = {"type": "string"}
            case "CHARCONST":
                p[0] = {"type": "char"}
            case _:
                print(f"\033[91mErro: Constante {p[1]} não reconhecida\033[0m - ISSO NÃO DEVIA TER ACONTECIDO")
                exit(1)
    

    def p_loop(self,p):
        '''loop : while
                | for'''
        print("LOOP")
        

    def p_while(self,p):
        '''while : WHILE LEFTPAREN condicao RIGHTPAREN contexto'''
        

    def p_for(self,p):
        '''for : FOR LEFTPAREN tipos ID SEMICOLON condicao SEMICOLON ID atribuicao RIGHTPAREN contexto
                | FOR LEFTPAREN tipos ID SEMICOLON condicao SEMICOLON operacao_especial RIGHTPAREN contexto
                | FOR LEFTPAREN tipos ID ATTRIBUTION valor SEMICOLON condicao SEMICOLON ID atribuicao RIGHTPAREN contexto
                | FOR LEFTPAREN tipos ID ATTRIBUTION valor SEMICOLON condicao SEMICOLON operacao_especial RIGHTPAREN contexto'''
        
        # declaração de variável
        print(f"FOR DETECTADO")
        self.context_level += 1
        self.variables_table.append(Variable(p[4], p[3], self.context_level))

    def p_condicional(self,p):
        '''condicional : IF LEFTPAREN condicao RIGHTPAREN contexto
                        | IF LEFTPAREN condicao RIGHTPAREN contexto ELSE contexto'''
        

    def p_condicao(self,p):
        '''condicao : operacao comparador valor
                    | LEFTPAREN condicao RIGHTPAREN
                    | condicao comparador condicao'''
        print("CONDIÇÃO")

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
        # TODO: Implementar  tabela de funções

        function = self.funtions_table.get_by_name(p[1])
        if function is None:
            print(f"\033[91mErro: Função {p[1]} não foi declarada\033[0m")
            exit(1)
        else:
            p[0] = {"type": function.type}


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


