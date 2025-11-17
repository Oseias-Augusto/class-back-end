from connection import Database

class Banner:
    def __init__(self, id_banner, titulo_banner, sub_titulo_banner, imagem_banner, usuario_id_user, categoria_id_categoria=None):
        self.id_banner = id_banner
        self.titulo_banner = titulo_banner
        self.sub_titulo_banner = sub_titulo_banner
        self.imagem_banner = imagem_banner
        self.usuario_id_user = usuario_id_user
        self.categoria_id_categoria = categoria_id_categoria

    @classmethod
    def create(cls, titulo, sub_titulo, imagem, usuario_id, categoria_id=None):
        conn = Database().get_conn()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO banners (titulo_banner, sub_titulo_banner, imagem_banner, usuario_id_user, categoria_id_categoria)
            VALUES (%s, %s, %s, %s, %s) RETURNING id_banner;
        ''', (titulo, sub_titulo, imagem, usuario_id, categoria_id))
        new_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return cls(new_id, titulo, sub_titulo, imagem, usuario_id, categoria_id)
