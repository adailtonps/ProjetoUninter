import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('database/jogo.db')
        self.cursor = self.conexao.cursor()

        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            create table if not exists pontuacoes(
                id integer primary key autoincrement,
                jogador text not null,
                pontuacao integer not null
            )
        """)
        self.conexao.commit()

    def salvar_pontuacao(self, jogador, pontuacao):
        self.cursor.execute("""
            insert into pontuacoes(jogador, pontuacao)
            values (?, ?)
            """, (jogador, pontuacao))
        self.conexao.commit()

    def buscar_pontuacoes(self, jogador):
        self.cursor.execute("""
            select jogador, pontuacao
            from pontuacoes
            where jogador = ?
            order by id desc
            """, (jogador,)
                            )
        return self.cursor.fetchall()

    def buscar_total_pontos(self, jogador):
        self.cursor.execute("""
                            select sum(pontuacao)
                            from pontuacoes
                            where jogador = ?
                            """, (jogador,))
        resultado = self.cursor.fetchone()
        return resultado[0] or 0

    def buscar_historico(self):
        self.cursor.execute("""
                            select id, jogador, pontuacao
                            from pontuacoes
                            order by id asc
                            """)
        return self.cursor.fetchall()