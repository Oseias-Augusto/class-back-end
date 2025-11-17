import psycopg2

class Database:
    def __init__(self):
        self.dbname = "banco_barbalao"
        self.user = "root"
        self.password = "DdDLJr8BYykOf9hJL9TWXP2eDsF2A8S6"
        self.host = "dpg-d42kp3i4d50c739qr750-a.oregon-postgres.render.com"
        self.port = "5432"

    def get_conn(self):
        return psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
