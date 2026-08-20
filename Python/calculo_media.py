#Este Programa em Python é para calcular a nota de uma disciplina
"""
Entrada de dados:
1) Exercício de fixação (15%)
2) Nota teste de desempenho (25%)
3) Prova eletrônica (60%)p
Saída de dados
A média final
"""

def calcular_media(nota1, nota2, nota3):
    m = nota1*0.15 + nota2*0.25 + nota3*0.60
    return m
    
#Entrada de dados
nomeDisciplina01 = input("Informe o nome da disciplina: ")
exer01 = float(input("Informe sua nota dos exercícios de fixação: "))
teste01 = float(input("Informe sua nota do teste de desempenho: "))
prova01 = float(input("Informe sua nota da prova eletrônica: "))

#Chamando subprograma calcular_media(...)
mediaF01 = calcular_media(exer01, teste01, prova01)

#Saída: Mostrar resultado na tela
print (f"\nDisciplina: {nomeDisciplina01}")
print(f"Média Final: {mediaF01:.2f}\n")


#Entrada de dados
nomeDisciplina02 = input("Informe o nome da disciplina: ")
exer02 = float(input("Informe sua nota dos exercícios de fixação: "))
teste02 = float(input("Informe sua nota do teste de desempenho: "))
prova02 = float(input("Informe sua nota da prova eletrônica: "))

#Chamando subprograma calcular_media(...)
mediaF02 = calcular_media(exer02, teste02, prova02)

#Saída: Mostrar resultado na tela
print (f"\nDisciplina: {nomeDisciplina02}")
print(f"Média Final: {mediaF02:.2f}")
