casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o salario do comprador? '))
prazo = float(input('Em quantos anos vai pagar o financiamento: '))
parcela = casa / (prazo * 12)

if parcela > (sal * 0.3):
    print('Empréstimo negado, parcela excede 30% do salario')
else:
    print('Empréstimo aprovado!!')
    
print(f'Para pagar uma casa de R${casa:.2f}, em {prazo} anos')
print(f'A parcela será de {parcela:.2f}')