1:For vs While ne zaman kullanılır?
For: Bir koleksiyonun (liste, dizi, metin) başı ve sonu bellidir. "Şu listenin içindeki her elemana bak" dediğinizde for kullanırsınız. Sayaç otomatik ilerler.
While: Bir belirsizlik hakimdir. "İnternet bağlantısı gelene kadar bekle" veya "Kullanıcı doğru şifreyi girene kadar sormaya devam et" gibi durumlarda kullanılır.Koşul bozulana kadar döner.

2:Break ve Continue gerçek hayatta neyi temsil eder?
Break: Döngüyü tamamen kırar ve dışarı çıkar. Gerçek hayat örneği: Bir yangın alarmı çaldığında binadaki işinizi (döngüyü) yarım bırakıp binayı terk etmenizdir.
Continue: Sadece o anki turu iptal eder, bir sonraki tura geçer. Gerçek hayat örneği: Bir kutu meyveyi ayıklarken çürük bir elmaya denk gelip onu kenara atmanız ve kutudaki diğer elmaları kontrol etmeye devam etmenizdir.

3:Random veri üretmenin test sürecindeki rolü?
Kullanıcılar genelde "mutlu senaryolar" (her şeyin doğru girildiği durumlar) üzerinden kod yazar. Ancak gerçek hayatta kullanıcılar saçma veriler girebilir.
Fuzz Testing: Sisteme rastgele, devasa veya hatalı veriler göndererek sistemin çöküp çökmediğini kontrol ederiz.
Çeşitlilik: Binlerce farklı profil senaryosunu saniyeler içinde oluşturup sistemin yük kaldırma kapasitesini ölçeriz.

4:Döngülerin veri analizindeki önemi?
Veri analizi büyük veri yığınlarıyla uğraşır.
Toplu İşlem: 1 milyon müşterinin harcama verisi olduğunu düşünün. Döngü olmazsa her satır için ayrı kod yazmanız gerekir. Döngü ile tek bir komutla tüm satırları tarayıp toplam ciroyu veya en çok satan ürünü bulabilirsiniz.
Filtreleme: Sadece belirli şartlara uyan verileri örneğin: 18 yaş altı kullanıcılar ayıklamak için döngülerle tüm listeyi hızlıca süzersiniz.
