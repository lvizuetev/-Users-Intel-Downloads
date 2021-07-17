class operaciones 
    def  _init_(self,num1,num2): 
        self.numero1=num1
        self.numero2=num2

    def suma(self):
        suma = self.num1 + self.num2
        return suma 

    def resta(self):
        if self.numero1 >= self.numero2:
            return self.num1 - self.num2
        return 0
    
    def multiplicacion(self):
        return self.num1 * self.num2

    def divison(self):
        if self.muero2 != 0  return self.num1 / self.num2
        return 0

    def divisonEntera(self):
        if self.muero2 != 0  return self.num1 // self.num2
        return 0

    def Reciduo(self):
        return self.num1 % self.num2

    def exponente(self):
        return self.num1 ** self.num2
 
    def mostrar(self):
        print("Operando1={},Operando2={}".format(self.numero1,self.numero2))

print ("Menu Operaciones Matematicas")
print ("1) Suma\n2) Resta\n3) Multplicacion\n4) Division\n5) Division Entera\n6) Residuo\n7) Exponente")
