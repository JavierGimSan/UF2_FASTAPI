import psycopg2

def insert_dat_csv_to_db(pos, data): #Le pasamos pos(la 'i' del bucle) y data(la lista de la que podemos extraer 'WORD' y 'THEME')
    conn = psycopg2.connect(
        database="postgres_24277",
        user="user_postgres1",
        password="pass_postgres1",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    sql = "INSERT INTO paraules (word, tematica) VALUES (%s, %s);"
    values = ((data["WORD"][pos], data["THEME"][pos]))

    cur.execute(sql, values)
    conn.commit()

    cur.close()
    conn.close()

    return {"Message":"Data inserted"}