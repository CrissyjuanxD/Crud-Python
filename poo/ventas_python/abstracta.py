from abc import ABC, abstractmethod
# Una clase abstracta en Python es una clase que no puede ser instanciada directamente, sino que sirve como una plantilla para otras clases. Las clases abstractas pueden contener métodos abstractos(al menos uno), que son métodos declarados pero no implementados en la clase abstracta. Las subclases de una clase abstracta deben proporcionar implementaciones concretas para todos los métodos abstractos definidos en la clase abstracta.
class Alumno(ABC):
    def __init__(self, nombre, edad, grado, escuela, promedio):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.escuela = escuela
        self.promedio = promedio

    @abstractmethod
    def notas(self):
        pass
  
    def mostrar(self):
        print(self.nombre)
# Crear una clase que herede la clase abstracta con un método de presentar datos.
class Estudiante(Alumno):
    def notas(self):
        return self.promedio

    def presentar_datos(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}, Escuela: {self.escuela}, Promedio: {self.promedio}'

# alum = Alumno('Ana', 20, 'Segundo', 'Escuela XYZ', 85)# no se puede instanciar la clase abstracta
estudiante = Estudiante('Juan', 20, 'Segundo', 'Escuela XYZ', 85)
print(estudiante.notas())
print(estudiante.presentar_datos())