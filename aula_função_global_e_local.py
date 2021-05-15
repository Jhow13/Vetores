'''
#1
def quem_sou_eu(): #criação da função
    nome = 'Megan' #isso é uma variável local
    print('Meu nome é: %s' % nome)

#2
nome = 'Megan' #isso é uma variável global
def quem_sou_eu():
    print('Meu nome é: %s' % nome)
quem_sou_eu() #chama a função 


#3
nome = 'Megan'
def quem_sou_eu():
    nome ='Fox'
    print('Meu nome é: %s' % nome)
print('Meu nome é: %s' %nome) #imprime a variável global
quem_sou_eu() #chama a função 
print('Que absurdo! Meu nome é: %s' %nome) #imprime  a variável global
'''

#4
nome = 'Megan'
def quem_sou_eu():
    global nome #Avisa que a variável em baixo vai ser global
    nome = 'fox' #Nome vira global: 'Fox'
    print('Meu nome é: %s' % nome)
print('Meu nome é: %s' % nome)
quem_sou_eu()
print('Na verdade, meu sobrenome é: %s' % nome) #Sai 'fox', pois agora ele é global
