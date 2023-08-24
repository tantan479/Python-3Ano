from tkinter import *


main = Tk()
main.title("Meu formulário")
main.geometry("400x300")

row = Frame(main)
row.pack(side=TOP, fill=X, padx=5, pady=5)

lbl = Label(row, text="Nome:", anchor='w')
lbl.pack(side=LEFT)

txt = Entry(row)
txt.pack(side=LEFT, expand=YES, fill=X, padx=5)


def printarNome():
    print(txt.get())


btn = Button(main, text="Exibir", command=printarNome)
btn.pack(side=LEFT, padx=5, pady=5)


main.mainloop()
