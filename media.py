# 02. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo 
# número 0 (zero). Ao final, o programa deve mostrar a média
# aritmética de todos os números lidos (excluindo o zero).

# Dica: use repetição com teste no final
q = 0
soma = q
media = 0
while True:
    n = int(input().strip())
    if n != 0:
        soma += n
        q += 1
        media = soma / q
    if n == 0:break

if media != 0:
    print(f'{media:.2f}')
