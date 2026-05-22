orders = [
    {
"customer":"Ahmet",
"items": ["Laptop","Mouse","Mouse"],
"total":18500,
"is_paid":True
    },
    {
"customer":"Zeynep",
"items": ["Keyboard"],
"total":2500,
"is_paid":False
    },
    {
"customer":"Mehmet",
"items": ["Monitor","HDMI Cable","Monitor"],
"total":7200,
"is_paid":True
    },
    {
"customer":"Mehmet",
"items": ["Monitor","HDMI Cable","Monitor"],
"total":7200,
"is_paid":True
    }
 ]

#1. Sipariş Sayısı Analizi:
#Toplam sipariş sayısı
toplam_siparis= len(orders)
print("Toplam Sipariş Sayısı:", toplam_siparis)

#Ödenmiş,ödenmemiş sipariş sayısı
odenmis_siparis= 0
odenmemis_siparis=0

if orders[0]["is_paid"]==True:
    odenmis_siparis+=1
else:
    odenmemis_siparis+=1

if orders[1]["is_paid"]==True:
    odenmis_siparis+=1
else:
    odenmemis_siparis+=1
    
if orders[2]["is_paid"]==True:
    odenmis_siparis+=1
else:
    odenmemis_siparis+=1
    
if orders[3]["is_paid"]==True:
    odenmis_siparis+=1
else:
    odenmemis_siparis+=1
    
#2.Müşteri Listesi
#İsimleri listele
musteri_listesi = [orders[0]["customer"], orders[1]["customer"],orders[2]["customer"],orders[3]["customer"]]
print("Müşteri Listesi:", musteri_listesi)
#Tekrar eden verileri sil
musteri_listesi = set(musteri_listesi)
print("Tekrarsız Müşteri Listesi:", musteri_listesi)

#3.Ürün Analizi
#Satılan ürünlerin listesini oluştur
tüm_ürünler = orders[0]["items"] + orders[1]["items"] + orders[2]["items"] + orders[3]["items"]
print("Satılan Ürünler:", tüm_ürünler)
#Aynı ürünlerin tekrar ettiğini göster
tekrar_eden_ürünler = set([item for item in tüm_ürünler if tüm_ürünler.count(item) > 1])
print("Tekrar Eden Ürünler:", tekrar_eden_ürünler)
#unique ürünleri ayırma 
unique_ürünler = set(tüm_ürünler)
print("Unique Ürünler:", unique_ürünler)

#4.Sipariş Durum Kontrolü
if orders[0]["is_paid"]:
    print("Sipariş onaylandı")
else:
    print("Ödeme bekleniyor")

if orders[1]["is_paid"]:
    print("Sipariş onaylandı")
else:
    print("Ödeme bekleniyor")

if orders[2]["is_paid"]:
    print("Sipariş onaylandı")
else:
    print("Ödeme bekleniyor")

if orders[3]["is_paid"]:
    print("Sipariş onaylandı")
else:
    print("Ödeme bekleniyor")

#Güvenli Sipariş Özeti
# Tuple neden değiştirilemez?
# Cevap: Tuple'lar immutable yapılardır. 
# Bu özellik, verilerin program akışı sırasında kazara değiştirilmesini önler, 
# veri bütünlüğünü korur ve listelere göre bellekte daha az yer kaplayarak daha hızlı çalışır.
müsteri1 = (orders[0]["customer"], orders[0]["total"])
müsteri2 = (orders[1]["customer"], orders[1]["total"])
müsteri3 = (orders[2]["customer"], orders[2]["total"])
müsteri4 = (orders[3]["customer"], orders[3]["total"])

tüm_müsteriler= [müsteri1, müsteri2, müsteri3, müsteri4]
print("Sipariş Özetleri:", tüm_müsteriler)

#Genel Çıktılar
print("Toplam Sipariş Sayısı:", toplam_siparis)
print("Ödenmiş Sipariş Sayısı:", odenmis_siparis)
print("Ödenmemiş Sipariş Sayısı:", odenmemis_siparis)
print("Unique Ürünler:", unique_ürünler)

