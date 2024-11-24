from db_connect.conn import connection_db

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

def create_user(name: str, surname: str):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, surname) VALUES (%s, %s) RETURNING id;",
            (name, surname),
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return user_id
    except Exception as e:
        raise Exception(f"Error al crear: {e}")
    
def update_user(user_id: int, name: str, surname: str):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET name = %s, surname = %s WHERE id = %s;",
            (name, surname, user_id),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return f"Usuari {user_id} actualitzat."
    except Exception as e:
        raise Exception(f"Error al actualitzar: {e}")
    
def delete_user(user_id: int):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return f"Usuario {user_id} esborrat."
    except Exception as e:
        raise Exception(f"Error al eliminar: {e}")