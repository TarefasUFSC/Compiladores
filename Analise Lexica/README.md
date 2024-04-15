# Analisador Léxico

Este projeto implementa um analisador léxico para arquivos escritos em linguagem C, identificando tokens como palavras reservadas, identificadores, números e operadores.

## Requisitos

- Python 3.11

## Instruções de Uso

### Usando Pipenv

1. **Configuração do Ambiente Virtual:**

   - Execute `pipenv shell` para criar e ativar o ambiente virtual.
   - Execute `pipenv install` para instalar as dependências necessárias.

### Sem Ambiente Virtual

1. **Instalação de Dependências:**

   - Instale as dependências necessárias com:
     ```
     pip install -r requirements.txt
     ```

### Execução

- Execute o analisador léxico com o comando:
  ```
  python main.py "<CAMINHO PARA O ARQUIVO EM C>"
  ```

## Funcionamento do Analisador Léxico

O analisador inicia pela leitura do arquivo em C especificado na linha de comando. Usando as definições na classe `TokenRules`, o programa identifica os componentes léxicos baseados nas regras pré-definidas para tokens e palavras reservadas. A biblioteca `ply` é usada para facilitar a análise e tokenização do arquivo de entrada.
