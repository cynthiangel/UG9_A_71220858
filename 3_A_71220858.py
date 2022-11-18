#3.A. test case 1
import math
p = int(input("Masukkan panjang : "))
l = int(input("Masukkan lebar : "))
r = int(Input("Masukkan jari-jari : "))
luaslingkaran = float((math.pi)*(r**2))/2)
luaspp = float (p*l)
jumlahkaleng = float (((luaslingkaran+luaspp)/15))
print ("Area tersebut membutuhkan",math.ceil(jumlahkaleng),"kaleng cat")
