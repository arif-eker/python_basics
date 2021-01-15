# Dosya İşlemleri

# default parametre "r" dir. fakatbu kod hata verecek. dosya yok ya da yol hatası
f_r = open("musteriler.txt", "r")

# dosya oluşturmak için :
f_w = open("Dosyalarla_Calismak/musteriler.txt", "w")

# var oolan dosyaya ekleme yapmak için :
f_a = open("Dosyalarla_Calismak/musteriler", "a")

# dosya yoksa dosya oluşturmak varsa oluşturmamak için :
f_x = open("Dosyalarla_Calismak/musteriler", "x")

# r = Read
# w = Write
# a = Append
# x = Create


f = open("Dosyalarla_Calismak/musteriler.txt")
f.read()

# ilk 3 karakteri okumak için :
f = open("Dosyalarla_Calismak/musteriler.txt")
f.read(3)
# yukarıdaki hali ile tekrar 3 karakter okutmak istersem, sonraki 3 karakteri gösterecektir. baştan göstermeyecektir.

# satır satır okumak için :
f_line = open("Dosyalarla_Calismak/musteriler.txt")
f_line.readline()

for line in f_line:
    print(line)

# İşlemler bittikten sonra dosyayı kapatmak gerekir.
f_line.close()

# Dosyaya ekleme yapalım:
f_add = open("Dosyalarla_Calismak/musteriler.txt", "a")
f_add.writelines("Arif Eker")
f_add.close()

# dosyayı silmek için
import os

os.remove("Dosyalarla_Calismak/musteriler.txt")

# bir dosya var mı yok mu?

if os.path.exists("Dosyalarla_Calismak/musteriler.txt"):
    print("Dosya var")
else:
    print("Dosya yok")

# klasörü tamamen silmek için :
os.rmdir("Dosyalarla_Calismak")
