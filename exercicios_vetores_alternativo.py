
#A
def preenche_vetor(nome, v, tam):
    for i in range(tam):
        v[i] = int(input('%s[%d] = ' % (nome, i)))
def exibe_vetor(nome, v, tam):
    print('%s: ' % nome, end='')
    for i in range(tam):
        print(v[i], end=' ')
    print()
def copia_vetor1(a, b, tam):
    i = 0    while i < tam:
        b[i] = a[i]
        i += 1def copia_vetor2(a, b, tam):
    for i in range(tam):
        b[i] = a[i]
tam = int(input('Quantos itens? '))
a = [0] * tampreenche_vetor('a', a, tam)
b = [0] * tamcopia_vetor2(a, b, tam)
exibe_vetor('a', a, tam)
exibe_vetor('b', b, tam)

#B
def preenche_vetor(nome, v, tam):
    for i in range(tam):
        v[i] = int(input('%s[%d] = ' % (nome, i)))
def exibe_vetor(nome, v, tam):
    print('%s: ' % nome, end='')
    for i in range(tam):
        print(v[i], end=' ')
    print()
def zera_ind_par(a, tam):
    for i in range(tam):
        if i % 2 == 0:
            a[i] = 0tam = int(input('Quantos itens? '))
a = [0] * tampreenche_vetor('a', a, tam)
exibe_vetor('a', a, tam)
zera_ind_par(a, tam)
exibe_vetor('a', a, tam)

#C
def preenche_vetor(nome, v, tam):
    for i in range(tam):
        v[i] = input('%s[%d] = ' % (nome, i))
def exibe_vetor(nome, v, tam):
    print('%s: ' % nome, end='')
    for i in range(tam):
        print(v[i], end=' ')
    print()
def junta_vetores(a, b, c, tam1, tam2):
    j = 0
    for i in range(tam1):
        c[j] = a[i]
        j += 1
    for i in range(tam2):
        c[j] = b[i]
        j += 1
    return j
tam1 = int(input('Quantos itens para o vetor a? '))
a = [''] * tam1
tam2 = int(input('Quantos itens para o vetor b? '))
b = [''] * tam2
c = [''] * (tam1 + tam2)
preenche_vetor('a', a, tam1)
preenche_vetor('b', b, tam2)
exibe_vetor('a', a, tam1)
exibe_vetor('b', b, tam2)
tam3 = junta_vetores(a, b, c, tam1, tam2)
exibe_vetor('c', c, tam3)

#D
def preenche_vetor(nome, v, tam):
    for i in range(tam):
        v[i] = input('%s[%d] = ' % (nome, i))
def exibe_vetor(nome, v, tam):
    print('%s: ' % nome, end='')
    for i in range(tam):
        print(v[i], end=' ')
    print()
def intercala_vetores(a, b, c, tam1, tam2):
    i = 0
    j = 0
    k = 0
    while i < tam1 and j < tam2:
        if a[i] < b[j]:
        c[k] = a[i]
        i += 1
        elif a[i] > b[j]:
            c[k] = b[j]
            j += 1
        else:
            c[k] = a[i]
            i += 1
            j += 1
            k += 1
    while i < tam1:
        c[k] = a[i]
        i += 1
        k += 1
    while j < tam2:
        c[k] = b[j]
        j += 1
        k += 1
    return k
