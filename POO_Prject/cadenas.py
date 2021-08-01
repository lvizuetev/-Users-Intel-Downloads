print("Ingrese La Opcion que desea Realizar")
print("1.Recorrer y presentar datos de una Cadena\n2.Buscar caracter en una cadena\n3.Retornar lista con las pociones dadas de un caracter \n4.Retornar lista con todas las")
print("5. Retornar una cadena a partir de una lista.\n6.insertar dato en una cadenada dada la Posocion")
print("7.Eliminar todas las ocurrencuas de una cadena\n8.Retornar cualquier valor de una cadena eliminandolo\n9.Contanar cadena\n10.Salir")
#Punto1
def recorrerCadena(cadena):
            len(cadena)
            print("La cadena es:"+ cadena+" y cuenta con: " +  str(len(cadena)) + " Caracteres")
            for i, c in enumerate(cadena):
                print('Caracter: %s' % (c))
#Punto2
def BuscarCaracter(cadena1,buscador):
    acu = 0
    for i in range (len(cadena1)):
        if (cadena1[i]== buscador):
            acu+=1 
            print("Existe :" + str(acu))
            print("En el caracter: "+ str(i))
        else:
            print("No hay Coincidencia")
#Punto3
def listaPosiciones(caracter,cadena3):
    for i, c in enumerate(cadena3):
            print('Caracter: %s - Puesto: %i' % (c,i))
            if (cadena3[i]== caracter):
                print('El Caracter : %s - Se encuentra en el Puesto: %i' % (c,i))
##Punto4
def listaPalabras():
    frase=input("Ingrese la Oracion\n")
    Palabras = frase.split()
    print(Palabras)
    print(len(Palabras))
##Punto5
def ListaPalabras(Palabras):
    Lista=[]
    ##Palabras=str(input("Ingrese una palabra, al finaizar use el punto\n"))
    while Palabras!=".":
        Lista.append(Palabras)
        Palabras=str(input("Ingrese una palabra, al finaizar use el punto\n"))
    print("La Lista seria\n"+ str(Lista))
    Cad=" ".join(Lista)
    print("La Cadena seria\n"+ str(Cad))
##Punto6
def insertardatos(Palabras1):
    Lista=[]
    while Palabras1!=".":
        Lista.append(Palabras1)
        Palabras1=str(input("Ingrese una palabra, al finaizar use el punto\n"))
    print("La Lista seria\n"+ str(Lista))
    buscado1=str(input("Ingrese lo que desea agregar a la lista\n"))
    Posicion1=int(input("Ingrese en que posicion desea agregar el anadido\n"))
    Lista.insert(Posicion1, str(buscado1))
    print("La Lista ahora es\n"+ str(Lista))
##Punto7
import re
def eliminarOcurrencia(buscado):
    import re
    Lista1=[]
    while buscado!=".":
        Lista1.append(buscado)
        buscado=str(input("Ingrese una palabra, al finaizar use el punto\n"))
    print("La Lista seria\n"+ str(Lista1))
    buscado1=str(input("Ingrese la concurrencia que desea eliminar de la lista\n"))
    oncurrencia=len(re.findall(str(buscado1), str(Lista1)))
    print('La Concurrencia de su caracter es:',oncurrencia)
    Cad1=" ".join(Lista1)
    print("La Cadena seria\n"+ str(Cad1))
    Cad1 = ''.join( x for x in Cad1 if x not in buscado1)
    print("La Cadena quedaria como\n" + str(Cad1))
#Punto9
def concatenarCadena(dato):
    Lista4=[]
    while dato!=".":
        Lista4.append(dato)
        dato=str(input("Ingrese una palabra, al finaizar use el punto\n"))
    ##print("La Lista seria\n"+ str(Lista))
    Cad=" ".join(Lista4)
    print("La Cadena seria\n"+ str(Cad))
