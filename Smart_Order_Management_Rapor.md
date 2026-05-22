1. Giriş: Koleksiyonların Gerçek Hayattaki Karşılığı:
Dijital dünyada ham veri, işlenmediği sürece bir anlam ifade etmez. E-ticaret gibi dinamik sistemlerde veriler durağan değildir; sürekli güncellenir, filtrelenir ve gruplanır. Python koleksiyonları,gerçek hayattaki bir depo yönetim sistemine benzer.Ürünlerin raflara dizilmesi (List), her ürüne özel bir barkod atanması (Dict) veya bazı verilerin mühürlenerek değiştirilemez hale getirilmesi (Tuple) bu yapıların somut karşılıklarıdır.

2. Veri Yapıları Arasındaki Temel Farklar:
List: Sıralı ve değiştirilebilirdir. Projedeki kullanımı siparişlerin ve ürünlerin kronolojik takibini yapmak.
Set: Sırasız ve benzersizdir. Projedeki kullanımı müşteri portföyü ve ürün çeşitliliği analizi yapmaktır.
Tuple: Sıralı fakat değiştirilemezdir. Projedeki rolü bazı verilerin sabitlenmesi ve korunmasıdır.

3. Sistem Mantığında Bool ve If Kontrolleri:
Bir sistemin akıllı olarak nitelendirilmesi, karar verme yeteneğine bağlıdır. Bool veri tipi (True/False), sistemin mantıksal anahtarıdır.
Süreç Yönetimi: is_paid değişkeni bir bayrak (flag) görevi görür.
Hata Payı: Eğer if/else kontrolü olmasaydı, ödemesi yapılmamış bir siparişin lojistik sürecine girmesi engellenemezdi. Bu kontroller, işletme mantığının kod seviyesindeki koruma kalkanlarıdır.

4. Veri Yapısı Seçim Nedenleri:
Bu projede belirli yapıların seçilme nedenleri stratejiktir:
Neden Dictionary? Sipariş verilerinde her bir özelliği (müşteri, ürünler, tutar) isimlendirilmiş anahtarlarla (key) tutmak, veriye erişim hızını ve okunabilirliği artırır.
Neden Set? Analiz aşamasında "Kaç farklı müşterimiz var?" sorusuna en hızlı cevabı set verir; çünkü algoritması gereği tekrar eden elemanları otomatik olarak eler.
Neden Tuple? Sipariş özeti oluşturulurken (müşteri_adı, toplam_tutar) yapısı tercih edilmiştir. Tuple değiştirilemezdir; bu sayede rapor oluşturulduktan sonra bir program hatasıyla müşterinin borcunun veya adının değişmesi teknik olarak imkansız hale getirilir bu da veri Bütünlüğü sağlar.

5. Sonuç:Bu proje verinin sistem içindeki güvenli yolculuğunu temsil eder. Doğru veri yapısı seçimi, sistemin bellekte daha az yer kaplamasını ve daha hızlı çalışmasını sağlarken; mantıksal kontroller ise operasyonel hataları minimize eder.