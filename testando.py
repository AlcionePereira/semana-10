d = float(input().strip())
t = float(input().strip())
taxa = t / 100
dobro = d * 2
q = 0

while  d < dobro:
    novo_valor = d * taxa
    d+= novo_valor
    q = q +1
print(f'{q}')
