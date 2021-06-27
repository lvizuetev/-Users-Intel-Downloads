class Ejercicios:
    def __init__(self):
        pass
    def compra(self):
        TC= float(input("Ingrese la Cantidad total de la compra: "))
        Des= (TC * 0.15)
        TP= TC - Des
        print("El Total a pagar por su compra es:{}".format(TP))
    def Ventas(self):
        SB= float(input("Ingrese su  sueldo base:"))
        venta1= float(input("Ingrese la cantidad de la primer venta: "))
        venta2= float(input("Ingrese la cantidad de la segunda venta: "))
        venta3= float(input("Ingrese la cantidad de la tercer venta: "))
        TotalV= (venta1+venta2+venta3)
        Comi= TotalV * 0.1
        TSR= SB+Comi
        print("El sueldo total a recibir más comisiones es:{}".format(TSR))
        
    def Calificacion(self):
         Cal= float(input("Ingrese su calificación: "))
         if Cal >= 7:
             print("Aprobado, cumple con la calificación requerida")
         else:
             print("No cumple con la calificación requerida")

comp1= Ejercicios()
comp1.compra()
ven1=Ejercicios()
ven1.Ventas()
cali1=Ejercicios()
cali1.Calificacion()

class MasEjercicios:
    def __init__(self):
        pass
    def Aumento(self):
        Sueldo= float(input("Ingrese su sueldo: "))
        CA= Sueldo * 0.1
        if Sueldo <= 600:
            NS= Sueldo + CA
            print("Su Sueldo Actual añadido el aumento es:{}".format(NS))
        else:
            print("Su sueldo no aplica para el aumento")

    def HorasEx(self):
        nuhotra= int(input("Ingrese el número de horas trabajadas este mes: "))
        phn= int(input("Ingrese el pago de sus horas de trabajo normal: "))
        pht=0
        Phd=0
        Sueldo=0
        if nuhotra > 48:
            pht= nuhotra - 48
            Phd= 8
            Sueldo= (40*phn) + (Phd*phn*2) + (pht*phn*3)
            print("El sueldo total más las horas extras es:{}".format(Sueldo))
        else:
            if nuhotra > 40 :
                Phd= nuhotra-40
                Sueldo= (40*phn) + (Phd*phn*2)
                print("El sueldo total más las horas extras es:{}".format(Sueldo))
            else:
                Sueldo= nuhotra*phn
                print("El sueldo sin horas extras es:{}".format(Sueldo))

    def NumeroMayor(self):
        nu1= int(input("Ingrese un número entero: "))
        nu2= int(input("Ingrese un número entero: "))
        nu3= int(input("ingrese un número entero: "))
        if (nu1>nu2)  and (nu1>nu3):
            NM= nu1
            print("El número entero mayor ingresado es:{}".format(NM))
        elif (nu2>nu3):
            NM=nu2
            print("El número entero mayor ingresado es:{}".format(NM))
        else:
            NM= nu3
            print("El número entero mayor ingresado es:{}".format(NM))
    def dosVariables(self):
        numero= int(input("Ingrese el número: "))   
        V= int(input("ingrese el número: "))     
        if numero==1:
            resul= 100*V
            print("El resultado de la función es:{}".format(resul))
        elif  numero==2:
            resul= 100**V
            print("El resultado de la función es:{}".format(resul))
        elif numero==3:
            resul=100/V
            print("El resultado de la función es:{}".format(resul))
        else:
            resul= 0
            print("El resultado de para este número ingresado es:{}".format(resul))
    def ExAspirante(self):
        Examen1= float(input("Ingrese su califiación del primer exámen: "))
        Examen2= float(input("Ingrese su califiación del primer exámen: "))
        if (Examen1>= 80) and (Examen2>=80):
            print("--¡El estudiante ha sido aceptado!--")
        else:
            print("Sus calificaciones obtenidas no son suficientes")

    def SumaE(self):
        suma= 0
        for i in range(1 , 100 + 1):
            suma+= i*2
            print("La suma de los numeros es: {}".format(suma))
            
            

Au1= MasEjercicios()
Au1.Aumento()
hoex1= MasEjercicios()
hoex1.HorasEx()
Nent= MasEjercicios()
Nent.NumeroMayor()
varia=MasEjercicios()
varia.dosVariables()
Aspirante1= MasEjercicios()
Aspirante1.ExAspirante()
sum1= MasEjercicios()
sum1.SumaE()

class Deber:
    def __init__(self):
         pass
    def numeros(self):
        i=1
        while i<=100:
            print(i)
            i+= 1
        print("programa finalizado!")
    def operaciones(self):
        suma= 0
        producto=1
        resp=(input("Digite N o n para salir del ciclo: "))
        
        while (resp != 'N' )and (resp != 'n'):
            num=int(input("ingrese numero: "))
            suma= suma + num
            producto= producto * num
            resp=(input("Digite N  para salir del ciclo o  S para seguir: "))
            if resp == 'N':
               print("El resultado de la suma es:{}".format(suma))
               print("El resultado de el producto es:{}".format(producto))
           


    def centinela(self):
        S=0
        P=1
        Num=int(input("Ingrese el numero: "))
        while (Num != -1 ):
            S= S + Num
            P= P * Num
        print("El total de la suma es:{}".format(S))
        print("El total de el producto es:{}".format(P))
    def primo(self):
        numero= int(input("¿Ingresa el número que deseas saber si es primo: "))
        valor= range(2,numero)
        contador = 0
        for n in valor:
            if numero % n == 0:
                contador +=1
            print("divisor:", n)
  
        if contador > 0 :
           print("El número no es primo" )
        else:
           print("El nÚmero es primo")
    def Factorial(self):
        numero=int(input("Ingrese el número: "))
        factorial= 1 
        if numero != 0:
            for i in range(1, numero+1):
                factorial= factorial*i
            print("El numero factorial es:{}".format(factorial))
    def vectorC(self):
        TL= int(input("Ingrese el tamaño de la Lista: "))
        Lista=[None]*(TL+1)
        for I in range(1,TL+1,1):
            Lista[I]=int(input("Ingrese calificación: "))
        for I in range(TL,0,-1):
            print("Las calificaciopnes serian:{}".format(Lista[I]))
    def positivosyNegativos(self):
        x=1
        a=0
        b=0
        c=0
        while x <= 20:
            nu=int(input("Ingrese el numero: "))
            if nu==0:
                a= a+1
            else:
                if nu < 0:
                    b= b+1
                else:
                    c= c+1

            x+= 1
        print("Los numeros positivos son:{}".format(c))
        print("Los numeros negativos son:{}".format(b))
        print("Los numeros neutros son:{}".format(a))





numer1= Deber()
numer1.numeros()
op1= Deber()
op1.operaciones()
cen1=Deber()
cen1.centinela()
prim1= Deber()
prim1.primo()
facto1= Deber()
facto1.Factorial()
vec1=Deber()
vec1.vectorC()