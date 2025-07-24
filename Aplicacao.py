from tkinter import *
import Backend as core  # Módulo backend

class App:
    def __init__(self, window):
        self.window = window
        self.window.title("Clientes")

        # Entradas
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        Label(window, text="Nome").grid(row=0, column=0)
        self.entNome = Entry(window, textvariable=self.txtNome)
        self.entNome.grid(row=0, column=1)

        Label(window, text="Sobrenome").grid(row=0, column=2)
        self.entSobrenome = Entry(window, textvariable=self.txtSobrenome)
        self.entSobrenome.grid(row=0, column=3)

        Label(window, text="Email").grid(row=1, column=0)
        self.entEmail = Entry(window, textvariable=self.txtEmail)
        self.entEmail.grid(row=1, column=1)

        Label(window, text="CPF").grid(row=1, column=2)
        self.entCPF = Entry(window, textvariable=self.txtCPF)
        self.entCPF.grid(row=1, column=3)

        # Lista de clientes
        self.listClientes = Listbox(window, height=10, width=55)
        self.listClientes.grid(row=2, column=0, columnspan=4, rowspan=6, pady=10)

        # Scrollbar
        self.scroll = Scrollbar(window)
        self.scroll.grid(row=2, column=4, rowspan=6, sticky='ns')
        self.listClientes.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.listClientes.yview)

        self.listClientes.bind('<<ListboxSelect>>', self.get_selected_row)

        btn_width = 10

        Button(window, text="Ver Todos", command=self.view_command, width=btn_width).grid(row=2, column=5)
        Button(window, text="Buscar", command=self.search_command, width=btn_width).grid(row=3, column=5)
        Button(window, text="Inserir", command=self.insert_command, width=btn_width).grid(row=4, column=5)
        Button(window, text="Atualizar", command=self.update_command, width=btn_width).grid(row=5, column=5)
        Button(window, text="Deletar", command=self.del_command, width=btn_width).grid(row=6, column=5)
        Button(window, text="Fechar", command=self.window.destroy, width=btn_width).grid(row=7, column=5)

    def view_command(self):
        self.listClientes.delete(0, END)
        for row in core.view():
            self.listClientes.insert(END, row)

    def search_command(self):
        self.listClientes.delete(0, END)
        for row in core.search(self.txtNome.get(), self.txtSobrenome.get(), self.txtEmail.get(), self.txtCPF.get()):
            self.listClientes.insert(END, row)

    def insert_command(self):
        core.insert(self.txtNome.get(), self.txtSobrenome.get(), self.txtEmail.get(), self.txtCPF.get())
        self.view_command()

    def update_command(self):
        if self.selected:
            core.update(self.selected[0], self.txtNome.get(), self.txtSobrenome.get(), self.txtEmail.get(), self.txtCPF.get())
            self.view_command()

    def del_command(self):
        if self.selected:
            core.delete(self.selected[0])
            self.view_command()

    def get_selected_row(self, event):
        try:
            index = self.listClientes.curselection()[0]
            self.selected = self.listClientes.get(index)

            self.entNome.delete(0, END)
            self.entNome.insert(END, self.selected[1])

            self.entSobrenome.delete(0, END)
            self.entSobrenome.insert(END, self.selected[2])

            self.entEmail.delete(0, END)
            self.entEmail.insert(END, self.selected[3])

            self.entCPF.delete(0, END)
            self.entCPF.insert(END, self.selected[4])
        except IndexError:
            self.selected = None

# Execução principal
if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()
