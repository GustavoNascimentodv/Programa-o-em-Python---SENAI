# váriaveis
# sinais de comparação lógico
# sinais de comparação arimético
# input / output


nome = (input('Digite o nome do aluno: '))
nota1 = float(input(' 1º trimestre nota:  '))
nota2 = float(input(' 2º trimestre nota:  '))            
nota3 = float(input(' 3º trimestre nota:  '))
nota4 = float(input(' 4º trimestre nota:  '))
              
media = (nota1+nota2+nota3+nota4)/4
              
print(' média do aluno: ', nome,' = ',media)

aprov = media >= 7
recup = media >= 5 or media <=
6
reprov = media < 5
              
              
print(f'''
Situação do Aluno {nome}
APROVADO - {aprov}
RECUPERAÇÃO - {recup}
REPROVADO - {reprov}
''')