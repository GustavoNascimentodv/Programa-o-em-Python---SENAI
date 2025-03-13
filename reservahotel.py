escolhas_quartos  = []
clientes =  []
meus_valores = []
quartos = ['SIMPLES','DUPLO','LUXO']
lista_precos =  [600,870,1300.00]

print('''Seja bem vindo(a),
Cadastre-se e
Escolha o quarto pelo ID,
SIMPLES(0),DUPLO(1),LUXO(2)''')

nome1 = input('Digite seu nome :')
idade1 = int(input('idade: '))
quarto1 = int(input('Escolha o ID quarto: '))
dias1 = int(input('quantidade de dias: '))

nome2 = input('Digite seu nome: ')
idade2 = int(input('idade :'))
quarto2 = int(input('Escolha o ID quarto: '))
dias2 = int(input('quantidade de dias: '))

nome3 = input('Digite seu nome: ')
idade3 = int(input('idade :'))
quarto3 = int(input('Escolha o ID quarto: '))
dias3 = int(input('quantidade de dias: '))


clientes.extend([nome1,nome2, nome3])
escolhas_quartos+=(quartos[quarto1],quartos[quarto2], quartos[quarto3])
meus_valores+=(lista_precos [quarto1],lista_precos [quarto2],lista_precos[quarto3])

cal1 = (lista_precos[quarto1] * dias1) 
cal2 = (lista_precos[quarto2] * dias2) 
cal3 = (lista_precos[quarto3] * dias3) 

print('****' * 21)

print(f'''

Quartos escolhidos -  {escolhas_quartos}

Valores escolhidos  -  {meus_valores}

**********************************

Cliente 1 -  {nome1}

QUARTO - {quarto1}
DIAS - {dias1}
VALOR R$ {cal1}

**********************************

Cliente  2  -  {nome2 }

QUARTO - {quarto2}
DIAS - {dias2}
VALOR R$ {cal2}

**********************************

Cliente 3  -  {nome3}

QUARTO - {quarto3}
DIAS - {dias3}
VALOR R$ {cal3}

''')