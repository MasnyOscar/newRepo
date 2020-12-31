print("Kaklulator pól figur geometrycznych")
figura= input("""1- kwadrat 
2- trójkąt 
3- trapez 
4- prostokąt
Wybierz figurę: """ )

if figura == "1":
    print("Wybrałeś kwadrat")
    a= input("Podaj dlugosc boku (cm): ")
    print("Pole kwadratu o podanych wymiarach wynosi: ",(float(a) ** 2), "cm²")

elif figura == "2":
    print("Wybrałeś trójkąt")
    a= input("Podaj długość 1 boku (cm): ")
    h= input("Podaj wysokości (cm): ")
    print("Pole trójkąta o podanych wymiarach wynosi: ", (float(a) * float(h)) / 2, "cm²")

elif figura == "3":
    print("Wybrałeś trapez")
    a= input("Podaj długość 1 boku (cm): ")
    b= input("Podaj długość 2 boku (cm): ")
    h= input("Podaj długość wysokości (cm): ")
    print("Pole trapezu o podanych wymiarach wynosi: ", (float(a) + float(b)) * float(h) / 2 ,"cm²")

elif figura == "4":
    print("Wybrałeś prostokąt")
    a= input("Podaj długość 1 boku (cm): ")
    b= input("Podaj długość 2 boku (cm): ")
    print("Pole prostokąta o podanych wymarach wynosi: ", float(a) * float(b) ,"cm²")
