#Linda Vizuete
class ciclos:
    def __init__(self, num1=5):
        self. numero=num1
    def usowhile(self):
        #ciclo repetitivo que se ejecuta por verdadero y sale por falso
        carac = input("Ingrese vocal: ")
        carac= carac.lower()
        while carac not in ('a','e','i','o','u'):
            carac=input("Ingrese el caracter:{} es una vocal".format(carac))
        print("Felicitaciones el caracter:{} es una vocal".format(carac))
ciclo1= ciclos()
ciclo1.usowhile()