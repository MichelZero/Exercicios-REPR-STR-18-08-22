#
# autores
# Michel Silva

from equacao import Equacao as E
# p(x) = x^4 - 4x^2 + 3x +1
def p(x):
  return x**4 - 4*x**2 + 3*x + 1
# for x in [1, 0 , -4, 2, 3, 5]:
#   print(f"{x} -> {p(x)}")
e1 = E(1, 0, -4, 3, 1)
print(e1)
print(e1.indices)
print("repr")
variavel = repr(e1)
print(variavel)
