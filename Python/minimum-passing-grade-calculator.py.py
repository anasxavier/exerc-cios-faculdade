#Este Programa em Python é para calcular a nota de uma disciplina
"""
Entrada de dados:
1) Exercício de fixação (15%)
2) Nota teste de desempenho (25%)
3) Prova eletrônica (60%)
Saída de dados
Nota Mínima Prova
"""

#Entrada de dados
nomeDisciplina = input("Informe o nome da disciplina: ")
exer = float(input("Informe sua nota dos exercícios de fixação: "))
teste = float(input("Informe sua nota do teste de desempenho: "))


#Calcular a média final
notaMinProva = (6.0 - (exer*0.15 + teste*0.25))/0.60

#Saída: Mostrar resultado na tela
print (f"A nota mínima para passar na prova: {notaMinProva:.2f}")
