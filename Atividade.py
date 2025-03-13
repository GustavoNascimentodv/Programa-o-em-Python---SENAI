print(f''' Seja Bem Vindo(a) a Tech Hero 
      
      Para começar, vamos realizar seu registro ''')


nome  = []
idade = []
email = []
senha = []

meu_nome, minha_idade, meu_email, minha_senha  =  input(' Digite seu nome: '), input(' Digite sua idade: '), input(' Digite seu email: '), input(' Digite sua senha: ') 

nome.append( meu_nome )
idade.append( minha_idade )
email.append( meu_email )
senha.append( minha_senha )

print(' !REGISTRADO COM SUCESSO! ')

print(f' SEJA BEM VINDO(A) {nome[0]} ')

dados = ( nome[0], idade[0], email[0], senha[0] )
print( dados )


print( '''
Escolha um produto a partir do ID
id 0 - Teclado Machenike k500
id 1 - Mouse Attack Shark X11
id 2 - Headset Redragon Hero            

''' )

menu =  [' Teclado Machenike k500 ', ' Mouse Attack Shark X11 ', ' Headset Redragon Hero ']
valores  =  [249, 130, 279.99]

escolha =  int(input(' Digite o ID do Produto: '))

meu_carrinho = []
total =  []

if escolha == 0:
    meu_carrinho.append(menu[escolha])
    total.append(valores[escolha])
    print(' -------------------------------- ')
    print(f' Produto -  {menu[escolha]} valor R$ {valores[escolha]} ')
elif escolha == 1:
    meu_carrinho.append(menu[escolha])
    total.append(valores[escolha])
    print(' -------------------------------- ')
    print(f' Produto -  {menu[escolha]} valor R$ {valores[escolha]} ')
elif escolha == 2:
    meu_carrinho.append(menu[escolha])
    total.append(valores[escolha])
    print(' -------------------------------- ')
    print(f' Produto -  {menu[escolha]} valor R$ {valores[escolha]} ')
else:
    print(' Digitação incorreta ')     



print(f'Total - R$ {valores[escolha]}')

print(f'''
      
      Pague em até 12x sem juros!
      
      ''')


forma_de_pagamento = {
1: 'PIX',
2: 'CC',
3: 'CD',
4: 'BOLETO'
}


escolha_form_pag =  int(input(' Escolha a forma de pagamento: 1 pix, 2 CC, 3 CD, 4 BOLETO '))

if escolha_form_pag == 1:
    forma =  forma_de_pagamento[1]
    print(f' Seu pagamento vai ser efetuado em {forma} ')
elif escolha_form_pag == 2:
    forma =  forma_de_pagamento[2]
    print(f' Seu pagamento vai ser efetuado em {forma} ')  
elif escolha_form_pag == 3:
    forma =  forma_de_pagamento[3]
    print(f' Seu pagamento vai ser efetuado em {forma} ')
elif escolha_form_pag == 4:
    forma =  forma_de_pagamento[1]
    print(f' Seu pagamento vai ser efetuado em {forma} ')
      
print(f''' Pagamento efetuado com sucesso
em aé 48 horas seu pedido será confirmado e enviado
''')        