# Interface se refiere a un conjunto de métodos que una clase debe implementar. Las interfaces proporcionan una forma de definir un contrato que las clases deben seguir para garantizar que cumplan con ciertas funcionalidades o comportamientos.
class OperacionesMatematicas:
    # tomas dos numeros y los sumas
    def suma(self, a, b):
        pass

    def resta(self, a, b):
        pass

    def multiplicacion(self, a, b):
        pass

    def division(self, a, b):
        pass

class Implementacion(OperacionesMatematicas):
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: No se puede dividir entre cero"

objeto = Implementacion()
print(objeto.suma(5, 3))
print(objeto.resta(5, 3))
print(objeto.multiplicacion(5, 3))
print(objeto.division(5, 3))
