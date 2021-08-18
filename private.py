class C1:
    def meth1(self): self.__X = 88 # __XはC1固有のもの
    def meht2(self): print(self.X) # __XはIでは_C1__Xとなる

class C2:
    def metha(self): self.__X = 99 # __XはC2固有のもの
    def methb(self): print(self.__X) # __XはIでは_C2__Xとなる

class C3(C1, C2): pass

I = C3()

I.meth1(); I.metha()
print(I.__dict__)
I.meth2(); I_methb()
