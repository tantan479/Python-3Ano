# 1 - Revisão de valores e Tipos!

type(20)
#Resposta no Console: <class 'int'> (INTEIRO)

type(15.6)
#Resposta no Console: <class 'float'> (PONTO FLUTUANTE)

type("15.6")
#Resposta no Console: <class 'str'> (STRING)


# Variáveis
# O que são variáveis são espaços de memória, nomeados, que armazenam uma informação.

# Exemplo 01
mensagem = "Minha primeira variável em Python!"
print("mensagem")

# Exemplo 02
numero = 25
print(numero)

# Exemplo 03
pi = 3.14159
print(pi)


# Manipular strings.
string01 = "teste01"
string02 = "teste02"

# Exemplo 01
print(string01)

# Exemplo 02
print(string01 + string02)

# Exemplo 03
string01*3
'teste01teste01teste01'


# Conversão entre tipos
minuto = 59
float(minuto)/60


# Funções criadas pelo usuário
#primeira letra do nome deve ser minuscula
def imprimeEmDobro(spam):
    print(spam, spam)

imprimeEmDobro(10)
imprimeEmDobro('teste')
imprimeEmDobro('teste'*3)


# Estruturas condicionais e operadores lógicos

# Esta função verifica se o numero é maior que 5


def maior(x):
    if x > 5:
        print("O número é maior do que 5") #TRUE
    else:
        print("O numero é menor ou igual a 5") #FALSE