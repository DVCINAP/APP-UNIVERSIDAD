class Matricula:
    
    def __init__(self, id, alumno_id, curso_id, fecha):
        self.id = id
        self.alumno_id = alumno_id
        self.curso_id = curso_id
        self.fecha = fecha
        
    def mostrar_info(self):
        print(f"ID Matricula: {self.id}")
        print(f"Alumno ID: {self.alumno_id}")
        print(f"Curso ID: {self.curso_id}")
        print(f"Fecha: {self.fecha}")