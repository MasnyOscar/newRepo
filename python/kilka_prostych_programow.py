print("Witaj w podstawowym kalkulatorze.")
fn= input("Podaj 1 liczbe: ")
sn= input("Podaj 2 liczbe: ")
char= input("Podaj znak: ")

if char == "+":
    print("Wynik wynosi:")
    print( float (fn) + float (sn) )


if char == "+":
    print("Wynik wynosi:")
    print( float (fn) - float (sn) )

if char == "*":
    print("Wynik wynosi:")
    print( float (fn) * float (sn) )


if char == "/":
    print("Wynik wynosi:")
    print( float (fn) / float (sn) )


if char == "**":
    print("Wynik wynosi:")
    print( float (fn) ** float (sn) )

print("\n")
print("\n")
###################################

login= input("Podaj login: ")
password= input("Podaj haslo: ")

if login == "oskarsarba@gmail.com" and password == "admin":
    print("Zalogowano!")

else:
    print("Nie udało się zalogować :(")

print("\n")
print("\n")
################################################


print("Program do liczenia pola trapezu")

a= input("Podaj dlugosc pierwszego boku (cm) : ")
b= input("Podaj dlugosc drugiego boku (cm) : ")
h= input("Podaj dlugosc wysokosci (cm) :" )
wynik= ( (float(a) + float(b)) * 0.5 * float(h) )

if wynik or a or b or h <= 0:
    print("Podano niepoprawne dane.")

else:
    print("Pole trapezu o padanych wymiarach wynosi: ")
    print(wynik)
