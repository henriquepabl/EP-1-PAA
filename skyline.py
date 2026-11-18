import sys
def qual_maior(s1,s2):
    x = 0
    y = 0
    if s1[1] > s2[1]:
        x = 1
    if s1[0] > s2[0]:
        y = 1
    if x == 1 and y == 0:
        return s1[0],s1[0]
    elif x == 1 and y == 1:
        return s1[0],s2[0]
    elif x == 0 and y == 0:
        return s2[0],s1[0]
    else: return s2[0],s2[0]

def unirSilhuetas(s1, s2):
    final = []
    sorted(s1[0])
    for i,j in s1,s2:
        if i[0] != j[0]:
            final.append([i[0],i[1]])
            final.append(j[0],j[0])
        elif final.append([i[0],j[1]])
        elif i[1] > j[1]:
                final.append([i[0],i[1]])
    
    
    
    


def silhuetaEdificio(edificio):
    return [(edificio[0],edificio[1]), (edificio[2],0)]

#recebe uma lista de triplas e devolve a lista de pares da silhueta, usando divisão e conquista
list = []
def skyline(edificios):
    if len(edificios) == 1:
        x,y = silhuetaEdificio(edificios) 
        return x,y
    s_ed1 = skyline(edificios[0:edificios//2])
    s_ed2 = skyline(edificios[edificios//2+1:])
    list.append(unirSilhuetas(s_ed1,s_ed2))

def readfile():
    if len(sys.argv) == 4:
        path_image = sys.argv[3]
    #captura caminho 
    path_input = sys.argv[1]
    #path_output = sys.argv[2]
    linha = []

    with open(path_input,"r", encoding="utf-8") as file:
        for i,linhas in enumerate(file):
            linha.append(linhas.rstrip('\n'))
    return linha

arquivo = readfile()
quant_edificios = int(arquivo[0])

temp = []
for i in range(quant_edificios):    
    linha = arquivo[i].split()
    for i in linha:
        i = int(i)
    temp.append(linha)

    
edificios = tuple(temp[1:])
silhueta_pair = skyline(edificios)

print(silhueta_pair)




# recebe duas silhuetas e devolve sua união


# devolve a silhueta de um único edifício


