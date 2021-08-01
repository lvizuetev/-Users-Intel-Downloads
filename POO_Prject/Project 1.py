from math import pi
from calculadora import CalEstandar, CalCientifica
from operacionesNumeros import Basico , Intermedio

class Menu:
    def __init__(self, titulo="",opciones=[]):
        self.titulo= titulo
        self.opciones= opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc= input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc
opc= ''
while opc !='5': #Menu principal
    menu = Menu ("Menu principal",["1) Calculadora","2) Numeros","3) Listas","4) Cadenas","5) Salir"])
    opc= menu.menu()
    if opc == "1": #Menu calculadora
        opc1 = ''
        while opc1 !='10':
            menu1 = Menu("Menu Calculadora",["1) Suma","2) Resta","3) Multiplicacion", "4) Division","5) Exponente",
            "6) Valor Absoluto","7) Circunferencia","8) Area Circulo", "9) Area Cuadrado","10) Salir"])
            opc1 = menu1.menu()
            if opc1 == "1":
                print("Suma de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese un numero: "))
                calEst = CalEstandar(n1,n2)
                suma= calEst.Suma()
                print("{}+{}={}".format(n1,n2,suma))
                
            opc2 = menu1.menu()
            if opc2 == "2":
                print("Resta de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese un numero: "))
                calEst = CalEstandar(n1,n2)
                resta= calEst.Resta()
                print("{}-{}={}".format(n1,n2,resta))
                    
            opc3 = menu1.menu()
            if opc3 == "3":
                print("Multiplicacion de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese un numero: "))
                calEst = CalEstandar(n1,n2)
                Multi= calEst.Multiplicacion()
                print("{}*{}={}".format(n1,n2,Multi))
                    
            opc4 = menu1.menu()
            if opc4 == "4":
                print("Division de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese un numero: "))
                calEst = CalEstandar(n1,n2)
                Div= calEst.Division()
                print("{}/{}={}".format(n1,n2,Div))
                        
            opc5 = menu1.menu()
            if opc5 == "5":
                print("Exponente de dos numeros")
                n1= int(input("Ingrese un numero: "))
                n2= int(input("Ingrese un numero: "))
                calEst = CalEstandar(n1,n2)
                Exp= calEst.Exponente()
                print("{}**{}={}".format(n1,n2,Exp))
                            
            opc6 = menu1.menu()
            if opc6 == "6":
                print("Valor Absoluto")
                x= int(input("Ingrese un numero: "))
                def Vabsoluto(numero):
                    if numero >= 0:
                        return numero
                    else:
                        return - numero
                print(Vabsoluto(x))
                                
            opc7 = menu1.menu()
            if opc7 == "7":
                print("Circunferencia")
                r= float(input("Ingrese el radio: "))
                CalCientifica= CalCientifica(n1,n2)
                Cir= CalCientifica.Circunferencia()
                print("{}*{}*{}={}".format(2,pi,r,Cir))
                                    
            opc8 = menu1.menu()
            if opc8 == "8":
                print("Area Circulo de un circulo")
                n1= int(input("Ingrese el radio: "))
                CalCientifica = CalCientifica(n1,n2)
                Acirculo= CalCientifica.AreaCirculo()
                print("{}*{}**{}={}".format(pi,r,2,Acirculo))
                                        
            opc9 = menu1.menu()
            if opc9 == "9":
                print("Area Cuadrado de dos numeros")
                l1= float(input("Ingrese valor de un lado: "))
                CalCientifica = CalCientifica(n1,n2)
                Acuadrado= CalCientifica.AreaCuadrado()
                print(Acuadrado(l1))
    elif opc == "2": #Menu operacionesNumeros
        opc2 = ''
        while opc2 != '11':
            menu2=Menu("Menú Operación Números",["1)Presentar los números de 1 a n","2)	Sumar los números de 1 a n","3)Múltiplo de cualquier numero", "4)Presentar los divisores de un numero","5)Numero Primo",
            "6)Factorial de cualquier numero","7)Fibonacci de una serie de n números","8)Perfecto", "9)Primos Gemelos","10)Números Amigos","11)Salir"])
            opc2 = menu2.menu()
            Object = Basico()
            if opc2 == "1":
                print("1)Presentar los números de 1 a n")
                n=int(input("Ingrese la cantidad de números a presentar: "))
                Pre = Object.numerosN(n)
            opc2 = menu2.menu()
            Obj = Intermedio()
            if opc2 == "2":
                print("2)	Sumar los números de 1 a n")
                n=int(input("Ingrese la cantidad de números a sumar: "))
                suma = Obj.numeros(n)
            opc2 = menu2.menu()
            Object = Basico()
            if opc2 == "3":
                print("3)Múltiplo de cualquier numero")
                numero = int(input("Ingrese el primer numero: "))
                multiplo = int(input("Ingrese el primer numero: "))




                
                

    
