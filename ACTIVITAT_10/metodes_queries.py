from conn import connection_db

def read_all(tematica):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute("SELECT word FROM paraules WHERE tematica = %s;", (tematica,))
        paraules = cursor.fetchall()
        cursor.close()
        conn.close()
        return paraules
    except Exception as e:
        raise Exception(f"Error: {e}")
    
def read_tematiques():
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT tematica FROM paraules;")
        paraules = cursor.fetchall()
        cursor.close()
        conn.close()
        return paraules
    except Exception as e:
        raise Exception(f"Error: {e}")
