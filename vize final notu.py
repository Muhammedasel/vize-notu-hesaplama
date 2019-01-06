vize1= float(input("kısa sınav notunuzu girin   : "))
vize2= float(input("vize notunuzu giriniz : "))
final= float(input("final notunuzu giriniz : "))

vize1= (vize1*30)/100
vize2= (vize2*30)/100
final= (final*40)/100

sonuç=  vize1+vize2+final

print("SINAV SONUCUNUZ : ", sonuç)

if(sonuç>=90):
    print("AA ALDINIZ.")
elif(sonuç>=85):
    print("BA ALDINIZ.")
elif(sonuç>=80):
    print("BB ALDINIZ.")
elif(sonuç>=75):
    print("CB ALDINIZ.")
elif(sonuç>=70):
    print("CC ALDINIZ.")
elif(sonuç>=65):
    print("DC ALDINIZ.")
elif(sonuç>=60):
    print("DD ALDINIZ.")
elif(sonuç>=55):
    print("FD ALDINIZ.")
elif(sonuç<=50):
    print("FF ALDINIZ , KALDINIZ.")
else:
    print("HATALI GİRİŞ YAPTINIZ.")
