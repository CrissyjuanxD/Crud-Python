from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce
import json

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion


def agregar_cliente_a_json(nuevo_cliente, ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            clientes = json.load(archivo)  # Cargar el contenido del archivo JSON en una lista de clientes
    except FileNotFoundError:
        clientes = []  # Si el archivo no existe, inicializar la lista de clientes como vacía

    clientes.append(nuevo_cliente)  # Agregar el nuevo cliente a la lista de clientes

    with open(ruta_archivo, 'w') as archivo:
        json.dump(clientes, archivo, indent=2)  # Guardar la lista actualizada de clientes en el archivo JSON

class CrudClients(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Cliente")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print("Ingrese los datos del cliente:")
        gotoxy(3,6);print("DNI: ", end="")
        dni = self.validar_dni(validar, "", 8, 6)  # Utiliza el método para validar el DNI
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        num_telef = int(input("Numero de telefono: "))

        
        # Crear el objeto cliente
        nuevo_cliente = {"dni": dni, "nombre": nombre, "apellido": apellido, "num_telef": num_telef}
        
        # Guardar el cliente en el archivo JSON
        ruta_archivo_clientes = path + '/archivos/clients.json'	
        agregar_cliente_a_json(nuevo_cliente, ruta_archivo_clientes)
        
        gotoxy(35,9);print("Cliente creado satisfactoriamente")
        time.sleep(2)

    def validar_dni(self, validar, mensaje, x, y):
        while True:
            dni = validar.solo_numeros(mensaje, x, y)
            if len(dni) == 10:
                return dni
            else:
                gotoxy(x,y);print(" " * (len(mensaje) + 30), end="")  # Limpiar línea
                gotoxy(x,y);print("El DNI debe tener exactamente 10 dígitos.", end="")
                time.sleep(2)
                gotoxy(x,y);print(" " * (len(mensaje) + 30), end="")  # Limpiar línea
                


    def update(self):
      validar = Valida()
      borrarPantalla()
      print('\033c', end='')
      gotoxy(2,1);print(green_color+"*"*90+reset_color)
      gotoxy(30,2);print(blue_color+"Actualizacion de Cliente")
      gotoxy(17,3);print(blue_color+Company.get_business_name())
      gotoxy(5,4);print("Ingrese los datos del cliente:")
      gotoxy(3,6);print("DNI: ", end="")
      dni = self.validar_dni(validar, "", 8, 6)
      json = JsonFile(path+'/archivos/clients.json')
      clients = json.read()
      updated_clients = []
      for client in clients:
          if client["dni"] == dni:
              num_telef = int(input("Nuevo número de teléfono: "))
              client["num_telef"] = num_telef
          updated_clients.append(client)

      json.save(updated_clients)
      gotoxy(35,12);print("Numero de telefono actualizado satisfactoriamente")
      time.sleep(2)


  
    def delete(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Eliminación de Cliente")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print("Ingrese los datos del cliente:")
        gotoxy(3,6);print("DNI: ", end="")
        dni = validar.solo_numeros("Error: Solo números", 8, 6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni", dni)
        if not client:
            gotoxy(35,9);print("Cliente no existe")
            time.sleep(2)
            return
        client = client[0]
        json_file.delete(client, "dni")
        gotoxy(35,9);print("Cliente eliminado satisfactoriamente")
        time.sleep(2)

  
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Consulta de Clientes")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        json_file = JsonFile(path+'/archivos/clients.json')
        clients = json_file.read()
        gotoxy(2,4);print("DNI"+" "*10+"Nombre"+" "*10+"Apellido"+" "*10+"Num.Telefono")
        gotoxy(2,5);print("="*90)
        line = 6
        for client in clients:
            gotoxy(2,line);print(f"{client['dni']}   {client['nombre']}   {client['apellido']}   {client['num_telef']}")
            line += 1
        x = input("Presione una tecla para continuar...")

        return clients
    
class CrudProducts(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Producto")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print("Ingrese los datos del producto:")
        gotoxy(3,6);print("ID: ", end="")
        id = int(validar.solo_numeros("Error: Solo numeros", 8, 6))
        descrip = input("Descripcion: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        nuevo_producto = {"id": id, "descripcion": descrip, "precio": precio, "stock": stock}
        ruta_archivo_productos = path + '/archivos/products.json'
        agregar_cliente_a_json(nuevo_producto, ruta_archivo_productos)
        
        gotoxy(35,9);print("Producto creado satisfactoriamente")
        time.sleep(2)
    
    def update(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Actualización de Producto")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print("Ingrese los datos del producto:")
        gotoxy(3,6);print("ID: ", end="")
        id = int(validar.solo_numeros("Error: Solo números", 8, 6))
        json_file = JsonFile(path+'/archivos/products.json')
        products = json_file.read()
        product_found = False
        for product in products:
            if product["id"] == id:
                product_found = True
                gotoxy(3,7);print("Stock actual: ", product["stock"])
                gotoxy(3,8);print("Ingrese nuevo stock: ", end="")
                new_stock = validar.solo_numeros("Error: Solo números", 23, 8)
                product["stock"] = new_stock
                gotoxy(35,10);print("Stock actualizado satisfactoriamente")
                time.sleep(2)
        if not product_found:
            gotoxy(35,10);print("Producto no encontrado")
            time.sleep(2)
            return
        json_file.save(products)

    
    def delete(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Eliminación de Producto")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print("Ingrese los datos del producto:")
        gotoxy(3,6);print("ID: ", end="")
        id = int(validar.solo_numeros("Error: Solo números", 8, 6))
        json_file = JsonFile(path+'/archivos/products.json')
        product = json_file.find("id", id)
        if not product:
            gotoxy(35,9);print("Producto no existe")
            time.sleep(2)
            return
        product = product[0]
        json_file.delete(product, "id")
        gotoxy(35,9);print("Producto eliminado satisfactoriamente")
        time.sleep(2)
    
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Consulta de Productos")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        json_file = JsonFile(path+'/archivos/products.json')
        products = json_file.read()
        gotoxy(2,4);print("ID"+" "*10+"Descripcion"+" "*10+"Precio"+" "*10+"Stock")
        gotoxy(2,5);print("="*90)
        line = 6
        for product in products:
            gotoxy(2,line);print(f"{product['id']}   {product['descripcion']}   {product['precio']}   {product['stock']}")
            line += 1
        x = input("Presione una tecla para continuar...")

        return products

class CrudSales(ICrud):
    def create(self):
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(15,6);print("Cedula:")
        dni=validar.solo_numeros("Error: Solo numeros",23,6)
        json_file = JsonFile(path+'/archivos/clients.json')
        client = json_file.find("dni",dni)
        if not client:
            gotoxy(35,6);print("Cliente no existe")
            return
        client = client[0]
        cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
        sale = Sale(cli)
        gotoxy(35,6);print(cli.fullName())
        gotoxy(2,8);print(green_color+"*"*90+reset_color) 
        gotoxy(5,9);print(purple_color+"Linea") 
        gotoxy(12,9);print("Id_Articulo") 
        gotoxy(24,9);print("Descripcion") 
        gotoxy(38,9);print("Precio") 
        gotoxy(48,9);print("Cantidad") 
        gotoxy(58,9);print("Subtotal") 
        gotoxy(70,9);print("n->Terminar Venta)"+reset_color)
        # detalle de la venta
        follow ="s"
        line=1
        while follow.lower()=="s":
            gotoxy(7,9+line);print(line)
            gotoxy(15,9+line);
            id=int(validar.solo_numeros("Error: Solo numeros",15,9+line))
            json_file = JsonFile(path+'/archivos/products.json')
            prods = json_file.find("id",id)
            if not prods:
                gotoxy(24,9+line);print("Producto no existe")
                time.sleep(1)
                gotoxy(24,9+line);print(" "*20)
            else:    
                prods = prods[0]
                product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                gotoxy(24,9+line);print(product.descrip)
                gotoxy(38,9+line);print(product.preci)
                gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros",49,9+line))
                gotoxy(59,9+line);print(product.preci*qyt)
                sale.add_detail(product,qyt)
                gotoxy(76,4);print(round(sale.subtotal,2))
                gotoxy(76,5);print(round(sale.discount,2))
                gotoxy(76,6);print(round(sale.iva,2))
                gotoxy(76,7);print(round(sale.total,2))
                gotoxy(74,9+line);follow=input() or "s"  
                gotoxy(76,9+line);print(green_color+"✔"+reset_color)  
                line += 1
        gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
        gotoxy(54,9+line);procesar = input().lower()
        if procesar == "s":
            gotoxy(15,10+line);print("😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            # print(sale.getJson())  
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            ult_invoices = invoices[-1]["factura"]+1
            data = sale.getJson()
            data["factura"]=ult_invoices
            invoices.append(data)
            json_file = JsonFile(path+'/archivos/invoices.json')
            json_file.save(invoices)
        else:
            gotoxy(20,10+line);print("🤣 Venta Cancelada 🤣"+reset_color)    
        time.sleep(2)    
    
    def update(self):
        validar = Valida()
        sale = Sale
        print('\033c', end='')
        gotoxy(2, 1); print('\033[1;36m' + "█"*90)
        gotoxy(2, 2); print('\033[1;36m' + "██" + " "*34 + "Actualización de Factura" + " "*35 + "██")
        print("Ingrese el número de factura a actualizar: ")
        gotoxy(2, 4); invoice_number = validar.solo_numeros("Error: Solo Numeros", 44, 3).strip()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2, 1); print('\033[1;36m' + "█"*90)
        gotoxy(2, 2); print('\033[1;36m' + "██" + " "*34 + "Actualización de Factura" + " "*35 + "██")
        if invoice_number.isdigit():
            invoice_number = int(invoice_number)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            invoice_found = False
            for invoice in invoices:
                if invoice["factura"] == invoice_number:
                    invoice_found = True
                    gotoxy(2, 5); print(f"-"*109)
                    gotoxy(48, 5); print('\033[1;35m' + f"Impresion de la Factura # {invoice_number}" + '\033[0m')
                    gotoxy(5, 6); print('\033[1;33m' + "Factura" + '\033[0m')
                    gotoxy(8, 7); print(f"{invoice_number}")
                    gotoxy(18, 6); print('\033[1;33m' + "Fecha" + '\033[0m')
                    gotoxy(16, 7); print(f"{invoice['Fecha']}")
                    gotoxy(33, 6); print('\033[1;33m' + "Cliente" + '\033[0m')
                    gotoxy(31, 7); print(f"{invoice['cliente']}")
                    gotoxy(48, 6); print('\033[1;33m' + "Subtotal" + '\033[0m')
                    gotoxy(50, 7); print(f"{invoice['subtotal']}")
                    gotoxy(64, 6); print('\033[1;33m' + "Descuento" + '\033[0m')
                    gotoxy(67, 7); print(f"{invoice['descuento']}")
                    gotoxy(80, 6); print('\033[1;33m' + "IVA" + '\033[0m')
                    gotoxy(80, 7); print(f"{invoice['iva']}")
                    gotoxy(91, 6); print('\033[1;33m' + "Total" + '\033[0m')
                    gotoxy(91, 7); print(f"{invoice['total']}")
                    gotoxy(2, 9); print("-"*109)
                    gotoxy(48, 9); print('\033[1;35m' + "Impresion de los Detalles" + '\033[0m')
                    linea_x = 2
                    linea_y = 11
                    for idx, detalle in enumerate(invoice['detalle'], 1):
                        gotoxy(linea_x, linea_y)
                        print('\033[1;36m' + f"Producto {idx}:" + '\033[0m')
                        gotoxy(linea_x, linea_y + 1)
                        print('\033[1;37m' + f"Producto: {detalle['poducto']}" + '\033[0m')
                        gotoxy(linea_x, linea_y + 2)
                        print('\033[1;37m' + f"Precio: {detalle['precio']}" + '\033[0m')
                        gotoxy(linea_x, linea_y + 3)
                        print('\033[1;37m' + f"Cantidad: {detalle['cantidad']}" + '\033[0m')
                        linea_x += 25
                    gotoxy(2, 16); print("-"*109)
                    gotoxy(2, 18);input("Presione Enter para seguir...")
                    borrarPantalla()
                    print('\033c', end='')
                    gotoxy(2, 1); print('\033[1;37m' + "█"*90)
                    gotoxy(2, 2); print('\033[1;37m' + "██" + " "*34 + "Actualización de Factura" + " "*35 + "██")
                    print('\033[0m' + "¿Qué desea actualizar?")
                    print('\033[0m' + "1. Fecha")
                    print('\033[0m' + "2. Cliente")
                    print('\033[0m' + "3. Subtotal")
                    print('\033[0m' + "4. Descuento")
                    print('\033[0m' + "5. Iva")
                    print('\033[0m' + "6. Total")
                    print('\033[0m' + "7. Detalle (Agregar/Actualizar/Eliminar)")
                    print('\033[0m' + "8. Cancelar")
                    gotoxy(1, 13); print('\033[0m' + 'Seleccione una opcion:', end="")
                    gotoxy(1, 13); opcion = validar.solo_numeros("Error: Solo numeros", 24, 13)

                    if opcion == '1':
                        print('\033[1;37m' + "Ingrese la nueva fecha (YYYY-MM-DD): " + '\033[0m')
                        nueva_fecha = validar.solo_fecha("Error: Solo Formato de Fecha", 39, 14)
                        invoice["Fecha"] = nueva_fecha
                    elif opcion == '2':
                        gotoxy(2, 14); print("Ingrese el nuevo cliente: ")
                        gotoxy(2, 15); nuevo_cliente = validar.solo_letras("Ingrese el nuevo cliente: ", "Error: Solo letras").lower().capitalize()
                        invoice["cliente"] = nuevo_cliente
                    elif opcion == '3':
                        gotoxy(2, 14); print('\033[1;37m' + "Ingrese el nuevo subtotal: " + '\033[0m')
                        gotoxy(2, 14); nuevo_subtotal = validar.solo_decimales("Ingrese el nuevo subtotal: ", "Error: Solo numeros")
                        invoice["subtotal"] = float(nuevo_subtotal)
                    elif opcion == '4':
                        gotoxy(2, 14); print('\033[1;37m' + "Ingrese el nuevo descuento: " + '\033[0m')
                        gotoxy(2, 14); nuevo_descuento = validar.solo_decimales("Ingrese el nuevo descuento: ", "Error: Solo numeros") 
                        invoice["descuento"] = float(nuevo_descuento)
                    elif opcion == '5':
                        gotoxy(2, 14); print('\033[1;37m' + "Ingrese el nuevo IVA: " + '\033[0m')
                        gotoxy(2, 14); nuevo_iva = validar.solo_decimales("Ingrese el nuevo IVA: ", "Error: Solo numeros") 
                        invoice["iva"] = float(nuevo_iva)
                    elif opcion == '6':
                        gotoxy(2, 14); print('\033[1;37m' + "Ingrese el nuevo total: " + '\033[0m')
                        gotoxy(2, 14); nuevo_total = validar.solo_decimales("Ingrese el nuevo total: ", "Error: Solo numeros")
                        invoice["total"] = float(nuevo_total)
                    elif opcion == '7':
                        subopcion = input("¿Qué desea hacer en el detalle? ( 1)agregar / 2)actualizar / 3)eliminar): ")
                        borrarPantalla()
                        print('\033c', end='')
                        gotoxy(2, 1); print('\033[1;37m' + "█"*90)
                        gotoxy(2, 2); print('\033[1;37m' + "██" + " "*34 + "Actualización de Factura" + " "*35 + "██")
 
                        if subopcion == '1':
                            # Agregar nuevo producto al detalle
                            print('\033[0m' + "Ingrese el nombre del producto: ")
                            producto_nuevo = validar.solo_letras("Ingrese el nombre del producto: ", "Error: Solo Letras").lower().capitalize()

                            json_file1 = JsonFile(path+'/archivos/products.json')
                            products = json_file1.read()
                            product_vali = None
                            for product in products:
                                if product["descripcion"].lower() == producto_nuevo.lower():
                                    product_vali = product
                                    break

                            if product_vali is None:
                                print("producto no existe")
                                time.sleep(1)
                                return
                            precio_nuevo = product_vali["precio"]
                            gotoxy(2,4);print(f'Precio del producto:{precio_nuevo}')
                            #print('\033[0m' + "Ingrese el precio del producto: ")
                            #precio_nuevo = validar.solo_decimales("Error: Solo Numeros",33,4)
                            print('\033[0m' + "Ingrese la cantidad del producto: ")
                            cantidad_nueva = validar.solo_numeros("Error: Solo Numeros",35,5)
                            nuevo_detalle = {"poducto": producto_nuevo, "precio": precio_nuevo, "cantidad": int(cantidad_nueva)}
                            invoice["detalle"].append(nuevo_detalle)
                            subtotal, discount, iva, total = sale.cal(invoice["detalle"], invoice["cliente"])
                            invoice["subtotal"] = round(subtotal, 2)
                            invoice["descuento"] = round(discount, 2)
                            invoice["iva"] = round(iva, 2)
                            invoice["total"] = round(total, 2)
                            print('\033[0m' + "Producto agregado al detalle.")
                            json_file.save(invoices)
                            break
                        
                        elif subopcion == '2':
                            # Mostrar detalle actual y permitir actualizar precio o cantidad
                            print('\033[0m' + "Qué producto quiere actualizar (Ingrese el nombre): ")
                            subopcion_update = validar.solo_letras("Error: Solo Letras",54,3).lower().capitalize()
                            invoice["detalle"]
                            for product in invoice["detalle"]:
                                if product["poducto"] == subopcion_update:
                                    print('\033[0m' + "ok, ingresa los nuevos datos:\n")
                                    print('\033[0m' + 'Ingresa el nuevo nombre:')
                                    product_new = validar.solo_letras("Error: Solo letras",26,6).lower().capitalize()
                                    json_file2 = JsonFile(path+'/archivos/products.json')
                                    product_vali = json_file2.find("descripcion",product_new)
                                    if not product_vali:
                                        print("producto no existe")
                                        time.sleep(1)
                                        return
                                    product_vali = product_vali[0]
                                    product["poducto"] = product_new
                                    product["precio"] = product_vali["precio"]
                                    gotoxy(2,7);print('\033[0m' + f"Precio del producto: {product['precio']}")
                                    print('\033[0m' + 'Ingresa la nueva cantidad:')
                                    product["cantidad"] = validar.solo_numeros("Error: Solo Numeros",29,8)
                                    subtotal, discount, iva, total = sale.cal(invoice["detalle"],invoice["cliente"])
                                    invoice["subtotal"] = round(subtotal, 2)
                                    invoice["descuento"] = round(discount, 2)
                                    invoice["iva"] = round(iva, 2)
                                    invoice["total"] = round(total, 2)
                                    json_file.save(invoices)
                            else:
                                print('\033[0m' + "Producto no encontrado en la factura")
                                time.sleep(1)

                            
                        elif subopcion == '3':
                            if len(invoice["detalle"]) == 1:
                                print('\033[0m' + "Solo queda un producto. Si elimina el ultimo producto, se le borrara automaticamente toda la factura")
                                print('\033[0m' + "¿Desea eliminar el producto? (s/n):")
                                opcion_eliminar_factura = validar.solo_letras("Error: Solo Letras",39,4)
                                if opcion_eliminar_factura.lower() == "s" or opcion_eliminar_factura.lower() == "si":
                                    invoices.remove(invoice)
                                    json_file.save(invoices)
                                    print('\033[0m' + "Factura eliminada.")
                                    break
                                else:
                                    print('\033[0m' + "Eliminacion de Factura Cancelada...")
                                    break

                            # Mostrar detalle actual y permitir eliminar un producto
                            print('\033[0m' + 'Qué producto quiere eliminar (Ingrese el nombre): ')
                            subopcion_update = validar.solo_letras("Error: Solo letras",51,3).lower().capitalize()
                            for i, product in enumerate(invoice["detalle"]):
                                if product["poducto"] == subopcion_update:
                                    del invoice["detalle"][i]
                                    subtotal, discount, iva, total = sale.cal(invoice["detalle"],invoice["cliente"])
                                    invoice["subtotal"] = round(subtotal, 2)
                                    invoice["descuento"] = round(discount, 2)
                                    invoice["iva"] = round(iva, 2)
                                    invoice["total"] = round(total, 2)
                                    print('\033[0m' + "Producto eliminado.")
                                    json_file.save(invoices)
                                    break
                            else:
                                print('\033[0m' + "Producto no encontrado.")

                        else:
                            print("Opción no válida.")
                            break
                    elif opcion == '8':
                        print("Operación de actualización cancelada.")
                        break
                    else:
                        print("Opción no válida.")
                        break
                    
                    json_file.save(invoices)
                    break

            if not invoice_found:
                print(f"No se encontró la factura con el número {invoice_number}.")
        else:
            print("Por favor, ingrese un número de factura válido.")

        input("Presione una tecla para continuar...")

    
    def delete(self):
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"--- Eliminación de Factura ---")
        # Obtener detalles del producto
        invoice = input(">>> Ingrese el # de Factura a eliminar: ")
        if invoice.isdigit():
            invoice = int(invoice)
            json_file = JsonFile(path+'/archivos/invoices.json')
            dato = json_file.read()
            invoices = json_file.find("factura",invoice)            
            if invoices:
                dato.remove(invoices[0])
                json_file.save(dato)
                print("+++ # Factura eliminada exitosamente. ", end="")
                time.sleep(1)  
                print(green_color + "✔" + reset_color)  
                time.sleep(3) 
            else:
                print("!!! # Factura inexistente. !!!")
        else:
            print("!!! # Factura inválida. !!!")
            
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Venta"+" "*35+"██")
        gotoxy(2,4);invoice= input("Ingrese Factura: ")
        if invoice.isdigit():
            invoice = int(invoice)
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.find("factura",invoice)
            print(f"\nFactura N° {invoice}")
            for invoice in invoices:
                print("\nFecha:", invoice['Fecha'])
                print("Cliente:", invoice['cliente'])
                print("\nDetalle:")
                print(green_color + "*" * 70 + reset_color)
                print("Articulo\tPrecio\tCantidad\tSubtotal")
                for detail in invoice['detalle']:
                    print(f"{detail['poducto']}\t{detail['precio']}\t{detail['cantidad']}\t{detail['precio']*detail['cantidad']}")
                print(green_color + "*" * 70 + reset_color)
                print("\nSubtotal:", invoice['subtotal'])
                print("Descuento:", invoice['descuento'])
                print("IVA:", invoice['iva'])
                print("Total:", invoice['total'])
        else:    
            json_file = JsonFile(path+'/archivos/invoices.json')
            invoices = json_file.read()
            print("Consulta de Facturas")
            for invoice in invoices:
                print("\nFactura N°:", invoice['factura'])
                print("Fecha:", invoice['Fecha'])
                print("Cliente:", invoice['cliente'])
                print("Total:", invoice['total'])
            
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), 
            invoices,0)
            totales_map = list(map(lambda invoice: invoice["total"], invoices))
            total_client = list(filter(lambda invoice: invoice["cliente"] == "Dayanna Vera", invoices))

            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = sum(totales_map)
            print("\nResumen:")
            print("Total de facturas:", tot_invoices)
            print("Factura máxima:", max_invoice)
            print("Factura mínima:", min_invoice)
            print("Total acumulado:", suma)
        x=input("presione una tecla para continuar...")


#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu("Menu Facturacion",["1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()    
            menu_clients = Menu("Menu Cientes",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                borrarPantalla()
                client = CrudClients()
                client.create()
            elif opc1 == "2":
                borrarPantalla()
                client = CrudClients()
                client.update()
            elif opc1 == "3":
                borrarPantalla()
                client = CrudClients()
                client.delete()
            elif opc1 == "4":
                borrarPantalla()
                client = CrudClients()
                client.consult()
                time.sleep(2)
            print("Regresando al menu Clientes...")
            # time.sleep(2)            
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()    
            menu_products = Menu("Menu Productos",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
            opc2 = menu_products.menu()
            if opc2 == "1":
                borrarPantalla()
                product = CrudProducts()
                product.create()
            elif opc2 == "2":
                borrarPantalla()
                product = CrudProducts()
                product.update()
            elif opc2 == "3":
                borrarPantalla()
                product = CrudProducts()
                product.delete()
            elif opc2 == "4":
                borrarPantalla()
                product = CrudProducts()
                product.consult()
                time.sleep(2)
    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu("Menu Ventas",["1) Registro Venta","2) Consultar","3) Modificar","4) Eliminar","5) Salir"],20,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()
                
            elif opc3 == "2":
                sales.consult()
                time.sleep(2)
            elif opc3 == "3":
                sales.update()
            elif opc3 == "4":
                sales.delete()
            print("Regresando al menu Ventas...")
            
     
    print("Regresando al menu Principal...")       

borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()

