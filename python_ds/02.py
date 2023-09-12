
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n



class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # def __add__(self, otherFraction):
    #     newNum = self.num * otherFraction.den + self.den * otherFraction.num
    #     newDen = self.den * otherFraction.den
    #     return Fraction(newNum,newDen)

    def __add__(self, otherFraction):
        newNum = self.num * otherFraction.den + self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum,newDen)
        return Fraction(newNum//common,newDen//common)

    def __eq__(self, other):
        firtNum = self.num * other.den
        secondNum = other.num * self.den
        return firtNum == secondNum

# myFraction = Fraction(3,5)
# print(myFraction)
# print(myFraction.show())
# print("I ate ", myFraction, "of the pizza")
# print(myFraction.__str__())
# print(gcd(35, 25))

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1 + f2
print(f3)

