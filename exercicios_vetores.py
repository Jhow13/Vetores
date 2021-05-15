'''
#A
def copia_vetor(a, b, tam):
    i = 0
    while i < tam:
        b[i] = a[i]
        i += 1

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
copia_vetor(a, b, 4)
print(b)

#B
def soma_vetores(a, b, c, tam):
    for i in range(tam):
        c[i] = a[i] + b[i]
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
c = [0] * 4
soma_vetores(a, b, c, 4)
print(c)

#C
def zera_ind_par(a, tam):
    for i in range(tam):
        if i % 2 == 0:
            a[i] = 0
a = [5, 2, 9, 3]
zera_ind_par(a, 4)
print(a)

#D
def junta_vetores(a, b, c, tam1, tam2):
    j = 0
    for i in range(tam1):
        c[j] = a[i]
        j += 1
    for i in range(tam2):
        c[j] = b[i]
        j += 1
    return j

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
c = [0] * (4 + 4)
junta_vetores(a, b, c, 4, 4)
print(c)
'''
#E
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

a = [10, 22, 30, 44]
b = [11, 20, 31, 40]
c = [0] * (4 + 4)
intercala_vetores(a, b, c, 4, 4)
print(c)



