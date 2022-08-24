##
# Autores:
# Michel Silva

# data: 17/08/2022

############### 1 ######################
# p(x) = x^4 - 4x^2 + 3x + 1
# p(x) = x^5 - 4x^2 + 3x + 1
'''
x = float(input("Digite o valor de x: "))
px = x ** 4 - 4 * x **2 + 3 * x + 1
print(px)
'''

# p(x) = x^4 - 4x^2 + 3x + 1
# [-1, 0, 2, 3.4]

# def p(pedro):
#   x = pedro
#   return x ** 4 - 4 * x ** 2 + 3 * x + 1

def p(pedro):
  return pedro ** 4 - 4 * pedro ** 2 + 3 * pedro + 1

lista = [-1, 0, 5, 3.4]

for maria in lista:
  print(f"valor[{maria}] = {p(maria)}")

################ 2 ######################
