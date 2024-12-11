from conn import connection_db

conn = connection_db()
cursor = conn.cursor()

# Consulta para listar tablas en PostgreSQL
idioma = "catala"
cursor.execute("SELECT lletra FROM abecedari WHERE idioma = %s;", (idioma,))
print(cursor.fetchall())

cursor.close()
conn.close()
