from connect import connect

cursor = connect.cursor()


def create():
    nome = str(input("Nome: "))
    cursor.execute(f"INSERT INTO person (id, nome) VALUES (DEFAULT, '{nome}');")
    connect.commit()
    read()


def read():
    cursor.execute("SELECT * FROM person;")
    records = cursor.fetchall()
    print(records)


create()