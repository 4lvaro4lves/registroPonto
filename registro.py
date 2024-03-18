import datetime
import re

def baterPonto(nomeProfessor, senha):
    ponto = open("registros.csv", "a")
    hora = datetime.datetime.now()
    hora = str(hora.day)+'-'+str(hora.month)+'-'+str(hora.year)+';'+str(hora.hour)+':'+str(hora.minute)+':'+str(hora.second)
    registro = nomeProfessor+';'+hora+"\n"
    ponto.write(registro)
    ponto.close()

def criarLista():
    a = open("registros.csv", "r").read()
    b = list(a)
    aux = ''
    aux2 = []
    for i in b:
        aux = aux + i
        if (i == '\n'):
            aux2.append(aux)
            aux = ''
    return (aux2)

def histProf(nomeP):
    listaHist = criarLista()
    listHisto = []
    for i in listaHist:
        if (nomeP in i):
            i = re.sub(nomeP, '', i)
            #i = re.sub('\n', '', i)
            listHisto.append(i)
    return (listHisto)

#x=histProf('Alvaro Alves')
