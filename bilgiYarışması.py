import random
import sqlite3 as sql
isim = input("İsim-Soyisim giriniz:") #kullanıcıdan isim bilgisini alır

soruMetni=open("C:\\Users\\PC\\PycharmProjects\\Eğitim\\Sorularım.txt")
sorular=soruMetni.readlines()
doğruCevapSayısı=0
yanlışCevapSayısı=0

birinciSoruİndeks=random.randint(0,9)
birinciSoru=sorular[birinciSoruİndeks]
print(birinciSoru)
cevap1=input("Şıkkı Giriniz:")
if birinciSoruİndeks==0:
    if cevap1=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if birinciSoruİndeks==1:
    if cevap1=="B":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if birinciSoruİndeks==2:
    if cevap1=="D":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if birinciSoruİndeks==3:
    if cevap1=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if birinciSoruİndeks==4:
    if cevap1=="B":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if birinciSoruİndeks==5:
    if cevap1=="D":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if birinciSoruİndeks==6:
    if cevap1=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("Yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if birinciSoruİndeks==7:
    if cevap1=="C":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if birinciSoruİndeks==8:
    if cevap1=="B":
        print("Tebriklre Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if birinciSoruİndeks==9:
    if cevap1=="C":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
ikinciSoruİndeks=random.randint(0,9)
ikinciSoru=sorular[ikinciSoruİndeks]
print(ikinciSoru)
cevap2=input("Şıkkı Giriniz:")

if ikinciSoruİndeks==0:
    if cevap2=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if ikinciSoruİndeks==1:
    if cevap2=="B":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if ikinciSoruİndeks==2:
    if cevap2=="D":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if ikinciSoruİndeks==3:
    if cevap2=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if ikinciSoruİndeks==4:
    if cevap2=="B":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if ikinciSoruİndeks==5:
    if cevap2=="D":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if ikinciSoruİndeks==6:
    if cevap2=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("Yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if ikinciSoruİndeks==7:
    if cevap2=="C":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if ikinciSoruİndeks==8:
    if cevap2=="B":
        print("Tebriklre Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if ikinciSoruİndeks==9:
    if cevap2=="C":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1

üçüncüSoruİndeks=random.randint(0,9)
üçüncüSoru=sorular[üçüncüSoruİndeks]
print(üçüncüSoru)
cevap3=input("Şıkkı Giriniz: ")

if üçüncüSoruİndeks==0:
    if cevap3=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if üçüncüSoruİndeks==1:
    if cevap3=="B":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if üçüncüSoruİndeks==2:
    if cevap3=="D":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if üçüncüSoruİndeks==3:
    if cevap3=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if üçüncüSoruİndeks==4:
    if cevap3=="B":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if üçüncüSoruİndeks==5:
    if cevap3=="D":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if üçüncüSoruİndeks==6:
    if cevap3=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("Yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if üçüncüSoruİndeks==7:
    if cevap3=="C":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if üçüncüSoruİndeks==8:
    if cevap3=="B":
        print("Tebriklre Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if üçüncüSoruİndeks==9:
    if cevap3=="C":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1

dördüncüSoruİndeks=random.randint(0,9)
dördüncüSoru=sorular[dördüncüSoruİndeks]
print(dördüncüSoru)
cevap4=input("Şıkkı Giriniz : ")
if dördüncüSoruİndeks==0:
    if cevap4=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if dördüncüSoruİndeks==1:
    if cevap4=="B":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if dördüncüSoruİndeks==2:
    if cevap4=="D":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if dördüncüSoruİndeks==3:
    if cevap4=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if dördüncüSoruİndeks==4:
    if cevap4=="B":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if dördüncüSoruİndeks==5:
    if cevap4=="D":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if dördüncüSoruİndeks==6:
    if cevap4=="A":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("Yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if dördüncüSoruİndeks==7:
    if cevap4=="C":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if dördüncüSoruİndeks==8:
    if cevap4=="B":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1
if dördüncüSoruİndeks==9:
    if cevap4=="C":
        print("Tebrikler Doğru Cevap")
        doğruCevapSayısı=doğruCevapSayısı+1
    else:
        print("yanlış cevap")
        yanlışCevapSayısı=yanlışCevapSayısı+1

print("Doğru cevap sayınız: ",doğruCevapSayısı)
print("Yanlış cevap sayınız: ",yanlışCevapSayısı)

def puanHesaplama(doğruCevapSayısı,yanlışCevapSayısı):#puan ve ortalama basari hesaplaniyor
    soruSayisi=doğruCevapSayısı+yanlışCevapSayısı
    ortalamaBasari=int(((float(doğruCevapSayısı)-(float(yanlışCevapSayısı)/3))/float(soruSayisi))*100)
    return ortalamaBasari
print(puanHesaplama(doğruCevapSayısı,yanlışCevapSayısı))
ortalamaBasari=puanHesaplama(doğruCevapSayısı,yanlışCevapSayısı)

verilerim= [isim,doğruCevapSayısı,yanlışCevapSayısı,ortalamaBasari]
veriTabanı = sql.connect('yarışmacıBilgileri.sqlite')
imlec = veriTabanı.cursor()  #veri tabanında işlem yapabilmek için imleç yarattım
imlec.execute("CREATE TABLE IF NOT EXISTS yarışmacıVerileri (İSİM,DOĞRU CEVAP SAYISI,YANLIŞ CEVAP SAYISI,ORTALAMA BAŞARI)")

imlec.execute("INSERT INTO yarışmacıVerileri VALUES (?, ?, ?, ?)", verilerim)



veriTabanı.commit()
veriTabanı.close()

