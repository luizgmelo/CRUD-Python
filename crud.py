from connect import connect

cursor = connect.cursor()


def create():
    nome = str(input("Nome: "))
    cursor.execute(f"INSERT INTO person (id, nome) VALUES (DEFAULT, '{nome}');")
    connect.commit()


def read():
    cursor.execute("SELECT * FROM person;")
    records = cursor.fetchall()
    print(records)


def update():
    uniqueId = int(input("ID: "))
    nome = str(input("Novo nome: "))
    cursor.execute(f"UPDATE person SET nome='{nome}' WHERE id = {uniqueId};")
    connect.commit()


def delete(): 
    uniqueId = int(input("ID: "))
    cursor.execute(f"DELETE FROM person WHERE id={uniqueId};")
    connect.commit()


