from connection import Database

class Usuario:
    def __init__(self, id_user, nome_user, hash):
        self.id_user = id_user
        self.nome_user = nome_user
        self.hash = hash
    
    @classmethod
    def find_by_nome(cls, nome):
        conn = Database().get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE nome_user = %s", (nome,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return cls(*row)
        return None
