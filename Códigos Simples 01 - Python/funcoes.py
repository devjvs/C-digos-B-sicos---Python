#
# Arquivo - Exemplos de Funções
#

# Definindo uma função básica
def func1():
    print("Eu sou uma função")

func1()

# Função que recebe argumentos
def func2(arg1, arg2):
    print(arg1 + " " + arg2)

func2("Dani" , "Monteiro")

# Função que retorna um valor
def cubo(x):
    return x * x * x

f = cubo(3)
print(f)
print(cubo(2))

