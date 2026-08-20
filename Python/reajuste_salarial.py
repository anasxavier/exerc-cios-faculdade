'''
Dados o nome e o salario atual de um funcionario, faça um programa em python
para funcinarios de acordo com a faixa de salario:
para salario < 2,500, tem aumento 15.45%
para salario >= 2,500, mas < 5,500 tem aumento 10.34%
para salario >= 5,500, tem aumento 8.55%
'''
#Criamos um subprograma para calcular salario com aumento
def cal_salarioAtualizado(nome,salario):
  if (salario<2500.0):
    aumento = salario*15.45/100
    sal_novo = salario + aumento
    print(f"{nome} seu salario com 15.45% de aumento: {sal_novo:.2f}")
  elif (salario<5500.0):
      aumento = salario*10.34/100
      sal_novo = salario + aumento
      print(f"{nome} seu salario com 10.34% de aumento: {sal_novo:.2f}")
  else:
      aumento = salario*8.55/100
      sal_novo = salario + aumento
      print(f"{nome} seu salario com 8.55% de aumento: {sal_novo:.2f}")

#Programa principal
nome = input("Informe seu nome: ")
salario = float(input("Informe seu salário atual: R$ "))
cal_salarioAtualizado(nome,salario)
