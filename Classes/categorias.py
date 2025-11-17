from connection import Database

class Categoria:
    def __init__(self, id_categoria, nome_categ, imagem_categ, usuario_id_user, categoria_id_categoria=None):
        self.id_categoria = id_categoria
        self.nome_categ = nome_categ
        self.imagem_categ = imagem_categ
        self.usuario_id_user = usuario_id_user
        self.categoria_id_categoria = categoria_id_categoria

    @classmethod
    def create(cls, nome, imagem, usuario_id, categoria_id=None):
        conn = Database().get_conn()
        cursor = conn.cursor()
        if categoria_id:
            cursor.execute('''
                INSERT INTO categoria (nome_categ, imagm_categ, usuario_id_user, categoria_id_categoria)
                VALUES (%s, %s, %s, %s) RETURNING id_categoria;
            ''', (nome, imagem, usuario_id, categoria_id))
        else:
            cursor.execute('''
                INSERT INTO categoria (nome_categ, imagm_categ, usuario_id_user)
                VALUES (%s, %s, %s) RETURNING id_categoria;
            ''', (nome, imagem, usuario_id))
        new_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return cls(new_id, nome, imagem, usuario_id, categoria_id)

    @classmethod
    def get_subcategorias(cls, categoria_id):
        conn = Database().get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categoria WHERE categoria_id_categoria = %s", (categoria_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [cls(*row) for row in rows]
