salario = float(input())
divida = float(input())

aumento = 5 / 100
divi = 15 /100
inicio = 0
ano = 2016
mes = 10
    
while divida < salario:
    mes+=1
    divida_atual = divida + divida * divi
    divida = divida_atual
    if mes == 12:
        ano+=1
        mes = inicio
    if mes == 3:
            novo_salario  = salario * aumento
            salario += novo_salario
    if divida > salario: break
       

print(f'{mes}/{ano}')

    
    

