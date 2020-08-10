def calcula_hipotenusa(a, b):
    hipotenusa = ((a*a) + (b*b))
    return hipotenusa

def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        c2 = (c*c)       
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (c2 == calcula_hipotenusa(a, b)): 
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1   
    return soma

def entrada():
    x = int(input("Digite um número inteiro e positivo: "))
    while x < 1:
        print("Número inválido! Tente novamente.")
        print()
        x = int(input("Digite um número inteiro e positivo: "))
    print(soma_hipotenusas(x)) 

if __name__ == "__main__":
    entrada()
