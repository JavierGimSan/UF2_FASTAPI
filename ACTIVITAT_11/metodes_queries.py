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
    
def read_lletres_idioma(idioma):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute("SELECT lletra FROM abecedari WHERE idioma = %s;", (idioma,))
        lletres = cursor.fetchall()
        cursor.close()
        conn.close()
        return lletres
    except Exception as e:
        raise Exception(f"Error: {e}")

def read_text_comencar():
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute("SELECT text_comencar from comencar_partida WHERE id = 1;")
        text_comencar = cursor.fetchone()
        cursor.close()
        conn.close()
        return text_comencar
    except Exception as e:
        raise Exception(f"Error: {e}")
    
def read_imatge_intents(intents):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute("SELECT nom_imatge from intents WHERE id_imatge = %s;",(intents,))
        nom_imatge = cursor.fetchone()
        cursor.close()
        conn.close()
        return nom_imatge
    except Exception as e:
        raise Exception(f"Error: {e}")
    
def read_nom_usuari(id_usuari):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute("SELECT nom_usuari from usuaris WHERE id_usuari = %s;",(id_usuari,))
        nom_imatge = cursor.fetchone()
        cursor.close()
        conn.close()
        return nom_imatge
    except Exception as e:
        raise Exception(f"Error: {e}")