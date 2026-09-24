#Este Programa em Python é para calcular a nota de uma disciplina
"""
Entrada de dados:
1) Exercício de fixação (15%)
2) Nota teste de desempenho (25%)
3) Prova eletrônica (60%)
Saída de dados
A média final
"""

#Entrada de dados
nomeDisciplina = input("Informe o nome da disciplina: ")
exer = float(input("Informe sua nota dos exercícios de fixação: "))
teste = float(input("Informe sua nota do teste de desempenho: "))
prova = float(input("Informe sua nota da prova eletrônica: "))

#Calcular a média final
mediaF = exer*0.15 + teste*0.25 + prova*0.60

#Saída: Mostrar resultado na tela
print (f"Disciplina: {nomeDisciplina}")
print(f"Média Final: {mediaF:.2f}")
