#Proje Tanımı:
#Projenin Amacı — Kullanıcının günlük ya da aylık harcamalarını takip etmesine yardımcı olan, basit ama güvenli bir bütçe asistanı geliştirmek
#Gerçek Hayatta Ne İşe Yarar? — Market, fatura, ulaşım harcamalarını analiz eder; toplam/ortalama gösterir; tasarruf fırsatı sunar; yanlış girişlere karşı güvenlidir.
#Kullanılan Python Konuları — Tablo halinde 7 konu: Fonksiyonlar, Girdi/Çıktı, *args, Gömülü Fonksiyonlar, Kapsam, Hata Yakalama, Hesap Makinesi Mantığı.

#Harcama Alma Fonksiyonu:
from matplotlib.pylab import double


def get_expenses():
    expenses=[] #liste 
    try:
        expensesSayi = int(input("Harcama sayısını giriniz:"))
        for i in range(expensesSayi): 
            try:
                expense = float(input("Harcama milktarını giriniz:"))
                expenses.append(expense)
            except:
                print("Geçersiz sayı girildi.Lütfen geçerli bir sayı giriniz.")
    except: 
        print("Geçersiz sayı girildi.Lütfen geçerli bir sayı giriniz.")
    return expenses
    
#Toplam ve ortalama fonksiyonu:
def calculate_summary(expenses):
        toplam_harcama = sum(expenses)
        if len(expenses) == 0:
            ortalama_harcama = 0
        else:
            ortalama_harcama = toplam_harcama / len(expenses)
        print("Toplam Harcama:", round(toplam_harcama, 2)) #round ile 2 basamak gösterme
        print("Ortalama Harcama:", round(ortalama_harcama, 2))
        return round(toplam_harcama, 2), round(ortalama_harcama, 2)

#Args ile esnek hesaplama:
def flexible_total(*args):
        toplam= sum(args)
        gelen=len(args)
        print(f"Toplam Harcama :{toplam} TL")
        print("Gelen argüman sayısı :",gelen)

#En yüksek ve en düşük harcama:
def find_extremes(expenses):
        if len(expenses) == 0:
            print("Hiç harcama yok.")
            return
        max_expense = max(expenses)
        min_expense = min(expenses)
        print("En Yüksek Harcama:", round(max_expense, 2))
        print("En Düşük Harcama:", round(min_expense, 2))
        return round(max_expense, 2), round(min_expense, 2)

#Kapsam Gösterimi:
currency = "TL" #global degisken 

def show_currency():
    print("Para birimi:", currency)

def change_currency():
    currency = "USD"  #local degisken
    print("Fonksiyon içindeki para birimi:", currency)

show_currency()
change_currency()
show_currency()

# Fonksiyon içinde yapılan değişiklik global değişkeni etkilemiyor çünkü burada yeni local değişken oluşturulur.
def main():
    expenses = get_expenses() 

    toplam_harcama, ortalama_harcama = calculate_summary(expenses) 

    max_expense, min_expense = find_extremes(expenses)

    print("\n--- SONUÇLAR ---")
    print("Toplam harcama:", toplam_harcama, "TL")
    print("Ortalama harcama:", ortalama_harcama, "TL")
    print("En yüksek harcama:", max_expense, "TL")
    print("En düşük harcama:", min_expense, "TL")

    # args fonksiyonu test
    print("\n--- ARGS TEST ---")
    flexible_total(*expenses)


main()