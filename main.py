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

class Stadium:
  def __init__(self, name, opening, country, city, capacity):
      self.name=name
      self.opening=opening
      self.country=country
      self.city=city
      self.capacity=capacity




stadion1=Stadium("Tipos",2015,"SR","Bratislava",15000)
stadion2=Stadium("Steal arena", 2010,"SR","Kosice",10000)
stadion3=Stadium("Lombardi",2000,"IT","Bologna",5000)

stadions=[stadion1,stadion2,stadion3]

zoradenie=sorted(stadions, key=lambda x: x.capacity)


for stadium in zoradenie:
  print(f"{stadium.name} - Capacity: {stadium.capacity}")

# najvacsia_kapacita=0
# najvacsi_stadion=None
# for i in stadions:
#     if i.capacity>najvacsia_kapacita:
#         najvacsia_kapacita = i.capacity
#         najvacsi_stadion = i
#
# print(najvacsi_stadion.name)

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price is negative")

kniha = Book("Harry Potter", 400, 10)
print(kniha.price)
kniha.price = 20
print(kniha.price)

