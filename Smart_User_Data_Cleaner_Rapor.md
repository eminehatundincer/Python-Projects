1.GİRİŞ:
Projenin Amacı: Bu projede, kullanıcıdan gelen ham, hatalı ve tutarsız metin verilerini Python programlama dilinin string işleme araçlarıyla temizlemeye, parçalamaya ve anlamlı çıktılara dönüştürmeyi amaçlamaktadır.
Proje kapsamında aşağıdaki tek ham veri satırı işlenmektedir:
raw_data = "  AhMeT  yILMAZ ;  23 ;  1.78 ;  ahmetYILMAZ@GMAIL.Com   "
Bu veri; isim, yaş, boy ve e-posta bilgilerini noktalı virgülle ayrılmış şekilde, ancak büyük-küçük harf karışıklığı, fazla boşluklar ve tutarsız formatlarla içermektedir.

Veri Temizlemenin Önemi:
Gerçek dünya uygulamalarında veriler nadiren temiz ve düzenli gelir. Kullanıcıların formlara girdiği bilgiler sıklıkla şu sorunları barındırır:
•	Büyük-küçük harf tutarsızlıkları (örn. 'AhMeT')
•	Baş ve son boşluklar
•	Sayısal değerlerin metin olarak saklanması
•	E-posta adreslerinde büyük harf kullanımı
Bu tür veriler doğrudan kullanıldığında veritabanı hataları, eşleştirme sorunları ve yanlış analizlere yol açabilir. Veri temizleme, yazılım geliştirme sürecinin vazgeçilmez bir adımıdır.

String İşlemlerinin Veri Ön İşlemedeki Rolü:
Python'un string metodları, ham veriyi işlenebilir hale getirmede temel araçlardır. Veritabanına kaydetmeden, CSV oluşturmadan veya kullanıcıya göstermeden önce verinin normalleştirilmesi gerekir. Bu normalizasyon süreci büyük ölçüde string manipülasyonuna dayanır.

2.Kullanılan Python Konuları:
Bu projede değişkenler, string veri tipi, string metodları, slicing ve tip dönüşümleri kullanılmıştır.

Temel string metodları:
strip() / lstrip() / rstrip():Metinin başındaki/sonundaki boşlukları siler.
lower() + title(): title her kelimenin ilk harfini büyük diğerlerini küçük yapar, lower ise tüm harfleri küçük yapar.
split(): Metni girilen veriye göre böler.
find() + slicing: Girilen değerlere göre konum bulur ve metnin o konuma kadar olan parçasını alır. 
int() / float(): Tip dönüşümü yapılır. 

3.Veri Temizleme Süreci:
Ham verideki problemler ve çözümleri adım adım uygulanmıştır:
•	Genel temizlik: strip() + split(';') ile veri 4 parçaya ayrıldı.
•	İsim düzeltme: [0:20].strip().lower().title() → "Ahmet Yilmaz"
•	Yaş işleme: int() ile tam sayıya çevrildi , float(yas+10) ile ondalıklı sayıya çevrilip 10 yıl sonrası hesaplandı.
•	Boy analizi: float() ile metre değeri alında ve cm'ye (×100) kullanılarak çevrildi.
•	Email: strip().lower() + find('@') + slicing ile kullanıcı kodu alındı.

4.Sonuç:
Bu proje; harf tutarsızlıkları, fazla boşluklar ve tip uyumsuzlukları gibi gerçek veri sorunlarını yalnızca string metodları ve slicing kullanarak çözmüştür. Kazanılan temel beceriler: string metodlarının zincirleme kullanımı, slicing ile hassas veri kesme ve tip dönüşümü teknikleridir. Bu teknikler form verisi temizleme, CSV ön işleme ve kullanıcı kayıt sistemlerinde doğrudan uygulanabilir.








