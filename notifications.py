#Hücre 1 – Proje Tanımı (Markdown)
# Projenin amacı:
## Farklı bildiri türlerini (Email, SMS, Push) tek bir arayüzden yönetmek.  
## Polymorphism sayesinde aynı `send()` metodunu çağırarak farklı çıktılar elde etmek.  
## Ayrıca özel metodlar (`__str__`, `__len__`), hata yönetimi (`try/except`) ve standart kütüphaneler (`datetime`, `random`) kullanılarak OOP’nin ileri özelliklerini göstermek.

# Polymorphism nedir, neden gereklidir?
## Polymorphism, aynı isimli metodların farklı sınıflarda farklı davranış göstermesidir.  
## Bu sayede tek bir kod parçası ile farklı nesneler üzerinde işlem yapılabilir.  
## Örneğin `send()` metodu EmailNotification’da e‑posta gönderirken, SMSNotification’da SMS gönderir. Kod tekrarını azaltır ve esnekliği artırır.

# Kullanılan Python konuları:
## - Class ve inheritance (temel sınıf + alt sınıflar)  
## - Polymorphism (aynı metod, farklı davranış) 
## - Özel metodlar: `__str__`, `__len__`
## - Hata yönetimi: `try/except`
## - Standart kütüphaneler: `datetime`, `random`
## - Modüler yapı: ayrı `.py` dosyaları (notifications.py, utils.py, main.py)


# Hücre 2 – Modülleri Import Et
from notifications import EmailNotification, SMSNotification, PushNotification
from utils import generate_message

# Hücre 3 – Bildirimleri Oluştur
notif1 = EmailNotification(generate_message())
notif2 = SMSNotification(generate_message())
notif3 = PushNotification(generate_message())

notifications = [notif1, notif2, notif3]
#farklı türlerdeki bildirimleri tek bir liste içinde tutuyoruz

# Hücre 4 – Polymorphic Gönderim
for n in notifications:
    n.send()

# Hücre 5 – Özel Metod Kullanımı   
print(notif1)          # __str__ çalışır
print(len(notif1))     # __len__ çalışır

# Hücre 6 – Hata Yönetimi
try:
    bad_notif = EmailNotification("")  # Boş mesaj
    if not bad_notif.message:
        raise ValueError("Mesaj boş olamaz!")
    bad_notif.send()
except ValueError as e:
    print("Hata:", e)
