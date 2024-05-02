numeros = [10,30,40,50]
#           0 1  2   3
numeros[0]=20
numeros.append(60)
usuario = ("ana",123,True)
#usuario[0]="Jose" la tupla no se puede modificar
alumno = {"nombre":"Jose","edad":20}
alumno['nombre']="Elian"
alumno["nota"]=70
"""print(numeros)
print(usuario)
print(alumno.items())"""
# valores= range(1,12,2) #(1,3,5,7,9,11)
# print(valores)
# for valor in valores:
#     print(valor)
# print(numeros,numeros[0],numeros[1:3],numeros[-1])   
# print([20]) 
# pos=0
# for num in numeros:
#     if pos%2!=0:
#         print(num)
#     pos=pos+1   

# rango=(range(len(numeros)))#(0,5)
# print(rango)
# for pos in rango:
#     if pos%2!=0:
#          print(f'{pos}->{numeros[pos]}')   
           
# for pos,valor in enumerate(numeros):
#     if pos%2!=0:
#         print(f'{pos}->{valor}')
# for ele in usuario:
#     print(ele)

# for clave,valor in alumno.items():
#     print(clave,": ",valor)
#print("nombre:",alumno["nombre"]," ",alumno["edad"])

# datos=["ana",30,500.50]
# cadena1 = datos[0]+";"+str(datos[1])+";"+str(datos[2])+"\n"
# datos2=["ana","30","500.50"]
# cadena2= "|".join(datos2)
# print(cadena2)
nume =[    20      ,     40,              50]
    #       0            1                 2
lista=[["1","ana","50"],["2","dan","30"],["3","ruth","40"],["4","Juan","40"]]
    #    0    1     2      0     1   2     0     1     2
list = lista[-1]
id = int(lista[-1][0])+1
lista.append([id,"Miguel","60"])
#print(f'codigo:{id}')
for lis in lista:
    #print(lis)
    print(lis,lis[0],lis[1],lis[2])
    # for ele in lis:
    #     print(ele)

#sublista=lista[-1]
#cod=sublista[0]
#print(sublista,sublista[0])
# codsig=int(lista[-1][0])+1
# nombre = input("Nombre: ")
# edad= input("Edad:")
# datos=[str(codsig),nombre,edad]
       
# with open("empleados.txt", 'a') as w:
#         dat = "|".join(datos)+"\n" 
#         w.write(dat)
        
