# def __init__ (self):
#     pass
# def inseLista(self):
    
#6) (sin funciones no sabia como resolverlo)
# lista= [10,20,30,40]
# print(lista)
# print("Insertar un valor en una posicion dada")
# valor= int(input("ingrese un valor entero: "))
# pos= int(input("Ingrese una posicion: "))
# lista.insert(pos, valor)
# print(lista)
# #elimine un valor de la lista
# eli=int(input("Ingrese el valor entero que desea eliminar de la lista: "))
# for x in range (len(lista)-1,-1,-1):
#     if lista[x] == eli:
#         print(lista.pop(x))
# print(lista)
    def presentarLista(self):
        print("Ingrese una lista:")    
        op = 'y'
        while op != 'n':
            data = input("Ingrese los datos de la lista :")
            self.__l1.append(data)
            op = input('Desea continuar (Si = Y / no = N): ').lower()
        print(self.__l1)
    def buscarLista(self,valor):
        self.presentarLista()
        for i in self.__l1:
            if i == valor:
                print(f"El valor que busca se encuentra en : {i}" )
            else:
                print(f"El valor {valor} que ingreso no se encuentra en la lista")
    def listaFactorial(self): 
        self.presentarLista()
        fact = []
        def fact_1(n):
            factorial_total = 1
            while n > 1:
                factorial_total *= n
                n -= 1
            return factorial_total
        for i in self.__l1:
            fact.append(int(i))
        for j in fact:
            d = fact_1(j)
            print(d)
    def listaPrimo(self):
        self.presentarLista()
        v = []
        def es_primo(num):
            for n in range(2, num):
                if num % n == 0:
                    return False
            return True
        for i in self.__l1:
            v.append(int(i))
        for j in v:
            r = es_primo(j)
            if r == True:
                print(j)
    def listaNotas(self,dic:list):
        for i in dic:
            print(i)
    def insertarLista(self,valor,posicion:int):
        self.presentarLista()
        self.__l1.insert(posicion,valor)
        print(self.__l1)
    def eliminarLista(self,valor:str):
        self.presentarLista()
        valor = str(valor)
        for i in self.__l1:
            c = self.__l1.count(valor)
            if c > 1:
                h = self.__l1.index(valor)
                self.__l1.pop(h) 
        print(self.__l1)
    def retornaValorLista(self,posicion):
        self.presentarLista()
        posicion = int(posicion)
        print(posicion)
        valor = self.__l1[posicion]
        self.__l1.pop(posicion)
        print(self.__l1)
        return valor
    def copiarTuplaLista(self,tupla):
        for i in tupla:
            self.__l1.append(i)
        print(self.__l1)