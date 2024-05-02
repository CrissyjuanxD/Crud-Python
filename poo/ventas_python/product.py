class Product:
    next = 0
    def __init__(self,id=0, descrip="Ninguno", preci=0, stock=0):
        # Método constructor para inicializar los atributos de la clase Cliente
        Product.next += 1
        # variables de instancias
        #self.__id = Product.next  # Asigna el ID único a la 
        self.__id = id  # Asigna el ID único a la 
        self.descrip = descrip
        self.preci = preci
        self.__stock = stock  # Atributo privado para almacenar el número de identificación del cliente
                    
    @property
    def stock(self):
        # Getter para obtener el valor del atributo privado __stock
        return self.__stock
    
    def __repr__(self):
        # Método especial para representar la clase Cliente como una cadena
        return f'Producto:{self.__id} {self.descrip} {self.preci} {self.stock}'  
    
    def __str__(self):
        # Método especial para representar la clase Cliente como una cadena
        return f'Producto:{self.__id} {self.descrip} {self.preci} {self.stock}'  
    
    def getJson(self):
        # Método especial para representar la clase Cliente como una cadena
        return {"id":self.__id,"descripcion":self.descrip,"precio":self.preci,"stock": self.stock}
      
    def show(self):
        # Método para imprimir los detalles del cliente en la consola
       
        print(f'{self.__id}  {self.descrip}           {self.preci}  {self.stock}')  
          
if __name__ == '__main__':
    # Se ejecuta solo si este script es el principal
    product1 = Product("Aceite",2,1000)
    product2 = Product("Colas",3,5000)
    product3 = Product("leche",1,300)
    # Muestra la información de la primera empresa
    products = []
    products.append(product1)
    products.append(product2)
    products.append(product3)
    # print(products)
    prods=[]
    print('Id Descripcion Precio tock') 
    for prod in products:
      print(prod.getJson())
      prods.append(prod.getJson())
    print(prods)
    # for prod in products: prod.show()
    # prods=[prod.descrip for prod in products if prod.stock <=1000]
    # prods=tuple(prod.descrip for prod in products if prod.stock <=1000)
    # prods=[{"descripcion":prod.descrip} for prod in products if prod.stock <=1000] 
    # print(prods)
    # # lambda es una función anónima y de una sola línea. útiles cuando se necesita una función rápida para un cálculo simple 
    # newPreci= lambda x: x*1.20
    # print(newPreci(10))
    # # map es una función de orden superior que toma dos argumentos: una función y uno o más iterables (por ejemplo, listas, tuplas, etc.) y devuelve un iterador
    # x = map(lambda prod: round(prod.preci*1.20,2),products)
    # print(list(x))