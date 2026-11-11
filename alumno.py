

class Alumno:
    # constructor de la clase Alumno
    def __init__ (self, id, nombre, email, edad ):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.edad = edad
    # Metodo sin retorno mostrar informacion del alumno    
    def mostrar_info(self):
        print(f"ID: {self.id}" )
        print("Nombre: ", self.nombre)
        print(f"Email: {self.email}")
        print(f"Edad: {self.edad}")
        
        
