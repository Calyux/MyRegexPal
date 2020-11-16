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
        self.cont1.grid(row=0, column=0, sticky=(N, W, E, S))
        self.cont2.grid(row=1, column=0, sticky=(N, W, E, S))
        self.cont3.grid(row=2, column=0, sticky=(N, W, E, S))

        self.bt1 = ttk.Button(self.cont1, text="Buscar IP",
                              command=self.buscar)
        self.bt1.grid(row=1, column=1, sticky=(N, W, E, S), padx=5, pady=5)

        self.label2 = ttk.Label(self.cont2, text="Texto")
        self.txt2 = st.ScrolledText(self.cont2, width=100, height=11)
        self.label2.grid(row=0, column=0, sticky=(N, W, E, S), padx=5, pady=5)
        self.txt2.grid(row=1, column=0, sticky=(N, W, E, S), padx=5, pady=5)

        self.lista1 = ttk.Treeview(self.cont3, height=10)
        self.lista1.heading('#0', text="Matches")
        self.lista1.column("#0", width=810, minwidth=300, stretch=NO)
        self.lista1.grid(row=0, column=0, sticky=(N, W, E, S), padx=0, pady=5)
        self.vsb = ttk.Scrollbar(self.cont3, orient="vertical",
                                 command=self.lista1.yview)
        self.vsb.grid(row=0, column=1, sticky=(N, W, E, S), pady=5)
        self.lista1.configure(yscrollcommand=self.vsb.set)
        self.Label3Matches = StringVar(value="Numero de matches: 0")
        self.label3 = ttk.Label(self.cont3, textvariable=self.Label3Matches)
        self.label3.grid(row=1, column=0, sticky=(N, W, E, S), padx=5, pady=5)

        with open('Linux_2k.log') as f:
            self.read_data = f.read()

        self.txt2.insert(END, self.read_data)

    def buscar(self):
        self.lista1.delete(*self.lista1.get_children())

        texto = self.txt2.get("1.0", END)

        # Expresion regular
        patron = r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\." \
                 r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\." \
                 r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\." \
                 r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\b"
        try:
            self.compilado = re.compile(patron, re.MULTILINE)
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
                nmatches = nmatches + 1
                self.Label3Matches.set('Total de matches: {}'.format(nmatches))
        except re.error as msg:
            messagebox.showerror("Error", msg)


if __name__ == "__main__":
    root = Tk()
    App = Aplicacion(root)
    App.mainloop()
