#
# Exemplo - Como usar os comando Break e Continue
#
print()
print("----- Usando o comando Break -----")

def loopBreak():
    for x in range(5, 10):
        if x == 7:
            break
        print("O valor de x é: ", x)

loopBreak()

print()
print("----- Usando o comando Continue -----")

def loopContinue():
    for x in range(5, 10):
        if x == 7:
            continue
        print("O valor de x é: ", x)

loopContinue()
