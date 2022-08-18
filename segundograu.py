##
# Autores:
# Michel Silva

import math # Importa a biblioteca math para usar o método sqrt

# segundo grau

class SegundoGrau: # Cria a classe SegundoGrau

  def __init__(self): # Construtor da classe SegundoGrau
    print("1 - equação do segundo grau")
    print("2 - sair")
    opcao = int(input("escolha uma opção: "))
    while opcao == 1:
      # calcular a equação do segundo grau
      if opcao == 1:
        self.calculo()
        #  elif opcao == 0:
    #    return
    #  else:
    #   opcao = int(input("escolha uma opção: "))

  def calculo(self): # Método para calcular a equação do segundo grau
    # ax^2+bx+c
    a1 = int(input("entre com o valor de a: "))
    if a1 == 0:   # se a for 0, não é uma equação do segundo grau
      print("o valor de 'a' não pode ser zero") # mostra mensagem de erro
      return  # retorna para o menu
    b1 = int(input("entre com o valor de b: "))
    c1 = int(input("entre com o valor de c: "))
    self.raiz(a1, b1, c1) # chama o método raiz e passa os parâmetros a1, b1 e c1
    return

  def raiz(self, a, b, c): # Método para calcular a raiz da equação do segundo grau
    delta = b ** 2 - 4 * a * c # calcula o delta
    if delta > 0: # se delta for maior que 0, a equação tem duas raízes reais
      raiz1 = (-b + math.sqrt(delta)) / (2 * a)  # com a math
      raiz2 = (-b - (delta) ** (1 / 2)) / (2 * a)  # sem a math
      print(f"\nValor de x1 = {raiz1}") # mostra o valor de x1
      print(f"\nValor de x2 = {raiz2}")
    elif delta == 0: # se delta for igual a 0, a equação tem uma raiz real
      raiz1 = (-b + (delta) ** (1 / 2)) / (2 * a)  # sem a math
      print(f"\nValor de x1 = x2 = {raiz1}") # mostra o valor de x1 e x2
    else: # se delta for menor que 0, a equação não tem raízes reais
      print("não existe raiz!")

