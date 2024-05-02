class Archivo:
    def __init__(self,nombreArchivo,separador=';'):
        self.__archivo = nombreArchivo
        self.__separador = separador
        
    def leer(self):
        try:
          with open(self.__archivo, 'r', encoding="UTF-8") as file:
            lista=[] 
            for linea in file:
     
              line = linea[:-1].split(self.__separador)
              
              lista.append(line)
        except IOError:
           lista=[]    
        return lista       
    
    def buscar(self,buscado): 
        resultado = [] 
                      
        with open(self.__archivo, mode='r', encoding='utf-8') as file:
            for linea in file:
               if linea[:-1].split(self.__separador)[0].find(buscado) is not -1 :
                    resultado = linea[:-1].split(self.__separador)
        return resultado
   
    def buscarLista(self,buscado):
        resultado = []
        with open(self.__archivo, mode='r', encoding='utf-8') as file:
            for linea in file:
                registro = linea[:-1].split(self.__separador) 
                if registro[0] == buscado:
                    resultado.append(registro)
        return resultado
     
    def buscar2(self,buscado1,buscado2):
        resultado = []
        with open(self.__archivo, mode='r', encoding='utf-8') as file:
            for linea in file:
                registro = linea[:-1].split(self.__separador) 
                if registro[1] == buscado1 and registro[2] == buscado2:
                    resultado = registro
        return resultado
             
    def escribir(self,datos,modo):
         with open(self.__archivo, modo, encoding="UTF-8") as file:
           for dato in datos:
             file.write(dato+'\n')
             
    def escribirM(self,datos,modo):
      with open(self.__archivo, modo, encoding="UTF-8") as file:
        for dato in datos:
          linea=''
          for valor in dato:
            if type(valor) == int or float: linea +=str(valor)+self.__separador
            else: linea += valor + self.__separador     
          file.write(linea[:-1]+"\n")            

# arch = Archivo("./archivos/cargo.txt","|")
# cargos = [[1,"Informatico"],[2,"Analista"]]
# #arch.escribir(["Daniel","Ana","Jose"],"w")  
# arch.escribirM(cargos,"a")  
# lista = arch.leer()
# #sig = int(lista[len(lista)-1][0])+1
# print(lista)
