from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox
import re


class Aplicacion(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title("Expresiones Regulares")
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        self.mainFrame = ttk.Frame(self.master, padding="15 15 15 15")
        self.mainFrame.grid(row=0, column=0, sticky=(N, W, E, S))
        self.widgets()

    def widgets(self):
        self.cont1 = ttk.Frame(self.mainFrame, padding="10 10 10 10")
        self.cont2 = ttk.Frame(self.mainFrame, padding="10 10 10 10")
        self.cont3 = ttk.Frame(self.mainFrame, padding="10 10 10 10")
        self.cont4 = ttk.Frame(self.mainFrame, padding="10 10 10 10")
        self.cont5 = ttk.Frame(self.mainFrame, padding="10 10 10 10")
        self.cont1.grid(row=0, column=0, sticky=(N, W, E, S))
        self.cont2.grid(row=1, column=0, sticky=(N, W, E, S))
        self.cont3.grid(row=2, column=0, sticky=(N, W, E, S))
        self.cont4.grid(row=3, column=0, sticky=(N, W, E, S))
        self.cont5.grid(row=4, column=0, sticky=(N, W, E, S))

        self.label1 = ttk.Label(self.cont1, text="Expresion Regular")
        self.re = StringVar()
        self.txt1 = ttk.Entry(self.cont1, textvariable=self.re, width=80)
        self.label1.grid(row=0, column=0, sticky=(N, W, E, S), padx=5, pady=5)
        self.txt1.grid(row=1, column=0, sticky=(N, W, E, S), padx=5, pady=5)
        self.bt1 = ttk.Button(self.cont1, text="Buscar", command=self.buscar)
        self.bt1.grid(row=1, column=1, sticky=(N, W, E, S), padx=5, pady=5)

        self.label2 = ttk.Label(self.cont2, text="Texto")
        self.txt2 = st.ScrolledText(self.cont2, width=70, height=5)
        self.label2.grid(row=0, column=0, sticky=(N, W, E, S), padx=5, pady=5)
        self.txt2.grid(row=1, column=0, sticky=(N, W, E, S), padx=5, pady=5)

        self.lista1 = ttk.Treeview(self.cont3, height=3)
        self.lista1.heading('#0', text="Matches")
        self.lista1.column("#0", width=568, minwidth=270, stretch=NO)
        self.lista1.grid(row=0, column=0, sticky=(N, W, E, S), padx=0, pady=5)
        self.vsb = ttk.Scrollbar(self.cont3, orient="vertical",
                                 command=self.lista1.yview)
        self.vsb.grid(row=0, column=1, sticky=(N, W, E, S), pady=5)
        self.lista1.configure(yscrollcommand=self.vsb.set)
        self.Label3Matches = StringVar(value="Numero de matches: 0")
        self.label3 = ttk.Label(self.cont3, textvariable=self.Label3Matches)
        self.label3.grid(row=1, column=0, sticky=(N, W, E, S), padx=5, pady=5)

        self.lista2 = ttk.Treeview(self.cont4, height=3)
        self.lista2.heading('#0', text="Groups")
        self.lista2.column("#0", width=568, minwidth=270, stretch=NO)
        self.lista2.grid(row=0, column=0, sticky=(N, W, E, S), padx=0, pady=5)
        self.vsb2 = ttk.Scrollbar(self.cont4, orient="vertical",
                                  command=self.lista2.yview)
        self.vsb2.grid(row=0, column=1, sticky=(N, W, E, S), pady=5)
        self.lista2.configure(yscrollcommand=self.vsb2.set)

        self.label4 = ttk.Label(self.cont5, text='Grupo (entero ejem: 1)')
        self.label4.grid(row=0, column=0, sticky=(N, W, E, S), padx=5, pady=5)
        self.label5 = ttk.Label(self.cont5, text='Reemplazo')
        self.label5.grid(row=0, column=1, sticky=(N, W, E, S), padx=5, pady=5)
        self.grupoReplace = StringVar()
        self.txt3 = ttk.Entry(self.cont5,
                              textvariable=self.grupoReplace, width=30)
        self.txt3.grid(row=1, column=0, sticky=(N, W, E, S), padx=5, pady=5)
        self.reemplazo = StringVar()
        self.txt4 = ttk.Entry(self.cont5,
                              textvariable=self.reemplazo, width=30)
        self.txt4.grid(row=1, column=1, sticky=(N, W, E, S), padx=5, pady=5)
        self.bt2 = ttk.Button(self.cont5, text="Replace Group",
                              command=self.replaceGroup)
        self.bt2.grid(row=1, column=2, sticky=(N, W, E, S), padx=5, pady=5)
        self.txt3 = st.ScrolledText(self.cont5, width=70, height=5)
        self.txt3.grid(row=2, column=0, columnspan=4, sticky=(N, W, E, S), padx=5, pady=5)

    def buscar(self):
        self.lista1.delete(*self.lista1.get_children())
        self.lista2.delete(*self.lista2.get_children())

        texto = self.txt2.get("1.0", END)
        try:
            self.compilado = re.compile(self.re.get(), re.MULTILINE)
            last = 0
            nmatches = 0
            while last <= len(texto):
                m = self.compilado.search(texto, last)
                if m is None:
                    break
                first, last = m.span()
                if last == first:
                    last = first+1
                self.lista1.insert('', END, text=texto[first:last])
                groups = list(m.groups())
                groups.insert(0, m.group())
                for i in range(len(groups)):
                    g = "%2d: %r" % (i, groups[i])
                    self.lista2.insert('', END, text=g)
                nmatches = nmatches + 1
                self.Label3Matches.set('Total de matches: {}'.format(nmatches))
        except re.error as msg:
            messagebox.showerror("Error", msg)

    def replaceGroup(self):
        texto = self.txt2.get("1.0", END)
        nuevotexto = texto[:]
        gr = self.grupoReplace.get()  # Grupoa reemplazar
        newcd = self.reemplazo.get()  # Cadena que pondra
        self.txt3.delete(1.0, END)
        try:
            self.compilado = re.compile(self.re.get(), re.MULTILINE)
            last = 0
            while last <= len(texto):
                m = self.compilado.search(texto, last)
                if m is None:
                    break
                first, last = m.span()
                if last == first:
                    last = first+1
                groups = list(m.groups())
                groups.insert(0, m.group())
                new = re.sub(groups[int(gr)], newcd, groups[0])
                nuevotexto = nuevotexto.replace(nuevotexto[first:last], new)
                self.txt3.delete(1.0, END)
                self.txt3.insert(END, nuevotexto)
        except re.error as msg:
            messagebox.showerror("Error", msg)


if __name__ == "__main__":
    root = Tk()
    App = Aplicacion(root)
    App.mainloop()
