1-Fonksiyon kullanmanın avantajları:
Kodu fonksiyonlara bölmek tekrarı ortadan kaldırır ve her birimi bağımsız test etmeyi mümkün kılar.
•	Yeniden kullanılabilirlik: aynı mantık farklı noktalardan çağrılır
•	Okunabilirlik: main() fonksiyonu programın akışını belge gibi anlatır
•	Bakım kolaylığı: bir değişiklik tek noktada yapılır, tüm sisteme yayılır
2-*args Neden Gereklidir?
Kullanıcının kaç harcama gireceği önceden bilinemez. Sabit parametre sayısı bu belirsizliği karşılayamaz.
•	*args gelen tüm değerleri tuple olarak toplar, fonksiyon her sayıda argümanı kabul eder
•	flexible_total(*expenses) çağrısı listeyi otomatik olarak parçalara ayırarak iletir
3- Scope Hataları Neden Sık Yapılır?
Python bir fonksiyon içinde atama gördüğünde otomatik olarak local değişken oluşturur — sözdizimi hatası vermez, yanlış sonuç üretir.
•	LEGB kuralı: Local → Enclosing → Global → Built-in sırasıyla aranır
•	change_currency() içindeki currency = 'USD' global'i değiştirmez; yeni local yaratır
•	Çözüm: global anahtar kelimesi ya da return ile değer döndürmek
4- try/except Gerçek Sistemlerde Neden Kritiktir?
Kullanıcı girdisi her zaman güvenilmezdir. Korunmasız bir input() çağrısı tüm programı çökertebilir.
•	İç içe katman: dış try harcama sayısını, iç try her miktarı ayrı korur
•	Hatalı giriş atlanır, program kalan verilerle çalışmaya devam eder
•	bare except: yerine except ValueError: yazılmalı — aksi halde tüm hatalar yakalanır
Bu dört ilke birbirini tamamlar: fonksiyonlar yapıyı, *args esnekliği, scope güvenli değişken yönetimini, try/except ise dayanıklılığı sağlar.


