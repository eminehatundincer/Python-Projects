from models import Budget
from notifications import EmailNotification, SMSNotification
from utils import get_user_expenses, generate_random_notification

# Hücre 1 – Proje Tanımı 
# Amaç: Harcamaları kaydetmek, bütçe limitini kontrol etmek ve aşım durumunda bildirim göndermek.
# Kullanılan konular: Python temelleri, koleksiyonlar, kontrol yapıları, fonksiyonlar, OOP, modüler yapı.
# Gerçekçi çünkü günlük finans yönetimi senaryosunu simüle ediyor.

# Hücre 2 – Kullanıcıdan Veri Alma
expenses = get_user_expenses()   # Harcamaları al, Expense nesnesine çevir, listeye ekle

# Hücre 3 – Bütçe Analizi
budget = Budget(limit=5000)      # Örnek limit: 5000 TL
for e in expenses:
    budget.add_expense(e)

print("Toplam harcama:", budget.total_expense(), "TL")
print("Ortalama harcama:", round(budget.average_expense(), 2), "TL")

# En büyük / en küçük harcama
if expenses:
    max_expense = max(expenses, key=lambda x: x.amount)
    min_expense = min(expenses, key=lambda x: x.amount)
    print("En büyük harcama:", max_expense)
    print("En küçük harcama:", min_expense)

# Set ile kategori analizi
categories = set(e.category for e in expenses)
print("Kategoriler:", categories)

# Hücre 4 – Limit Kontrolü
if budget.is_limit_exceeded():
    print("Limit durumu: AŞILDI")
else:
    print("Limit durumu: UYGUN")

# Hücre 5 – Bildirim Sistemi
notifications = [
    EmailNotification(generate_random_notification()),
    SMSNotification(generate_random_notification())
]

for n in notifications:
    n.send()   # Polymorphism çalışıyor

# Hücre 6 – Özet Çıktılar
print("\n--- Özet ---")
print("Toplam harcama:", budget.total_expense(), "TL")
print("Ortalama harcama:", round(budget.average_expense(), 2), "TL")
print("Limit durumu:", "AŞILDI" if budget.is_limit_exceeded() else "UYGUN")
print("Gönderilen bildirimler:")
for n in notifications:
    print("-", n.__class__.__name__, "gönderildi")
