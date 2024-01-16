class MojaKalkulacka:
    @staticmethod
    def sucet(a,b):
        return a+b
    @staticmethod
    def sucin(a,b):
        return a*b

print(MojaKalkulacka.sucet(2,2))
print(MojaKalkulacka.sucin(2,3))

class Zviera:
    def hlas(self):
        raise NotImplementedError("Podtrida musi implementovat tuto metodu")

class Pes(Zviera):
    def hlas(self):
        return "haf"
    def koncatiny(self):
        return "4"

class Kohut(Zviera):
    def hlas(self):
        return "Kotkodak"
    def koncatiny(self):
        return "2"

class Macka(Zviera):
    def hlas(self):
        return "Mnau"
    def koncatiny(self):
        return "5"

def vydaj_zvuk(Zviera):
    return zviera.hlas()

def napis_koncatiny(Zviera):
    return zviera.koncatiny()

pes = Pes()
macka = Macka()
kohut = Kohut()

for zviera in [pes, macka, kohut]:
    print(vydaj_zvuk(zviera))
    print(napis_koncatiny(zviera))