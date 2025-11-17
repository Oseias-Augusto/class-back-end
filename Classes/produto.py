from connection import Database

class Produto:
    def __init__(self, id_prod, nome_prod, preco_prod, descricao_prod, imagem_prod, categoria_id_categoria, usuario_id_user):
        self.id_prod = id_prod
        self.nome_prod = nome_prod
        self.preco_prod = preco_prod
        self.descricao_prod = descricao_prod
        self.imagem_prod = imagem_prod
        self.categoria_id_categoria = categoria_id_categoria
        self.usuario_id_user = usuario_id_user

    @classmethod
    def create(cls, nome, preco, descricao, imagem, categoria_id, usuario_id):
        conn = Database().get_conn()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produto (nome_prod, preco_prod, descricao_prod, imagem_prod, categoria_id_categoria, usuario_id_user)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_prod;
        ''', (nome, preco, descricao, imagem, categoria_id, usuario_id))
        new_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return cls(new_id, nome, preco, descricao, imagem, categoria_id, usuario_id)

    @classmethod
    def list_all(cls):
        conn = Database().get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produto")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [cls(*row) for row in rows]
