
import argparse

from analyser.compiler import Compiler



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
    
    compiler = Compiler()
    compiler.input(file_text_utf8)

    # Tokenização
    for token in compiler.tokenize():
        print(token)
    
    # chama o parser
    compiler.parse(file_text_utf8)