#Este progrma é para calcular IMC utilizando subprograma

#Criamos um subprograma para calcular IMC recebendo peso e altura
#Nesse caso o subprograma é uma função
def calcular_imc(peso,altura):
  imc = peso/(altura*altura)#altura**2
  return imc

#Criamos um subprograma como procedimento
def resultado(imc):
  print(f"A seu imc calculado: {imc:.2f}")

def avaliacao_imc(imc):
    if (imc <= 18.5):
       print("Abaixo do peso normal")
    elif (18.6 <= imc < 24.9):
      print("Peso normal ou saudável")
    elif (25.0 <= imc < 29.9):
      print("Excesso de peso ou sobrepeso")
    elif (30.0 <= imc < 34.9):
      print("Obsidade grau 1")
    elif (35.0 <= imc < 39.9):
      print("Obsidade grau 2")
    else: #em outros casos
      print("Obsidade grau 3 ou grave")

#Programa principal
#Entrada da dados: peso e altura
peso = float (input("Informe seu peso (Kg): "))
altura = float(input("Informe sua altura (m): "))
imc_calculado = calcular_imc(peso,altura)
resultado (imc_calculado)
avaliacao_imc (imc_calculado)
