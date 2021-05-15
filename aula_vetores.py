
#1
#Índice   0     1    2    3    4    5    6    7
vetor1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(vetor1[2]) #Imprime o valor do índice 2: C

#2
#notas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
notas = [0.0] * 8 #guarda 8 lugares para notas 
for i in range(8):
    nota
    s[i] = float(input('%d nota: ' % (i+1)))
'''
#O mesmo exemplo
#notas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
notas = [0.0] * 8 #guarda 8 lugares para notas 
for i in range(1, 8, 1):
    notas[i] = float(input('%d nota: ' % i))
'''
#3
def zera_vetor(a, n):
    for i in range(n):
        a[i] = 0 #Altera o valor da função "7" para "0" até o fim da lista
while True:
    n = int(input("Tamanho do vetor: "))
    if 0 < n < 21: break #O programa se incia somente entre 1 e 20
a = [7] * n #Adiciona o número de indice com o "7"
for i in range(n): 
    print("%d" % a[i], end="") #Exibe na tela o número do indice: "7"
print("\n \nAgora o vetor será zerado") #Exibe somente quando a lista termina
zera_vetor(a, n)#Chama a função
for i in range(n): #Percore a lista da função assim que ela acaba 
    print("%d" % a[i], end="") #Exibe o índice da lista: "0"    

#4
#Crie um programa que receba como entrada notas de alunos...
# E exiba apenas as notas que forem maiores do que a média...
# O usuário vai informar as notas

def preenche(v, n):
    for i in range(n): #O número informado de notas até o final do laço
        v[i] = float(input('nota: ')) #Inclusão de nota

        
def soma(v, n):
    s = 0.0 #contador, cada nota no índice preenche vai ser somado ao 's'
    for i in range(n): #Até o fim do laço 
        s += v[i]
    return s #Retorna a soma dos indices
    
qtd_notas = int(input('Quantas notas? '))
notas = [0.0] * qtd_notas #O número de indices que notas irá preencher
preenche(notas, qtd_notas) #preenchimento de nota em cada indice: 'v'
media = soma(notas, qtd_notas) / qtd_notas #soma das notas dividida pela quantidade
print('Média = %.2f' % media) 
for i in range(qtd_notas):
    if notas[i] > media: #Exibe quais as notas foram maiores que a média
        print('notas[%d] = %.2f' % (i, notas[i]))


