print("Witaj w tym oto kalkulatorze bmi ;-)")

#deklaracja zmiennych
a= input("podaj wage: ")
b= input("podaj wzrost: ")

print("Twoje BMI wynosi: ")

#tutaj trzeba skonwertowac typ zmiennych, bo domyslnie jest to typ STRING
print(float (a) / (float (b) * float (b) ) )
