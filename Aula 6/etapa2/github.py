import connection

class Github(connection.Connection):
    def __init__(self):
        super().__init__()

    def insert(self, *args):
        try:
            sql = "INSERT INTO dados (login, idhub, avatar_url, repos_url, name, location, bio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)

    def get(self, id):
        try:
            sql_s = f"SELECT * FROM dados WHERE idhub = {id};"
            if not self.query(sql_s):
                return "Registro não encontrado"
            self.execute(sql_s)
            self.commit()
            return self.cur.fetchone()
        except Exception as e:
            print("Erro ao buscar", e)
