
# Declarando e inicializando uma variável
f = 0 
print(f)

# Declarando a mesma variável novamente
f = "abc"
print(f)

# Gerando um erro, tentando unir variãveis de tipos diferentes
print("Isto é uma string " + str(123))

# Variável Global X Variável local 
def AlgumaFuncao():
    global f
    f = "def"
    print(f)

AlgumaFuncao()
print(f)