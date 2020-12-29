#tutaj zaciagam potrzebne fumckcje itp. z biblioteki
from random import randint

#tutaj tworze losowa liczbe z danego przedzialy
random= randint(1, 15)

#tutaj deklaruje zmienna i, ktora bedzie inkrementowana
i= 0

#tutaj zaczyna sie petla, ktora bedzie trwala dopoki ktps nie poda poprawnej liczby
while i!=random:
    i+=1
    usr_num = input("Podaj liczbe od 1 do 15: ")
    if random > int(usr_num):
        print("\n")
        print("Podaj wieksza liczbe:")

    elif random < int(usr_num):
        print("\n")
        print("Podaj mniejsza liczbe:")

    elif random == int(usr_num):
        print("\n")
        print("Podano poprawną liczbę :)", "za", i,"razem")
        break
