print("Kaklulator figur geometrycznych")
operacja= input("""1- pole
2- objętość
Wybierz co chcesz obliczyć: """)
print("\n")
if operacja == "1":
    figura= input("""
    WYBRŁEŚ POLE
   --------------
    1- kwadrat
    2- trójkąt
    3- trapez
    4- prostokąt
    5- koło
    Wybierz figurę: """ )

    if figura == "1":
        print("\n")
        print(" WYBRAŁEŚ KWADRAT")
        print("------------------")
        a= input("Podaj dlugosc boku (cm): ")
        if float(a) > 0:
            print("Pole kwadratu o podanych wymiarach wynosi: ",(float(a) ** 2), "cm²")
        else:
            print("Podaj wartości większe od 0.")


    elif figura == "2":
        print("\n")
        print(" WYBRAŁEŚ TRÓJKĄT")
        print("------------------")
        a= input("Podaj długość 1 boku (cm): ")
        h= input("Podaj wysokości (cm): ")
        if float(a) >0:
            if float(h) > 0:
                print("Pole trójkąta o podanych wymiarach wynosi: ", (float(a) * float(h)) / 2, "cm²")
            else:
                print("Podaj wartości większe od 0.")
        else:
            print("Podaj wartości większe od 0.")


    elif figura == "3":
        print("\n")
        print(" WYBRAŁEŚ TRAPEZ")
        print("-----------------")
        a= input("Podaj długość 1 boku (cm): ")
        b= input("Podaj długość 2 boku (cm): ")
        h= input("Podaj długość wysokości (cm): ")
        if float(a)> 0:
            if float(b) > 0:
                if float(h) > 0:
                    print("Pole trapezu o podanych wymiarach wynosi: ", (float(a) + float(b)) * float(h) / 2 ,"cm²")

                else:
                    print("Podaj wartości większe od 0.")
            else:
                print("Podaj wartości większe od 0.")
        else:
            print("Podaj wartości większe od 0.")



    elif figura == "4":
        print("\n")
        print(" WYBRAŁEŚ PROSTOKĄT")
        print("--------------------")
        a= input("Podaj długość 1 boku (cm): ")
        b= input("Podaj długość 2 boku (cm): ")
        if float(a) > 0:
            if float(b) > 0:
                print("Pole prostokąta o podanych wymarach wynosi: ", float(a) * float(b), "cm²")
            else:
                print("Podaj wartość większe od 0.")
        else:
            print("Podaj wartości większe od 0.")


    elif figura == "5":
        print("\n")
        print(" WYBRAŁEŚ KOŁO")
        print("---------------")
        r= input("Podaj promień (cm): ")
        if float(r) > 0:
            print("Pole koła o podanych wymiarach wynosi: ", 3.14 * (float(r) ** 2),"cm²" )
        else:
            print("Podaj wartości większe od 0.")

elif operacja == "2":
    figura= input("""
    WYBRŁEŚ OBJĘTOŚĆ
   ------------------
    1- sześcian
    2- prostopadłościan
    3- graniastosłup prosty
    Wybierz figurę: """ )

if figura == "1":
    print("\n")
    print(" WYBRAŁEŚ SZEŚCIAN")
    print("-------------------")
    a = input("Podaj dlugosc krawędzi (cm): ")
    if float(a) > 0:
        print("Objętość sześcianu o podanych wymiarach wynosi: ", (float(a) ** 3), "cm³")
    else:
        print("Podaj wartości większe od 0.")

elif figura == "2":
    print("\n")
    print(" WYBRAŁEŚ PROSTOPADŁOŚCIAN")
    print("---------------------------")
    a= input("Podaj długość 1 boku (cm): ")
    b= input("Podaj długość 2 boku (cm): ")
    c= input("Podaj długość 3 boku (cm): ")
    if float(a)> 0:
        if float(b) > 0:
            if float(c) > 0:
                print("Objętość prostopadłościanu o podanych wymiarach wynosi: ", float(a) * float(b) * float(c) ,"cm³")

            else:
                    print("Podaj wartości większe od 0.")
        else:
                print("Podaj wartości większe od 0.")
    else:
            print("Podaj wartości większe od 0.")

elif figura == "3":
    print("\n")
    print(" WYBRAŁEŚ GRANIASTOSŁUP PROSTY")
    print("-------------------------------")
    pp= input("Podaj pole podstawy (cm²): ")
    h= input("Podaj wysokość (cm): ")
    if float(pp)> 0:
        if float(h) > 0:
            print("Objętość graniastosłupa prostego o podany wymiarach wynosi:", float(pp) * float(h), "cm³" )
        else:
                print("Podaj wartości większe od 0.")
    else:
            print("Podaj wartości większe od 0.")
