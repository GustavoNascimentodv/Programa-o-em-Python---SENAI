# 1

# Peça para o usuário digitar um número, verifique se o número 
# é positivo, negativo ou zero.

print(f''' escolha um número para continuar''')

num = int(input(' Digite um número: '))

print(f'''Agora, vamos verificar seu número
  ''')

print('=====================================')


if num  ==  0:
    print(' Seu número é zero ')  
elif num < 0: 
    print(' Seu número é negativo ')
else:
   print('Seu número é positivo ') 




# 2

# Peça para o usuário digitar a idade, verifique 
# se essa pessoa pode votar com base na idade.

idade = int(input(' Digite sua idade: '))

print(f'''Vamos verificar sua idade
      
      Aguarde...
      ''')

if idade >= 18:
    print(' Maior de idade ')
else: 
    print(' menor de idade ')    




# 3

# Declare uma variável com um número qualquer, 
# determine se o número é par ou ímpar.

num1  = int(input('Digite um número:'))

print(f'''vamos verificar se o número escolhido
      é impar ou par.
      
      Aguarde...''')

if num1 % 2 == 0:
   print(' Par ')
else:
   print(' impar ') 





# 4

# Usuário vai digitar 3 números, para criar um triângulo, 
#verifique se o triângulo é equilátero, isósceles ou escaleno


a = int(input(' Digite um numero '))
b = int(input(' Digite um numero '))
c = int(input(' Digite um numero '))

print(f'''Vamos verificar qual é este tipo de triângulo
      
      Aguarde...''')

if a == b == c:
   print(' equilátero ') 
elif a == b and  b!= c  or  a== c and b != c:
  print(' isóceles ') 
else:
  print(' escaleno ')




# 5

# Determine se um número é múltiplo de 5 e 7.

num2 = int(input('Digite um número: '))

print(f'''vamos verificar seu número
      
      Aguarde...''')

if num2 % 5 == 0 and num2 % 7 ==0: 
   print(' É multiplo ')
else: 
   print(' Não é multiplo')



# 6

# Verifique se um número é positivo e maior que 10

num3  =  int(input(' Digite um número: '))

print(f'''vamos verificar seu número
      
      Aguarde...''')

if  num3 > 0 and num3 >10:
    print(' O número é maior que 10 ')  
else: 
    print(' O número é menor que 10 ')




# 7

# Verifique se um número é divisível por 3 ou 5.
    
   
num4 =  int(input(' Digite um número: '))

print(f'''vamos verificar seu número
      
      Aguarde...''')

if num4 % 3 ==0 or num4 % 5 ==0: 
   print(' Divisivel ')
else:
   print(' Não divisivel ')