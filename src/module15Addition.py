class Module15:
    def __init__(self,a,b,m):
        self.a = a
        self.b = b
        self.m = m
        pass
    def addition(self):
        for i in range(self.a):
            for j in range(self.b):
                x = i + j
                x =  (x%self.m)
                y1 = (i%self.m)
                y2 = (j%self.m)
                y = y1 + y2
                # if (x == y):
                print(x,end=" ")

            print("")

    def multiplication(self):
        for i in range(self.a):
            for j in range(self.b):
                x = i * j
                x =  (x%self.m)
                y1 = (i%self.m)
                y2 = (j%self.m)
                y = y1 * y2
                # if (x == y):
                print(x,end="  ")

            print("")

if __name__ == '__main__':
    module  = Module15(15,15,15)
    module.addition()
    print("")

    module1 = Module15(15, 15, 6)
    module1.addition()
    print("")
    module.multiplication()
    print("")
    module1.multiplication()
