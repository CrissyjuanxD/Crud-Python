class Empleado:
    def __init__(self,ids,nom,ced,sueldo):
        self.id=ids
        self.nombre=nom
        self.cedula = ced
        self.sueldo=sueldo
    
    def mostrar(self):
        print(f'{self.id} {self.nombre}')
    
    def valorHora(self):
        return self.sueldo/240
    
    def getDatos(self):
        return [str(self.id),self.nombre,self.cedula,str(self.sueldo)]
    
    def getDatosString(self):
        return f'{str(self.id)}|{self.nombre}|{self.cedula}|{str(self.sueldo)}'

class Proveedor:
    def __init__(self,ids,nom,ced):
        self.id=ids
        self.nombre=nom
        self.cedula = ced
            
    
    def getDatosString(self):
        return f'{str(self.id)}|{self.nombre}|{self.cedula}'
