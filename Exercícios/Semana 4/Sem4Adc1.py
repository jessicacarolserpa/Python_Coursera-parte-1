número = int(input("Digite um número inteiro:"))
divisores = 0
for divisor in range(1, número):
    if número % divisor == 0:
        divisores = divisores + 1
        if divisores > 1:
          break
if divisores > 1:
  print("não primo")
else:
  print("primo")
