from crudArhivos import Archivo
from clases import Empleado,Proveedor
from componentes import Menu,Valida    
from helpers import *
import time
# emp = Empleado(10,"Andy","0914",5000.50)
# #emp2 = Empleado(11,"Luis","0914",5000.50)
# dat = [emp.getDatosString()]
# archEmp = Archivo("empleados.txt","|")
# archEmp.escribir(dat,"a")
def proveedores():
    #codigo = input("Ingrese Codigo: ")
    nombre = input("Ingrese nombre: ")
    ced = input("Ingrese cedula: ")
    archProv = Archivo("proveedore.txt","|")
    proveedores = archProv.leer()
    #[[1,'ana','4543455'],[2,'jose','0912'],['3','juan','0987']]
    #        0                     1            -1
    idSig=1
    if proveedores : idSig = int(proveedores[-1][0])+1
    pro = Proveedor(idSig,nombre,ced)
    datos = [pro.getDatosString()]
    archProv = Archivo("proveedore.txt","|")
    archProv.escribir(datos,"a")
    print("Registro del proveedor Grabado...")
    time.sleep(3)
    
def consultas():
   opc1 = ""
   while opc1 != "4":
        borrarPantalla()
        men = Menu("Menu Consultas",["1) Consulta Proveedores","2) Consulta Facturas","3) Consulta Pagos","4) Salir"])
        opc1=men.menu()
        if opc1 == "1":
            consultaProveedores()
        elif opc1 =="2":
            pass
        elif opc1 =="3":
            pass
        elif opc1 == "4":
            print("Gracias por su visita")
                
def consultaProveedores():
    print("Listado de Proveedores")
    archProv = Archivo("proveedore.txt","|")
    proveedores = archProv.leer()
    print("codigo nombre cedula")
    for prov in proveedores:
        print(prov[0],"  ",prov[1]," ",prov[2])
    time.sleep(5)  
    
opc = ""
while opc != "3":
    borrarPantalla()
    men = Menu("Menu Principal",["1) Proveedores","2) Consultas","3) Salir"])
    opc=men.menu()
    if opc == "1":
        proveedores()
    elif opc =="2":
        consultas()
    elif opc == "3":
        print("Gracias por su visita")
   

#emp.mostrar()
#datos = emp.getDatos()
# with open("empleados.txt", 'a') as w:
#         #dat = "|".join(datos)+"\n"
#         lista = [emp.getDatosString(),emp2.getDatosString()]
#         for dat in lista:
#             w.write(dat+"\n")

