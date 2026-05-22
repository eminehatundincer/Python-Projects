1. OOP Neden Gereklidir?
Nesne yönelimli programlama (OOP), gerçek dünyadaki varlıkları yazılım içinde nesne olarak modellemeyi sağlar. 
Bu yaklaşım:
Kodun tekrar kullanılabilirliğini artırır.
Daha düzenli ve anlaşılır bir yapı sunar.
Gerçek hayattaki ilişkileri (kitap–üye–işlem) doğrudan yansıtır.

2. Class ve Object Farkı
Class (sınıf): Bir varlığın şablonudur. Örneğin “Book” sınıfı, tüm kitapların ortak özelliklerini tanımlar.

Object (nesne): Sınıftan üretilen somut örnektir. Örneğin “Sefiller” kitabı, Book sınıfından türetilmiş bir nesnedir.

3. Inheritance Gerçek Hayatta Neyi Temsil Eder?
Inheritance (kalıtım), bir varlığın başka bir varlıktan özelliklerini miras almasıdır. 
Gerçek hayatta:
“Dijital Kitap” aslında bir “Kitap”tır, fakat ek özelliklere sahiptir (dosya boyutu, indirme işlemi).
Bu sayede ortak özellikler tekrar yazılmadan kullanılabilir, sadece farklılıklar eklenir.

4. Bu Projede Neden OOP Tercih Edildi?
Kütüphane sistemi; kitaplar, üyeler ve işlemlerden oluşan bir yapıdır. Bu varlıkların her biri ayrı sınıf olarak modellenmiştir.
OOP sayesinde:
Kitapların durumları (müsait/ödünçte) kolayca takip edilir.
Üyelerin işlemleri (ödünç alma, iade) mantıksal olarak sınıflara ayrılır.
Dijital kitaplar, klasik kitaplardan miras alarak ek özelliklerle genişletilir.