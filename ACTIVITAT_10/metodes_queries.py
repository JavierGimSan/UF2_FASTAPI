from conn import connection_db
def read_tematiques():
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT tematica FROM paraules;")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    except Exception as e:
        raise Exception(f"Error: {e}")
