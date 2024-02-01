def __init__(self,a):
    self.num=a

def piramide(self):
    self.r=self.num
    piramide=int(input("Tamaño de la piramide:"))

    i=1
    c="*"
    for piramide in range (1,self.r+1,1):
        while i<=self.r:
         print(c*i)
         i+=1

def main():
    obj = piramide()
    obj.piramide()

if __name__ == "__main__": main()