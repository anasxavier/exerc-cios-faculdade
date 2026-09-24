#Este programa é para gerar os números aleatórios para megaSena
#Criamos um subprograma para gerar os números inteiros aleatórios
import random
def MegaSena(qtd):
    cont = 1 #essa variável funcionar como contador
    while (cont <= qtd):
        #gerar um número inteiro aleatório entre 1 a 60
        num = random.randint(1,60)
        print(num)
        cont += 1 #atualizar o contador

#programa principal
qtd = int(input("Quantos números a serem gerados para megaSena? n = "))
print(f"Os {qtd} números gerados para megaSena: ")
MegaSena(qtd)
