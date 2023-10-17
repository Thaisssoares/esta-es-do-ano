#Projeto estações do ano de 2023

#Apresentação
print('\n\n--Verificador de Data:')

#Entradas
dia=int(input('Digite o dia: '))
mes=int(input('Digite mês:'))

#Processamento e Saída
if mes== 12 and dia >= 22 or mes== 1 or mes==2 or mes==3 and dia<20:
        print(f'Na data {dia}/{mes}/2023 estaremos na estação Verão')
elif mes== 3 and dia >=20 or mes==4 or mes==5 or mes==6 and dia <21:
        print(f'Na data {dia}/{mes}/2023 estaremos na estação Outono')
elif mes== 6 and dia >=21 or mes==7 or mes==8 or mes==9 <23:
        print(f'Na data {dia}/{mes}/2023 estaremos na estação Inverno')
elif mes== 9 and dia >=23 or mes==10 or mes==11 or mes==12 and dia <22:
        print(f'Na data {dia}/{mes}/2023 estaremos na estação Primavera')
else:
        print(f'Informações inválidas')





