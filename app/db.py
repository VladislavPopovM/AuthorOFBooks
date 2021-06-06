import psycopg2
import json
class DB:
    def __init__(self):
        self.conn = False
        self.cur = False
        try:
            self.conn = psycopg2.connect(
                database='database',
                user='username',
                password='secret',
                host='127.0.0.1',
                port='5405',
            )

            self.cur = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error: 
                print ("Error while creating PostgreSQL table", error)


    def set_writer(self, name):
        self.cur.execute('''INSERT INTO Writer (name) VALUES(%s);''', (name, ))
        self.conn.commit()
        self.cur.execute(f'''SELECT id FROM Writer WHERE name = '{name}';''')
        id_writer = self.cur.fetchone()
        self.conn.commit()
        return id_writer

    def set_book(self, name, author_id):
        self.cur.execute('''INSERT INTO Book (name, author_id) VALUES(%s, %s);''', (name, author_id))
        self.cur.execute(f'''SELECT Book.id, Book.name FROM Book WHERE name = '{name}';''')
        book = self.cur.fetchone()
        data_json = {
            "id": book[0],
            "name": book[1]
        }
        print(data_json)
        self.cur.execute(f'''Update Book SET data_json = '{json.dumps(data_json)}' WHERE id = {data_json["id"]}''')
        self.conn.commit()

    def get_author_with_books_non_json(self, id):
        self.cur.execute(f'''SELECT Writer.id, Writer.name, Book.id, Book.name FROM Writer, Book
                   WHERE Writer.id = {id} AND Book.author_id = Writer.id''')
        res = self.cur.fetchall()
        self.conn.commit()
        return res

    def get_author_with_books(self, id):
        self.cur.execute(f'''SELECT Writer.id, Writer.name, Book.data_json FROM Writer, Book
                   WHERE Writer.id = {id} AND Book.author_id = Writer.id''')
        res = self.cur.fetchall()
        self.conn.commit()
        return res

    def connect_close(self):
        self.cur.close()
