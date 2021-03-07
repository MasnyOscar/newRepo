import os

a = input("""Witaj użytkowniku! Co chcesz zrobić?
______________________________________________
1- dokonać zapisu faktury
2- odczytac faktury

WYBIERAM: """)

if a == "1":
    data = open("dane.txt", "w")
    os.system('cls')
    indeks = input("Podaj indeks: ")
    c_netto = input("Podaj cenę netto [zł]: ")
    c_brutto = input("Podaj cenę brutto [zł]: ")
    c_sprzedazy = input("Podaj cenę sprzedaży [zł]: ")
    ilosc = input("Podaj ilość [szt]: ")
    vat = input("Podaj stawkę vat [%]: ")


    if data.writable():
        data.write("Indeks:   " + indeks)
        data.write("\n" + "Cena netto:   " + c_netto + " zł")
        data.write("\n" + "Cena brutto:  " + c_brutto + " zł")
        data.write("\n" + "Cena sprzedaży:  " + c_sprzedazy + " zł")
        data.write("\n" + "Ilość:  " + ilosc + " szt")
        data.write("\n" + "Vat:  " + vat + " %")
        data.write("""
        
        
        """)
    data.close()

elif a == "2":
    data = open("dane.txt", "r")
    if data.readable():
        data_read = data.read()
        print("Zawartość ostatniej faktury: ")
        print("\n")
        print(data_read)
    data.close()

