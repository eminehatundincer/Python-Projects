#Projenin Amacı:
#Gerçek hayattaki kütüphane sistemini nesne yönelimli programlama ile modellemek.
#Neden OOP?
#Gerçek dünyadaki varlıkları (kitap,üye,işlem) nesne olarak düşünebilmek
#Kodun tekrar kullanılabilirliğini artırmak
#Daha düzenli ve anlaşılır bir yapı kurmak
#Kullanılan OOP Kavramları:
#Class tanımı, Arttribute(özellikler), Method(davranışlar), Default değerler, Inheritance(kalıtım)

#Book Sınıfı
class Book:
    def __init__(self,title,author,year,is_available=True):
        self.title=title
        self.author=author
        self.year=year
        self.is_available= is_available #default True

    def get_info(self):
        print(f"{self.title} - {self.author} ({self.year}) | Müsait:  {self.is_available}")
    
    #Member Sınıfı
class Member:
        def __init__(self,name,member_id):
            self.name= name
            self.member_id = member_id

        def borrow_book(self,book):
            if book.is_available:
                book.is_available = False
                print(f"{self.name} kitabını ödünç aldı.")
            else:
                print("Kitap şu anda müsait değil.")
        def return_book(self, book):
            book.is_available= True
            print("Kitap iade edildi.")
        
        #Default Değer Kullanımı
        #Yeni kitap oluştururken is_available otomatik True gelir
        book1 = Book("Sefiller", "Victor Hugo", 1862)
        book1.get_info()

        #İnheritance(Kalıtım)
class DigitalBook(Book): #Book sınıfından miras alıyor
            def __init__(self,title,author,year,file_size,is_available=True):
                super().__init__(title,author,year,is_available) #Book sınıfının init metodunu çağırır
                self.file_size=file_size
            def download(self):
                print("Dosya indiriliyor...")
        
        #Sistem Testi
book1= Book("Sefiller", "Victor Hugo", 1862)
book2 = Book("Suç ve Ceza", "Fyodor Dostoyevski", 1866)

ebook = DigitalBook("Python 101", "Michael Driscoll", 2014, 5)

member1 = Member("Ahmet", 101)

        #Testler 
member1.borrow_book(book1) #Ahmet kitabı ödünç aldı
member1.borrow_book(book1) #Kitap zaten ödünç alındığı için müsait değil   
member1.return_book(book1) #Kitap iade edildi
ebook.download() #Dosya indiriliyor... 