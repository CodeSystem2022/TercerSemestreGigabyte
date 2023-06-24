import psycopg2

class ConexionDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="proyecto_Python",
            user="postgres",
            password="admin"
        )
        self.cursor = self.conn.cursor()

        self.crear_tabla()

    def crear_tabla(self):
        # Creamos la tabla 'deseos' si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS deseos
                              (id SERIAL PRIMARY KEY,
                               producto TEXT,
                               cantidad INTEGER,
                               precio REAL)''')

        self.conn.commit()

    def agregar_deseo(self, producto, cantidad, precio):
        # Insertamos los datos en la tabla 'deseos'
        self.cursor.execute("INSERT INTO deseos (producto, cantidad, precio) VALUES (%s, %s, %s)",
                            (producto, cantidad, precio))

        self.conn.commit()

    def eliminar_deseo(self, deseo_id):
        # Eliminamos el registro con el ID proporcionado de la tabla 'deseos'
        self.cursor.execute("DELETE FROM deseos WHERE id = %s", (deseo_id,))

        self.conn.commit()

    def eliminar_todo(self):
        # Eliminamos todos los registros de la tabla 'deseos'
        self.cursor.execute("DELETE FROM deseos")

        self.conn.commit()

    def obtener_deseos(self):
        # Obtenemos todos los registros de la tabla 'deseos'
        self.cursor.execute("SELECT * FROM deseos")
        deseos = self.cursor.fetchall()

        return deseos

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()
