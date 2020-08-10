número = int(input("Digite um número inteiro: "))

adjacente = "não"

dig_a = número % 10

while (número > 0):

 número //= 10

 dig_b = número % 10

 if (dig_a == dig_b):

  adjacente = "sim"

 dig_a = dig_b

print("%s\n" % adjacente)
