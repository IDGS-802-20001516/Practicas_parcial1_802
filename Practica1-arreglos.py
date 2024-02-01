import os 

class trabajo1:
    nums = []
    
    def _init_(self):
        self.nums = []

    def arreglo(self):
        
        for i in range(10):
            num = int(input("Ingrese un numero: "))
            self.nums.append(num)

def main():
    obj = trabajo1()
    obj.arreglo()
    obj.nums.sort()
    imnumpares = list(set(num for num in obj.nums if num % 2 == 0))
    imnumimpares = list(set(num for num in obj.nums if num % 2 != 0))
    
    print("Arreglo Ordenado de Menor a Mayor2:", obj.nums)
    print("Arreglo de numeros pares:", imnumpares)
    print("Arreglo de numeros impares:", imnumimpares)
   
    contador = {}
    for num in obj.nums:
        contador[num] = contador.get(num, 0) + 1
    
    for num, cont in contador.items():
        if cont > 1:
            print("{}: {} veces".format(num, cont))

if __name__ == "__main__": main()


