from saleDetail  import SaleDetail
from calculos import Icalculo
from datetime import date
import os
# Colores en formato ANSI escape code
reset_color = "\033[0m"
red_color = "\033[91m"
green_color = "\033[92m"
yellow_color = "\033[93m"
blue_color = "\033[94m"
purple_color = "\033[95m"
cyan_color = "\033[96m"

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
        
class Sale(Icalculo):
    next=0
    FACTOR_IVA=0.12
    def __init__(self,client):
        Sale.next += 1
        self.__invoice = Sale.next
        self.date = date.today()
        self.client = client
        self.subtotal = 0
        self.percentage_discount = client.discount 
        self.discount = 0
        self.iva = 0 
        self.total = 0
        self.sale_detail = []
    
    @property
    def invoice(self):
        # Getter para obtener el valor del límite de crédito del cliente VIP
        return self.__invoice
    
    def __repr__(self):
        # Método especial para representar la clase Cliente como una cadena
        return f'Factura# {self.invoice} {self.date} {self.client.fullName()} {self.total}'  
    
    def cal_iva(self,iva=0.12,valor=0):
        return round(valor*iva,2)
    
    def cal_discount(self,valor=0,discount=0):
        return valor*discount
    
    def add_detail(self,prod,qty):
        # composicion entre detventa y venta
        detail = SaleDetail(prod,qty)
        self.subtotal += round(detail.preci*detail.quantity,2)
        # self.discount = self.subtotal*self.percentage_discount
        self.discount = self.cal_discount(self.subtotal,self.percentage_discount)     
        # self.iva = round((self.subtotal-self.discount)*Sale.FACTOR_IVA,2)
        self.iva = self.cal_iva(Sale.FACTOR_IVA,self.subtotal-self.discount)
        self.total = round(self.subtotal+self.iva-self.discount,2)
        self.sale_detail.append(detail)  
    
    def print_invoice(self,company):
        os.system('cls')
        print('\033c', end='')
        print(green_color+"*"*70+reset_color)   
        print(blue_color+f"Empresa: {company.business_name} Ruc: {company.ruc}",end='')    
        print(" Factura#:{:7}Fecha:{}".format(self.invoice,self.date))
        self.client.show()
        print(green_color+"*"*70+reset_color)  
        print(purple_color+"Linea Articulo Precio Cantidad Subtotal")
        for det in self.sale_detail:
            print(blue_color+f"{det.id:5} {det.product.descrip:6} {det.preci:7} {det.quantity:2} {det.preci*det.quantity:14}")  
        print(green_color+"*"*70+reset_color)    
        print(purple_color+" "*23,"Subtotal:  ",str(self.subtotal))
        print(" "*23,"Descuento: ",str(self.discount))
        print(" "*23,"Iva:       ",str(self.iva))
        print(" "*23,"Total:     ",str(self.total)+reset_color)  

    def getJson(self):
        # Método especial para representar la clase venta como diccionario
        invoice= {"factura":self.invoice,"Fecha":self.date.strftime("%Y-%m-%d")
,"cliente":self.client.fullName(),"subtotal":self.subtotal,"descuento": self.discount,"iva": self.iva,"total": self.total,"detalle":[]}
        for det in self.sale_detail:
            invoice["detalle"].append(
                {"poducto":det.product.descrip,
                "precio": det.preci,
                "cantidad": det.quantity}
            )  
        return invoice
    
    def cal(lista, name):
        name = name.split()[0]
        try:
            subtotal = sum(map(lambda producto: float(producto['precio']) * int(producto['cantidad']), lista))
            # discount = subtotal * 0.10
            json_file = JsonFile(path+'/archivos/clients.json')
            valide = json_file.find("nombre",name)
            valide = valide [0]
            if valide['valor'] !=0:
                discount = subtotal * 0.10
            else:
                discount = subtotal * 0
            iva = subtotal * 0.12
            total = subtotal + iva - discount
            return (subtotal, discount, iva, total)
        except UnboundLocalError:
            return (0, 0, 0, 0)
        
        
