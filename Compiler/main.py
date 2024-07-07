
import argparse

from analyser.compiler import Compiler



# entrada do arquivo com o código fonte como argumento usando argparse
if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Analisador Léxico')
    # parser.add_argument('arquivo', type=string, help='Arquivo de entrada')
    # args = parser.parse_args()
    file_name = "../c_tests/teste_personalizado.c"

    # open file
    file = open(file_name, 'r')
    file_text_utf8 = file.read()

    # converte pra string
    file_text_utf8 = str(file_text_utf8)
    print(file_text_utf8)
    # Construção do analisador léxico
    
    compiler = Compiler()

    # o parser sintatico chama o lexer by default, então removi isso aqui. Se quiser depurar os tokens ai tem que descomentar
    # compiler.input(file_text_utf8)

    # # Tokenização
    # for token in compiler.tokenize():
    #     print(token)
    

    # ---
    # chama o parser
    compiler.parse(file_text_utf8)