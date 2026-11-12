import sys


#recebe uma lista de triplas e devolve a lista de pares da silhueta, usando divisão e conquista
def skyline(edificios):

    return edificios

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

#def unirSilhuetas(s1, s2):

# devolve a silhueta de um único edifício
#def silhuetaEdificio(edificio):