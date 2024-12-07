# pobieranie potrzebnych zasobow
from random import randint

# ustawianie przedzialy z ktorego bedzie losowana liczba
random_number= randint(1, 100)

# zmienna i potrzebna do iteracji
i= 0


# początek pętli, bedzie sie powtarzać dopóki nie trafimy liczby
user_number = input("Podaj liczbe od 1 do 100: " )
while i!= random_number:
    i+=1


    if int(user_number)>random_number:
        user_number = input("Podaj Mniejszą liczbę: ")
        print("\n")
        
        
    elif int(user_number)<random_number:
        user_number = input("Podaj większą liczbę: ")
        print("\n")


    elif int(user_number)==random_number:
        print("Udało ci się za", i, "razem!")
        break
