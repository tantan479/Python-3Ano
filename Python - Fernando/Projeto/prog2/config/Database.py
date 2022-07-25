import psycopg2


class Database:
    def __init__(self, config: dict) -> None:
        self.connect(config)

    def connect(self, config: dict):
        self.conn = None

        try:
            print("Conectando com o PostgreSQL...")
            self.conn = psycopg2.connect(**config)

            cur = self.conn.cursor()

            print("\nPostgreSQL database Version")
            cur.execute("SELECT version()")

            db_version = cur.fetchall()
            print(db_version)

            cur.close

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)