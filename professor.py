import re

listProfessores = [-1]
arquivo = open('professores.txt', 'r')

def listP(listProfessores,P):
    listProfessores.append(P)
    return (listProfessores)

while(listProfessores[-1] != ''):
    listProfessores[0] = listProfessores[0]+1
    linha = arquivo.readline()
    linha = re.sub('[\n]', '', linha) #retirando o \n no final da linha

    listP(listProfessores,linha)

listProfessores.remove(listProfessores[-1])


listProfessoresCompleta = listProfessores
