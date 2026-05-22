#Rastegele Anket Verisi
import random

scores = []

while len(scores) < 20:
    score = random.randint(0,6)

    if score == 0:
        break
    if score == 6:
        continue

    scores.append(score)

#Veri Kontrolü:
print("Geçerli puan sayısı:",len(scores))
#Döngünün ne zaman biteceğini biliyoruz ama kaç adımda duracağını bilmiyoruz o yüzden while döngüsü kullanılır. 

#Ortalama Hesaplama:
if len(scores) == 0: #0'a bölme hatasını önlemek için kontrol eklenir.
    print("Geçerli puan yok.")
else: 
    ortalama = sum(scores) / len(scores)
    print("Ortalama Puan:" , round(ortalama, 2))
    #Max-Min Analizi:
    print("En düşük puan:", min(scores)) 
    print("En yüksek puan:", max(scores))

#Memnuniyet Analizi:
memnun=0
kararsiz=0
memnun_degil=0
for puan in scores:
    if puan >= 4:
        memnun+= 1;
    elif puan == 3:
        kararsiz+= 1;    
    else:
        memnun_degil+= 1;
print("Memnun:", memnun)
print("Kararsız:", kararsiz)
print("Memnun Değil:", memnun_degil)

#Erken Uyarı Sistemi
art_ardabir=0
for puan in scores:
    if puan == 1:
        art_ardabir+=1
    else:
        art_ardabir=0

    if art_ardabir == 3:
        print("⚠️ Kritik memnuniyetsizlik tespit edildi")
        break











    


