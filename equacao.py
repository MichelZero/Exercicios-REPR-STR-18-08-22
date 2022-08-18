##
# Autores:
# Michel Silva

# data: 17/08/2022

# vamos cona classe equacao que vai receber um polinomio e calcular a raiz dele

################ 1 ######################
class Equacao:
  def __init__(self, *indices): # Construtor da classe Equacao que recebe um polinomio como parâmetro
    # entre com os indices da equação
    self.indices = list(indices) # converte o parâmetro em uma lista para poder manipular os elementos

  def __repr__(self): # representação do objeto Equacao em forma de string para ser usado em print e input
    # retonar a representação string da equação
    return 'equação(repr)=' + str(tuple(self.indices)) # retorna a representação string da equação com os termos do polinomio

################ 2 ######################

  def __str__(self): # representação do objeto Equacao em forma de string para ser usado em print e input

    grau = len(self.indices) - 1  # calcula o grau do polinomio com base no tamanho da lista de indices (indices)
    # len retorna o número de elementos do objeto, -1 para saber o grau
    simbolo = ""  # pode ser x ou y, mas iniciamos com vazio

    def expoente(grau): # função para calcular o expoente de um termo do polinomio de acordo com o grau do polinomio
        if grau == 0: # se o grau for 0, o expoente é vazio
            simbolo = "" # simbolo vazio
        elif grau == 1: # se o grau for 1, o expoente é 1
            simbolo = "x" # simbolo x
        else: # se o grau for maior que 1, o expoente é x^grau
            simbolo = "x^"+str(grau)
        return simbolo # retorna o simbolo x ou x^grau