maior = 0
menor = 0
cont = 0
while True:
    n = int(input())
    cont+=1
    if n == 0: break
    if cont ==1:
        maior=menor=n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

if menor != 0:
    print(maior)

if menor != 0:
    print(menor)
