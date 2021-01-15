# Pythonda da constructor mantığı vardır : __init__(self):

class Matematik:

    # self sözcüğü sınıfın referansına işaret etmektedir. Kullanmak gerekir.
    def __init__(self, sayi1, sayi2):
        print("Constructor çalıştı!")
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    # Yukarıdaki __init__ altındaki self.sayi1 ve self.2 ifadeleri
    # C# veya Java' da globaldeki elemanı constructor yardımı ile değiştirmek gibidir.
    # Normalde private olan ve sınıf içinde olan değişkene, constructor yardımı ile ulaşmaktır kısaca.
    # Aşağıda örnek :

    # class Math:
    # sayiX=0
    # sayiY=0
    # def __init__(sef,sayi1,sayi2):
    # self.sayiX = sayi1
    # self.sayiY = sayi2

    def topla(self):
        return self.sayi1 + self.sayi2

    def cikar(self):
        return self.sayi1 - self.sayi2

    def carp(self):
        return self.sayi1 * self.sayi2

    def bol(self):
        # sınıf içindeki fonksiyonlarda, sınıfın başka fonksiyonunu çağırmak için :
        # self.topla()
        return self.sayi1 / self.sayi2


mat1 = Matematik(2, 3)
print(mat1.topla())


# Property
class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age


p1 = Person("Arif", "Eker", 23)

print("Adınız : ", p1.firstName,
      "\nSoyadınız : ", p1.lastName,
      "\nYaşınız : ", p1.age)


# Aşağıdaki kullanım hata veriyor. Çünkü örneği -nesneyi- oluştururken değerleri vermem gerek.
# Hata vermemesi için yorum satırına alıyorum.

# p2 = Person()
# p2.firstName = "Kasım"
# p2.lastName = "Kayacık"
# p2.age = 20


# Inheritance

class Worker(Person):
    def __init__(self, salary):
        self.salary = salary


class Customer(Person):
    def __init__(self, creditCardNumber):
        self.creditCardNumber = creditCardNumber


Ahmet = Worker(5000)
Ahmet.firstName = "Ahmet"
Ahmet.lastName="Pursak"
Ahmet.age = 37

print("Adınız : ", Ahmet.firstName,
      "\nSoyadınız : ", Ahmet.lastName,
      "\nYaşınız : ", Ahmet.age,
      "\nMaaşınız : ", Ahmet.salary)

Mehmet = Customer("2334283284")
Mehmet.firstName = "Mehmet"
Mehmet.lastName = "Megabit"
Mehmet.age = 43

print("Adınız : ", Mehmet.firstName,
      "\nSoyadınız : ", Mehmet.lastName,
      "\nYaşınız : ", Mehmet.age,
      "\nKredi Kart Numaranız : ", Mehmet.creditCardNumber)
