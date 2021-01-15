# SQLite kullanımı

import sqlite3

# veritabanı ismini yanlıış verirsen, o isimle veritabani oluşturur. dikkat yani!
connection = sqlite3.connect("Veritabani/chinook.db")

# Eğer burada * ile tüm sütunları almasaydık, 2 değişken alsaydık, alttaki row[0] ve row[1] değişkenleri değişebilirdi.
# Hangi değişkenleri aldığımıza bağlı olarak örneğin ad-soyad yerine select company,age desek row değerleri değişir.
cursor = connection.execute("select * from customers")

i = 1
for row in cursor:
    if i == 2:
        break
    else:
        print("Name : {} Last Name : {}".format(row[1], row[2]))

    i += 1

# açılan her bağlantı kapatılmalı
connection.close()


# Insert komutu kullanımı
def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(
        """insert into customers (firstName,lastName,city,email) values ('Arif','Eker','Bursa','xyz@gmail.com')""")

    # veri tabanına yüklemek için commit denir.
    connection.commit()
    connection.close()

#
# Geri kalan işlemler için yine aynı SQL komutları kullanılır. Fark yoktur.
#
