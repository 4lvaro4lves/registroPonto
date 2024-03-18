from tkinter import *
from tkinter import ttk
from professor import listProfessoresCompleta as professores
import registro

############################################### JANELA 01 MAIN (janela)

janela = Tk()
frm = ttk.Frame(janela, padding=10)
frm.grid()
janela.title("Controle Ponto")
janela.geometry('350x500')


############################################### FUNÇÕES

def inserirNomes(lbNomes,x):
    return (lbNomes.insert(END, x))

def btlbNomes():
    registro.baterPonto(lbNomes.get(ACTIVE),123)
    
def historico():
    janela2 = Tk()
    janela2.title(lbNomes.get(ACTIVE))
    frm2 = ttk.Frame(janela2, padding=10)
    frm2.grid()
    pontos = registro.histProf(lbNomes.get(ACTIVE))
    ttk.Label(frm2, text="Registro de Ponto").grid(row=0, column=0)
    ttk.Label(frm2, text=pontos).grid(row=1, column=0)
    ttk.Button(frm2, text="Quit", command=janela2.destroy).grid(row=0, column=1)

############################################### BOTÕES

ttk.Label(frm, text="Professores").grid(row=0, column=0)
lbNomes = Listbox(janela, height=3)
lbNomes.grid(row=1, column=0)
for i in range (1, len(professores)):
    inserirNomes(lbNomes,professores[i])
#lbNomes.get(ACTIVE)

ttk.Button(frm, text="Bater Ponto", command=btlbNomes).grid(row=2 ,column=1)
ttk.Button(frm, text="Histórico", command=historico).grid(row=2 ,column=2)
ttk.Button(frm, text="Quit", command=janela.destroy).grid(row=2, column=3)


janela.mainloop()
