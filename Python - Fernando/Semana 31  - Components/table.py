from tkinter import *
from tkinter import ttk


main = Tk()
main.title("Meu programa")
main.geometry("850x700")
main.config(background="cyan")



# Caixinha 1

wrapper = LabelFrame(main, text="Pesquisa")
wrapper.pack(fill="both", expand="yes", padx=20, pady=10) # Espaçamento = padding

lbl = Label(wrapper, text="Pesquisar")
lbl.pack(side=LEFT, padx=10)

q = StringVar()
ent = Entry(wrapper, textvariable=q)
ent.pack(side=LEFT, padx=6)

btn = Button(wrapper, text="Pesquisar")
btn.pack(side=LEFT, padx=6)


# Caixinha 2

wrapper1 = LabelFrame(main, text="Tabela")
wrapper.configure(background="red")
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10) # Espaçamento = padding

table = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4), show="headings", height=6)

table.heading(1, text="ID")
table.heading(2, text="Nome")
table.heading(3, text="Último nome")
table.heading(4, text="Idade")
table.insert('', 'end', values=[1, "João", "Silva", 20])
table.pack()


main.mainloop()
