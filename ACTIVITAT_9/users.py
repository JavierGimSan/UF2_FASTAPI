from conn import connection_db

def read_users():
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, surname FROM users;")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    except Exception as e:
        raise Exception(f"Error: {e}")
