from livro import Livro

class GerenciamentoLivros:
    def __init__(self, livros: [Livro]):
        self.livros = livros
        self.romance = []
        self.acao = []
        self.misterio = []

    def organizar_livros(self):  # organiza os livros por genero
        for i in self.livros:
            if i.genero.lower() == 'acao':
                if i not in self.acao:
                    self.acao.append(i)
            elif i.genero.lower() == 'romance':
                if i not in self.romance:
                    self.romance.append(i)

            elif i.genero.lower() == 'misterio':
                if i not in self.misterio:
                    self.misterio.append(i)

    def procurar_nome(self, nome_livro: str):  # realiza uma busca por nome
        nome_livro = nome_livro.lower()
        livro = 'Livro nao encontrado'
        for i in self.livros:
            if nome_livro == i.nome.lower():
                livro = i
        print(livro)

    def mostrar_genero(self, genero: str):  # lista os livros por genero
        genero = genero.lower()
        if genero == 'romance':
            for livro in self.romance:
                print(livro)
        if genero == 'acao':
            for livro in self.acao:
                print(livro)
        if genero == 'misterio':
            for livro in self.misterio:
                print(livro)

    def mostrar_colecoes(self):  # mostra uma lista com todos os livros separando-os por genero
        print('Livros Disponiveis')
        print('Livros de Acao')
        for i in self.acao:
            print(i)
            print()
        print('Livros de Romance')
        for i in self.romance:
            print(i)
            print()
        print('Livros de Misterio')
        for i in self.misterio:
            print(i)
            print()

    def limpar_colecoes(self):
        self.acao.clear()
        self.romance.clear()
        self.misterio.clear()

    def remover_livro(self, nome_livro: str):
        nome_livro = nome_livro.lower()
        resultado = 'Livro nao encontrado'
        for i in self.livros:
            if i.nome.lower() == nome_livro:
                self.livros.remove(i)
                print(f"Livro '{i.nome}' removido da biblioteca.")
                self.limpar_colecoes()
                self.organizar_livros()
                return

        print(resultado)


    def adicionar_livro(self, nome, genero, autor=None, ano_pub=None, isbn=None):
        novo_livro = Livro(nome, genero, autor, ano_pub, isbn)
        self.livros.append(novo_livro)
        print(f"Livro '{nome}' adicionado à biblioteca.")


