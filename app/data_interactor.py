import mysql.connector
from contact import Contact


#write all in class sqlService
def connect_to_db():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        port=3307,
        password="",
        database='contacts_db')

    return conn


def create_contact(first_name, last_name, phone_number):
    query = f"""
    INSERT INTO contacts (first_name, last_name, phone_number)
    VALUES ("{first_name}", "{last_name}", "{phone_number}");
    """
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query)
    id_num = cursor.lastrowid
    conn.commit()
    conn.close()

    return {
"message": "Contact created successfully",
"id": id_num
}


def get_all_contacts():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "select * from contacts"
    cursor.execute(query)
    contacts = cursor.fetchall()
    contact_list = []
    for contact in contacts:
        con_object = Contact(*contact)
        contact_list.append(con_object.convert_to_dict())
    conn.commit()
    conn.close()
    return contact_list


def update_contact(id):
    pass

def delete_contact(id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = f"delete from contacts where id={id}"
    cursor.execute(query)
    conn.commit()
    conn.close()
    return True