Ingreso=int(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))
while int(Ingreso==Ingreso):
    Ingreso=int(input("Si desea elegir aquella vuelva a ingresarla o cambie la Opcion dependiendo del Numero del Menu\n"))
    if Ingreso==1: 
        ##Bloque1
        recorrerCadena(cadena = input("Ingrese una palabra: " ))
        Ingreso1=str(input("Desea volver al menu Cadena(Y y N)\n"))
        if Ingreso1!= 'Y':
            print("Gracias Por ejecutar")
            break
        else:
            print("A selencionado seleccionar otra opcion")
        Ingreso=str(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))     
        ##
    elif Ingreso==2:
        ##Bloque2
        BuscarCaracter(cadena1=input("Ingrese la cadena"), buscador=input("cracter a buscar"))
        Ingreso1=str(input("Desea volver al menu Cadena(Y y N)\n"))
        if Ingreso1!= 'Y':
            print("Gracias Por ejecutar")
            break
        else:
            print("A selencionado seleccionar otra opcion")
        Ingreso=str(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))
        ## 
    elif Ingreso==3:
        listaPosiciones(cadena3=input("Ingrese una cadena\n"), caracter=input("Ingrese el caracter a buscar\n"))
        Ingreso1=str(input("Desea volver al menu Cadena(Y y N)\n"))
        if Ingreso1!= 'Y':
            print("Gracias Por ejecutar")
            break
        else:
            print("A selencionado seleccionar otra opcion")
        Ingreso=str(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))
        ## 
    elif Ingreso==4:
        listaPalabras()
        Ingreso1=str(input("Desea volver al menu Cadena(Y y N)\n"))
        if Ingreso1!= 'Y':
            print("Gracias Por ejecutar")
            break
        else:
            print("A selencionado seleccionar otra opcion")
        Ingreso=str(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))
        ## 
    elif Ingreso==5:
        ListaPalabras(Palabras=input("Ingrese la serie de palabras y al final el punto (Ingresar el punto Solo)\n "))
        Ingreso1=str(input("Desea volver al menu Cadena(Y y N)\n"))
        if Ingreso1!= 'Y':
            print("Gracias Por ejecutar")
            break
        else:
            print("A selencionado seleccionar otra opcion")
        Ingreso=str(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))
        ## 
    elif Ingreso==6:
        insertardatos(Palabras1=input("Ingrese la serie de palabras y al final el punto (Ingresar el punto Solo)\n "))
        Ingreso1=str(input("Desea volver al menu Cadena(Y y N)\n"))
        if Ingreso1!= 'Y':
            print("Gracias Por ejecutar")
            break
        else:
            print("A selencionado seleccionar otra opcion")
        Ingreso=str(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))
        ## 
    elif Ingreso==7:
        eliminarOcurrencia(buscado=input("Ingrese una palabra, al finaizar use el punto\n"))
        Ingreso1=str(input("Desea volver al menu Cadena(Y y N)\n"))
        if Ingreso1!= 'Y':
            print("Gracias Por ejecutar")
            break
        else:
            print("A selencionado seleccionar otra opcion")
        Ingreso=str(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))
        ## 
    elif Ingreso==9:
        concatenarCadena(dato=input("Ingrese la oracion que desee y al final un punto(El punto solo)"))
        Ingreso1=str(input("Desea volver al menu Cadena(Y y N)\n"))
        if Ingreso1!= 'Y':
            print("Gracias Por ejecutar")
            break
        else:
            print("A selencionado seleccionar otra opcion")
        Ingreso=str(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))
        ## 
    elif Ingreso==10:
        break
    elif Ingreso>10:
        print("No valido")
        Ingreso=int(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))
    
    
       
    

    

        
##print("Ingreso una opcion incorrecta por favor ingrese la Opcion dependiendo del Numero del Menu\n")
##Ingreso=int(input("Ingrese la Opcion dependiendo del Numero del Menu\n"))



