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

# ========================================
#     CREAR TABLA CURSO
# ========================================

cursor.execute(
    
    """
    CREATE TABLE IF NOT EXISTS curso (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        horas INTEGER NOT NULL
    )
        
    """
)
print("Tabla: 'curso' creada correctamente")

# ========================================
#     CREAR TABLA MATRICULA                
# ========================================

cursor.execute(
    
    """
    CREATE TABLE IF NOT EXISTS matricula (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alumno_id INTEGER NOT NULL,
        curso_id INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (alumno_id) REFERENCES alumno(id),
        FOREIGN KEY (curso_id) REFERENCES curso(id)
    )
        
    """
)
print("Tabla: 'matricula' creada correctamente")


#=========================================
#     guardar cambios 
#=========================================
conexion.commit()
print("Cambios guardados correctamente")


##=========================================
#     INSTANCIAR OBJETOS
#=========================================

#ALUMNOS
alumno1 = Alumno(None, "Juan Perez", "juan.perez@email.com", 20)
alumno2 = Alumno(None, "María García", "maria.garcia@email.com", 22)

#CURSOS
curso1 = Curso(None, "Matemáticas", 40)

#MATRICULAS
matricula1 = Matricula(None, 1, 1, "2024-06-01")

#===========================================
#        INSERT A BD
#===========================================

cursor.execute(
    
    """
    INSERT INTO alumno (nombre, email, edad) VALUES (?, ?, ?)
    """,
    (alumno1.nombre,
      alumno1.email,
        alumno1.edad)
)

conexion.commit()
print("Cambios guardados correctamente del alumno")