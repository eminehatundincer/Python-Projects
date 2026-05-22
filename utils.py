1. Polymorphism Nedir, Inheritance’tan Farkı:
Polymorphism, aynı isimli metodların farklı sınıflarda farklı davranış göstermesidir. Örneğin send() metodu EmailNotification’da e‑posta gönderirken, SMSNotification’da SMS gönderir. Bu sayede tek bir arayüz üzerinden farklı türde nesneler yönetilebilir.
Inheritance (kalıtım) ise bir sınıfın başka bir sınıftan özelliklerini miras almasıdır. Kalıtım “özellikleri devralma”yı sağlarken, polymorphism bu ortak metodların farklı şekilde uygulanmasını mümkün kılar.
2. Özel Metodlar Neden Kullanılır?
Python’daki __str__ ve __len__ gibi özel metodlar, nesnelerin daha doğal ve okunabilir şekilde kullanılmasını sağlar.

__str__: Nesneyi yazdırdığımızda anlamlı bir çıktı verir (örneğin bildirim mesajı + zaman damgası).

__len__: Nesnenin uzunluğunu tanımlar (örneğin mesajın karakter sayısı).
Bu metodlar sayesinde nesneler Python’un yerleşik fonksiyonlarıyla uyumlu hale gelir ve kullanıcıya sezgisel bir deneyim sunar.
3. Modüler Kodun Avantajları:
1-Kodun farklı dosyalara (notifications.py, utils.py, main.py) bölünmesi,
2-Okunabilirliği artırır,
3-Bakımı ve geliştirmeyi kolaylaştırır,
4-Tekrar kullanılabilirliği sağlar,
5-Takım çalışmasında iş bölümü yapılmasına olanak tanır,
Bu yapı sayesinde sistem büyüdükçe karmaşıklık azalır ve her dosya kendi sorumluluğunu taşır.
4. Hata Yönetimi Olmayan Bir Sistemde Ne Olur?
Eğer hata yönetimi (try/except) uygulanmazsa:
Boş mesaj gibi geçersiz veriler sisteme girildiğinde program çöker.
Kullanıcıya anlaşılmaz hata mesajları gösterilir.
Sistem güvenilirliğini kaybeder ve kullanıcı deneyimi olumsuz etkilenir.
Hata yönetimi sayesinde bu durumlar önlenir, kullanıcıya anlamlı uyarılar verilir ve sistem çalışmaya devam eder.