class Mango:
    def _init_(self):
        print("this is what?")
    def balaji(self):
        print("this is without para")
    def shetty (self, a, b):
        print (a+b, "this is with para")
    def magicalprime(self, a):
        print( 'check it magical prime or not')
    def neon (self,a):
        square = a**2
        sum_of_digits = sum(int(digit) for digit in str(square))
        return sum_of_digits == a
    
        print ('check neon or not')
man=Mango()
man.balaji()
man. shetty (10,20.5)
man.magicalprime (101)
man. neon (7)        

