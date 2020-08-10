def éPrimo(x):
    divisores = 0
    for divisor in range(1, x):
        if x % divisor == 0:
            divisores = divisores + 1
        if divisores > 1:
          break
    if divisores > 1:
        return False
    else:
        return True

def maior_primo(y):
    primo = y
    i = 0
    while i <= y:
        if éPrimo(i):
            primo = i
        i = i + 1
    return primo
