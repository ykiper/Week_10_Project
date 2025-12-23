import mysql.connector
from contact import Contact

def connect_to_db(query):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        port=3307,
        password="",
        database='contacts_db')

    cursor = conn.cursor(buffered=True)

    cursor.execute(query)

    conn.commit()
    conn.close()
    return cursor.fetchall()


def create_contact(first_name, last_name, phone_number):
    query = f"""
    INSERT INTO contacts (first_name, last_name, phone_number)
    VALUES ("{first_name}", "{last_name}", "{phone_number}");
    """

    connect_to_db(query)

    query = "select max(id) from contacts"
    id_num = connect_to_db(query)[0][0]

    return id_num


def get_all_contacts():
    query = "select * from contacts"
    contacts = connect_to_db(query)
    contact_list = []
    for contact in contacts:
        con_object = Contact(*contact)
        contact_list.append(con_object.convert_to_dict())
    return contact_list

print(get_all_contacts())

def update_contact():
    pass

def delete_contact(id):
    query = f"delete from contacts where id={id}"
    connect_to_db(query)
    return True
