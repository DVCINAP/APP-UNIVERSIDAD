import sqlite3

from alumno import Alumno
from curso import Curso
from matricula import Matricula

# --------------------------------
# CONECTAR CON LA BASE DE DATOS
# --------------------------------

conexion = sqlite3.connect("inacap.db")

print("Conexion realizada correctamente")

# --------------------------------------
# CREAR CURSOR
# --------------------------------------

cursor = conexion.cursor()

print("Cursor creado correctamente")


# ========================================
#     CREAR TABLA ALUMNO
# ========================================

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS alumno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL, 
        email TEXT NOT NULL,
        edad INTEGER
    )
        
    """
)

print("Tabla: 'alumno' creada correctamente")

