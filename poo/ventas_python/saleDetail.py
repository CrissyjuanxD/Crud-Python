class SaleDetail:
    _line=0
    def __init__(self,product,quantity):
        SaleDetail._line += 1
        self.__id = SaleDetail._line
        self.product = product
        self.preci = product.preci
        self.quantity = quantity
    
    @property
    def id(self):
        # Getter para obtener el valor del límite de crédito del cliente VIP
        return self.__id
    
    def __repr__(self):
        # Método especial para representar la clase Cliente como una cadena
        return f'{self.id} {self.product.descrip} {self.preci} {self.quantity}'  
