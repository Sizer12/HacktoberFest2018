# Her Türlü Ardışık Dizinin Terimleri Toplamını Veren Program

a = input("İlk Terim:") #ilk terim gidisini alır
b = input("Son Terim:") # ikinci terim girdisini alır
c = input("Ardışık İki Terimin Farkı:") #kaçar kaçar atlayacağı girdisini alır

sonuç = (((int(a) + int(b)) * (int(b) - int(a) + int(c))) / (2 * int(c))) #sonucu hesaplar

print("Sonuç:", int(sonuç)) #sonucu yazdırır

# Her Türlü Ardışık Dizinin Terimleri Toplamını Veren Program

a = input("İlk Terim:")
b = input("Son Terim:")
c = input("Artış Miktarı:")

sonuç = (((int(b) + int(a)) * (int(b) - int(a) + int(c))) / (2 * int(c)))

print("Sonuç:", int(sonuç))
