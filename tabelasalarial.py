#Meu primeiro projeto, estou aprendendo e procuro melhorar este programa e finalizar para
# adiquirir esperiência.
#e aprendendo com os erros.
#Projeto para fazer calculo trabalhista que vai servir para usuário empregador ou funcionário.
print('Calculo Salárial')
print('')
escolha = str(input('O calculo é para a empresa ou funcionário? ')).strip().title()#escolha de de empregador ou funcionário
if escolha == 'Empresa':#condição aninhada com if e elif para a escolha de funcionário ou empregador.
   #adicionado a variante funcionario no if na condiçao aninhada
    funcionario = str(input('Qual é o nome do funcionário? ')).strip().title()#nome do funcionário
    salario = float(input('Qual valor do salário do funcionário? R$'))
elif escolha == 'Funcionário' or 'Funcionario':#condição aninhada
    usuario = str(input('Qual é seu nome? ')).strip().title()#nome do usuário
#coleta de informações abaixo do funcionáiro oou usuário, para depois fazer os calculos.
    salario = float(input('Qual é o valor do seu salário? R$'))
    #adicionado a variante salario no elif condição aninhada
horastrabalhada = int(input('Qual é a carga horária do funcionário? '))
print('(Responda Sim ou Não se funcionário fez hora extra)')#frase modificada('Hora extra sim ou não')
horaextra = str(input('Funcionário fez Hora extra? ')).strip().title()
if horaextra == 'Sim':#Condição simples para perguntar se usuário ou funcionário fez ou não Hora extra
    horasex = float(input('Quantas Horas extras foram feitas? '))
print('(Responda Sim ou Não se funcionário tem horas noturnas)')#frase alterada(adicional noturno sim ou não')
adicionalnot = str(input('Funcionário tem adicional noturno para receber? ')).strip().title()
if adicionalnot == 'Sim':#Condição simples para saber se funcionário tem ou não adicional noturno para
    # receber
    adn = float(input('Quantas Horas de adicional noturno foi trabalhado? '))
salariominimo = float(input('Qual o salário minimo atual para cálculo do inss? R$'))#pedindo o salario
# minimo para calculo do inss, sobre a nova lei clt de calculo trabalhista.
print('=' * 60)
