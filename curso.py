class Curso:
    
    def __init__(self, id, nombre, horas):
        self.id = id
        self.nombre = nombre
        self.horas = horas
        
    def mostrar_info(self):
        print(f"ID: {self.id}")
        print(f"Nombre:{self.nombre}")
        print(f"Horas: {self.horas}")

