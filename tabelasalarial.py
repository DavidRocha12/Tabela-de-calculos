print('*' * 28, 'Cálculo Salarial', '*' * 28)
print('')
name = str(input('Nome do funcionário: ')).strip().title()
wage = float(input('Qual é o salário do funcionário:R$'))
advancemoney = (wage / 100) * 40
print('O seu adiantamento salárial é R${:.2f}'.format(advancemoney))
mwage = float(input('Qual é o valor do salário minimo para cálculo do INSS: R$'))
minimum = (mwage / 100) * 7.5
minimum1 = ((2203.48 - mwage) / 100) * 9
minimum2 = ((3305.22 - 2203.48) / 100 ) * 12
transvouchers = str(input('Tem desconto de vale transporte? ')).strip().upper()
if transvouchers == 'SIM':
    calculation = (wage / 100) * 6
    print('O desconto do vale transporte é R${:.2f}.'.format(calculation))
if wage > mwage:
    sun = minimum + (((wage - mwage) / 100 ) * 9)
if wage > 2203.48:
    sun = minimum + minimum1 + (((wage - 2203.48) / 100) * 12)
if wage > 3305.22:
    sun = minimum + minimum1 + minimum2 + ((wage - 3305.22) /100) * 14
print('O valor do INSS é R${:.2f}'.format(sun))
extrahour = str(input('O Funcionário fez hora extra? digite sim ou não: ')).strip().upper()
if extrahour == 'SIM':
    extrahour1 = int(input('Quantos horas extra foram feitas? '))
    extra = int(input('A hora extra é 100% ou 50%? '))
    workedhour = wage / 220
    if extra == 100:
        hundred = workedhour * 2
        print('Valor da hora extra 100% por hora é R${:.2f}.'.format(hundred))
        print('O funcionário tem {} horas extra e somando as horas o valor é '
              'R${:.2f}.'.format(extrahour1, extrahour1 * hundred))
    if extra == 50:
        fifty = (workedhour / 2) + workedhour
        print('Valor da hora extra 50% por hora é R${:.2f}.'.format(fifty))
        print('O funcionário tem {} horas extra e somando as horas o valor é R${:.2f}.'.format(extrahour1, extrahour1 * fifty))
print('-' * 35, 'Fim', '-' * 35)

