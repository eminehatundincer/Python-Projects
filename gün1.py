raw_data ="  AhMeT  yILMAZ ;  23 ;  1.78 ;  ahmetYILMAZ@GMAIL.Com   "

yeni_data = raw_data.strip().split(";")
print( yeni_data)

isim_duzelt= yeni_data[0][0:20].strip().lower().title()
print("Kullanıcı:", isim_duzelt)

simdiki_yas= int(yeni_data[1].strip())
yas_duzelt = float(simdiki_yas+10)
print("Yaş (10 yıl sonra):", yas_duzelt)

boy = float(yeni_data[2].strip())
boy_cm = boy * 100
print("Boy (cm):", boy_cm )

email_duzelt =yeni_data[3].strip().lower()
email_temiz = email_duzelt.find("@")
email_yeni = email_duzelt[0:email_temiz]
ilk_uc=email_yeni[0:3]
print("Email kullanıcı kodu:", ilk_uc)



