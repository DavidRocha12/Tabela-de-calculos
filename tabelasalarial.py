#Meu primeiro projeto, estou aprendendo e procuro melhorar este programa e finalizar para
# adiquirir esperiência.
#e aprendendo com os erros.
#Projeto para fazer calculo trabalhista que vai servir para usuário empregador ou funcionário.
print('Calculo Salárial')
print('')
escolha = str(input('Você é empregador ou funcionário? ')).strip().title()#escolha de de empregador ou funcionário
if escolha == 'Empregador':#condição aninhada com if e elif para a escolha de funcionário ou empregador.
    funcionario = str(input('Qual é o nome do funcionário? ')).strip().title()#nome do funcionário
elif escolha == 'Funcionário':#condição aninhada
    usuario = str(input('Qual é seu nome? ')).strip().title()#nome do usuário
#coleta de informações abaixo do funcionáiro oou usuário, para depois fazer os calculos.
salario = float(input('Qual valor do sálario do funcionário? R$'))
horastrabalhada = int(input('Qual é a carga horária do funcionário? '))
print('Hora extra responder Sim ou Não.')
horaextra = str(input('Funcionário fez Hora extra?')).strip().title()
if horaextra == 'Sim':#Condição simples para perguntar se usuário ou funcionário fez ou não Hora extra
    horasex = float(input('Quantas Horas extras foram feitas?'))
print('Adicional Noturno responder Sim ou Não.')
adicionalnot = str(input('Funcionário tem adicional noturno para receber?')).strip().title()
if adicionalnot == 'Sim':#Condição simples para saber se funcionário tem ou não adicional noturno para
    # receber
    adn = float(input('Quantas Horas de adicional noturno foi trabalhado? '))
salariominimo = float(input('Qual o salário minimo atual para cálculo do inss? R$'))#pedindo o salario
# minimo para calculo do inss, sobre a nova lei clt de calculo trabalhista.
print('=' * 60)