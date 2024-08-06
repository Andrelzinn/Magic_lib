from gerenciamentolivros import GerenciamentoLivros
from livro import Livro
class Bibliotecario:
    def __init__(self, nome, livros: [Livro]):
        self.nome = nome
        self.acervo_sistema = GerenciamentoLivros(livros)

    def adicionar_livro(self, nome, genero, autor=None, ano_pub=None, isbn=None):
        self.acervo_sistema.adicionar_livro(nome, genero, autor, ano_pub, isbn)

    def remover_livro(self, nome_livro):
        self.acervo_sistema.remover_livro(nome_livro)

    def mostrar_colecoes(self):
        self.acervo_sistema.mostrar_colecoes()

    def organizar_livros(self):
        self.acervo_sistema.organizar_livros()

    def procurar_nome(self, nome_livro):
        self.acervo_sistema.procurar_nome(nome_livro)

    def mostrar_genero(self, genero):
        self.acervo_sistema.mostrar_genero(genero)


livro1 = Livro(nome="Guia de Poções do Minecraft", genero="Misterio", autor="Steve",
               ano_pub=2024, isbn="0051")
livro2 = Livro(nome="Cinderela", genero="Romance", autor="Steve", ano_pub=2024, isbn="0051")

livro3 = Livro(nome="War", genero="Acao", autor="Steve", ano_pub=2024, isbn="0051")



bibliotecario = Bibliotecario('Andrel', [livro1, livro2, livro3])
bibliotecario.organizar_livros()
bibliotecario.mostrar_colecoes()
bibliotecario.procurar_nome('cinderela')
bibliotecario.mostrar_genero('acao')
bibliotecario.adicionar_livro('Python', 'Misterio', 'Guido Van Rossun', '1989', '19872')
bibliotecario.organizar_livros()
bibliotecario.mostrar_colecoes()
bibliotecario.remover_livro('Python')
bibliotecario.mostrar_colecoes()
