#Este progrma para testar varias utilidade do comando for
# 1)
def contaNumPar():
    soma = 0 #funciona como acumulador
    # range(100): uma sequncia de numeros inteiros de 0 a 99
    for num in range(10):
        if (num % 2 == 0): #verificar se mum Ã© par
              soma += num
    print(soma)

def manipularLista():
    #Uma lista de nomes
    nomes_professor = ["Cao","Magalhoes","Lucio","Nelson","Vitor"]
    print("Nomes armazenados na lista:")
    for nome in nomes_professor:
        print(nome)
    print("Nomes armazenados na lista:")
    #A variavel funciona como contador
    for cont in range(len(nomes_professor)):
        print(nomes_professor[cont])

def testarRange():
    #range(1,10,2): o nÃºmeo inicia com 1, e ate 9
    #cada iteraÃ§Ã£o (repetiÃ§Ã£o) a variÃ¡vel cont incrementa 2
    for cont in range(1,10,2):
        print(f"{cont}: Seja bem a linguagem Python")

def testarString():
    texto = "Linguagem Python"
    textoLista = []
    for letra in texto:
        textoLista.append(letra)
    print(textoLista)
       
#programa principal
#contaNumPar()
#manipularLista()
#testarRange()
#testarString()
#Para funcionar retire os #
