#Projeto estações do ano de 2023

#Apresentação
print('\n\n--Verificador de Data:')

#Entradas
mes=int(input('Digite mês:'))

#Processamento e Saída
if mes== 12 or mes== 1 or mes==2:
        print(f'Verão')
if mes== 3 or mes==4 or mes==5:
        print(f'Outuno')
if mes== 6 or mes==7 or mes==8:
        print(f'Inverno')
if mes== 9 or mes==10 or mes==11:
        print(f'Primavera')
else:
        print(f'nao tem estacao')



