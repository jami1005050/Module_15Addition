import math


class EuclidGCD:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def gcd(self,a,b):
        if(b == 0):
            return  a
        else:
            return self.gcd(b,a %b)

    def interative_gcd(self,a,b):
        while not b == 0:
            gc = a%b
            a = b
            b = gc

        return a

    def gcdExtended(self,a, b):
        if (b == 0):
            return (a,1,0)
        else:
            d_,x_,y_ = self.gcdExtended(b,a%b)
            d,x,y = d_,y_,x_ - math.floor(a/b) * y_
            return d,x,y


if __name__ =='__main__':
    euclidGCD = EuclidGCD(16,2)
    gcd = euclidGCD.gcd(16,2)
    igcd = euclidGCD.interative_gcd(16,2)
    print("euclidGCD:",gcd," interative: ",igcd)
    var = euclidGCD.gcdExtended(99,78)
    print("var: ",var)