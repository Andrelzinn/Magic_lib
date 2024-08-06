import tkinter as tk
from tkinter import simpledialog, messagebox, Scrollbar, Text
from gerencimentolivros import GerenciamentoLivros, Livro



class InterfaceGrafica:
    def __init__(self, root):
        self.livraria = GerenciamentoLivros(nome="Magic Books")
        self.root = root
        self.root.title("Magic Books - Livraria")
        self.botoes_interativos()

    def botoes_interativos(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.text_area = Text(self.main_frame, wrap=tk.WORD, font='Garamond')
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = Scrollbar(self.main_frame, command=self.text_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.menu.add_command(label="Listar Livros", command=self.listar_livros)
        self.menu.add_command(label="Adicionar Livro", command=self.adicionar_livro)
        self.menu.add_command(label="Buscar Livro", command=self.buscar_livro)
        self.menu.add_command(label="Criar Catálogo por Gênero", command=self.criar_catalogo_por_genero)
        self.menu.add_command(label="Reservar Livro", command=self.reservar_livro)
        self.menu.add_command(label="Ver Livros Reservados", command= self.ver_livros_reservados)
        self.menu.add_command(label="Sair", command=self.root.quit)

        self.text_area.insert(tk.END, "Bem-vindo à Livraria Magic Books!\nOnde a magia dos livros ganha vida.\n")

    def listar_livros(self):
        self.text_area.delete(1.0, tk.END)
        livros = self.livraria.listar_livros()
        self.text_area.insert(tk.END, f"--- Lista de Livros ---\n\n{livros}\n")

    def adicionar_livro(self):
        nome = simpledialog.askstring("Adicionar Livro", "Digite o nome do livro:")
        genero = simpledialog.askstring("Adicionar Livro", "Digite o gênero do livro:")
        autor = simpledialog.askstring("Adicionar Livro", "Digite o autor do livro (opcional):") or None
        ano_publicacao = simpledialog.askstring("Adicionar Livro", "Digite o ano de publicação (opcional):") or None
        isbn = simpledialog.askstring("Adicionar Livro", "Digite o ISBN do livro (opcional):") or None

        ano_publicacao = int(ano_publicacao) if ano_publicacao and ano_publicacao.isdigit() else None
        livro = Livro(nome=nome, genero=genero, autor=autor, ano_publicacao=ano_publicacao, isbn=isbn)
        resultado = self.livraria.adicionar_livro(livro)
        messagebox.showinfo("Resultado", resultado)
        self.listar_livros()


    def buscar_livro(self):
        nome = simpledialog.askstring("Buscar Livro", "Digite o nome (ou parte do nome) do livro:")
        resultado = self.livraria.buscar_livro(nome)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"--- Resultado da Busca por '{nome}' ---\n\n{resultado}\n")

    def criar_catalogo_por_genero(self):
        genero = simpledialog.askstring("Criar Catálogo", "Digite o gênero para criar o catálogo:")
        resultado = self.livraria.criar_catalogo_por_genero(genero)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"--- Catálogo de Livros do Gênero '{genero}' ---\n\n{resultado}\n")

    def reservar_livro(self):
        nome = simpledialog.askstring("Buscar Livro", "Digite o nome (ou parte do nome) do livro:")
        resultado = self.livraria.buscar_livro(nome)
        self.livraria.reservar_livro(resultado)
        self.text_area.delete(1.0, tk.END)
        self.ver_livros_reservados()

    def ver_livros_reservados(self):
        resultado = self.livraria.ver_livros_reservados()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"--- Livros Reservados ---\n\n{resultado}\n")


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()

