class Livro:
    def __init__(self, nome, genero, autor=None, ano_pub=None, isbn=None):
        """
        Inicializa uma nova instância da classe Livro.

        :param nome: Nome do livro.
        :param genero: Gênero ou tópico do livro.
        :param autor: Autor do livro (opcional).
        :param ano_pub: Ano de publicação do livro (opcional).
        :param isbn: Número ISBN do livro (opcional).
        """
        self.nome = nome
        self.genero = genero
        self.autor = autor
        self.ano_publicacao = ano_pub
        self.isbn = isbn

    def __str__(self):
        """
        Retorna uma representação em string dos detalhes do livro.
        """
        return (f"Livro: {self.nome}, Gênero: {self.genero}, "
                f"Autor: {self.autor}, Ano: {self.ano_publicacao}, ISBN: {self.isbn}")

    def resumo(self):
        """
        Retorna um resumo básico do livro.
        """
        return f"'{self.nome}' é um livro do gênero {self.genero}."


# Exemplo de uso:

livro1 = Livro(nome="Guia de Poções do Minecraft", genero="Misterio", autor="Steve",
               ano_pub=2024, isbn="0051")
livro2 = Livro(nome="Cinderela", genero="Romance", autor="Steve", ano_pub=2024, isbn="0051")

livro3 = Livro(nome="War", genero="Acao", autor="Steve", ano_pub=2024, isbn="0051")
