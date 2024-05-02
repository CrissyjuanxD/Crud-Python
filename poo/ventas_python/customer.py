class Client:
    def __init__(self, first_name="Consumidor", last_name="Final", dni="9999999999"):
        # Método constructor para inicializar los atributos de la clase Cliente
        self.first_name = first_name
        self.last_name = last_name
        self.__dni = dni  # Atributo privado para almacenar el número de identificación del cliente
                    
    @property
    def dni(self):
        # Getter para obtener el valor del atributo privado __dni
        return self.__dni
    
    @dni.setter
    def dni(self, value):
        # Setter para asignar un nuevo valor al número de identificación del cliente, con validación de longitud
        if len(value) in (10, 13):
            self.__dni = value
        else:
            self.__dni ="9999999999"  # Retorna el valor predeterminado si la longitud no es válida
  
    def __str__(self):
        # Método especial para representar la clase Cliente como una cadena
        return f'Cliente: {self.first_name} {self.last_name}'  
    
    def fullName(self):
        return self.first_name + ' ' + self.last_name
    
    def show(self):
        # Método para imprimir los detalles del cliente en la consola
        print('   Nombres    Dni')
        print(f'{self.fullName()}  {self.dni}')    

class RegularClient(Client):
    def __init__(self, first_name="Cliente", last_name="Final", dni="9999999999", card=False):
        # Método constructor para inicializar los atributos de la clase RetailClient
        super().__init__(first_name, last_name, dni)  # Llama al constructor de la clase padre
        self.__discount = 0.10 if card else 0  # Descuento del cliente regular
            
    @property
    def discount(self):
        # Getter para obtener el valor del descuento del cliente minorista
        return self.__discount
          
    def __str__(self):
        # Método especial para representar la clase RetailClient como una cadena
        return f'Client:{self.first_name} {self.last_name} Descuento:{self.discount}'
      
    def show(self):
        # Método para imprimir los detalles del cliente minorista en la consola
        print(f'Cliente Minorista: DNI:{self.dni} Nombre:{self.first_name} {self.last_name} Descuento:{self.discount*100}%')     

    def getJson(self):
        # Método para imprimir los detalles del cliente minorista en la consola
        return {"dni":self.dni,"nombre":self.first_name,"apellido":self.last_name,"valor": self.discount}


class VipClient(Client):
    def __init__(self, first_name="Consumidor", last_name="Final", dni="9999999999"):
        # Método constructor para inicializar los atributos de la clase VipClient
        super().__init__(first_name, last_name, dni)  # Llama al constructor de la clase padre
        self.__limit = 10000  # Límite de crédito del cliente VIP
              
    @property
    def limit(self):
        # Getter para obtener el valor del límite de crédito del cliente VIP
        return self.__limit
    
    @limit.setter
    def limit(self, value):
        # Setter para asignar un nuevo valor al límite de crédito del cliente VIP, con validación de rango
        self.__limit = 10000 if (value < 10000 or value > 20000) else value 
  
    def __str__(self):
        # Método especial para representar la clase VipClient como una cadena
        return f'Cliente:{self.first_name} {self.last_name} Cupo: {self.limit}'
            
    def show(self):
        # Método para imprimir los detalles del cliente VIP en la consola
        print(f'Cliente Vip: DNI:{self.dni} Nombre: {self.first_name} {self.last_name} Cupo: {self.limit}')     
        
    def getJson(self):
        # Método para imprimir los detalles del cliente VIP en la consola
        return {"dni":self.dni,"nombre":self.first_name,"apellido":self.last_name,"valor": self.limit}

if __name__ == '__main__':
    
    regular_cli1 = RegularClient() # instancia la clase RegularClient en el objeto regular_cli1 y ejecuta el constructor
    regular_cli2 = RegularClient("Daniel", "Vera", "0914122419", card=True)
    vip_cli1 = VipClient("Erick", "Vera", "0914122412")
    vip_cli2 = VipClient("Yadira", "Bohorquez", "0914122411")
    vip_cli2.limit = 15000
    datos=(2,4,6,8)
    for dat in datos: print(dat*2)
    clients = (regular_cli1, regular_cli2, vip_cli1, vip_cli2)
    for cli in clients: print(cli.getJson())
