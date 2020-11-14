from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as st


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

        self.label1 = ttk.Label(self.cont1, text="Expresion Regular")
        self.re = StringVar()
        self.txt1 = ttk.Entry(self.cont1, textvariable=self.re, width=75)
        self.label1.grid(row=0, column=0, sticky=(N, W, E, S), padx=5, pady=5)
        self.txt1.grid(row=1, column=0, sticky=(N, W, E, S), padx=5, pady=5)
        self.bt1 = ttk.Button(self.cont1, text="Buscar", command=self.uno)
        self.bt1.grid(row=1, column=1, sticky=(N, W, E, S), padx=5, pady=5)

        self.label2 = ttk.Label(self.cont2, text="Texto")
        self.texto = StringVar()
        self.txt2 = st.ScrolledText(self.cont2, width=70, height=10)
        self.label2.grid(row=0, column=0, sticky=(N, W, E, S), padx=5, pady=5)
        self.txt2.grid(row=1, column=0, sticky=(N, W, E, S), padx=5, pady=5)

        self.lista1 = ttk.Treeview(self.cont3)
        self.lista1.grid(row=0, column=0, sticky=(W), padx=5, pady=5)

    def uno(self):
        pass


if __name__ == "__main__":
    root = Tk()
    App = Aplicacion(root)
    App.mainloop()
