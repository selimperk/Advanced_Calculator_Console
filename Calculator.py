import Functions as fct

# CODE BEGINN

while True:
    fct.display_menu()
    start= str(input("----------Do you want to calculate? (Y) / (N)----------\n")).lower()

    if start == "y":
        #menu no1
        print(""""
                ====================================
                (1): Simple calculations
                (2): Graphicical overview
                (3): Advanced functions
                (4): Quit
                ====================================""")
        choice_start = input("Please choose an option (1-4):\n")

        #menu simple calculation
        if choice_start == "1":
            number1, number2 = fct.get_numbers()
            print(""""
            ====================================
            (1): Addition
            (2): Subtraction
            (3): Multiplication
            (4): Division
            (5): Modulo
            (6): Quit
            ====================================""")
            choice_simple = input("Please choose an option (1-6):\n")
    
            if choice_simple == "1":
                fct.addition(number1,number2)
            elif choice_simple == "2":
                fct.subtraction(number1,number2)
            elif choice_simple == "3":
                fct.multiplication(number1,number2)
            elif choice_simple == "4":
                fct.division(number1,number2)
            elif choice_simple == "5":
                fct.modulo(number1,number2)
            elif choice_simple == "6":
                break
            else:
                print("Invalid! Please enter a number between 1-6")

        #menu graphical overview
        elif choice_start == "2":
            print(""""
                            ====================================
                            (1): Sinus function
                            (2): Cosinus function
                            (3): Quadratic function
                            (4): Linear functions
                            (5): Circular functions
                            (6): Quit
                            ====================================""")
            choice_graphic = input("Please choose an option (1-6):\n")

            if choice_graphic == "1":
                fct.sinus_display()
            elif choice_graphic == "2":
                fct.cosinus_display()
            elif choice_graphic == "3":
                fct.quadratic_display()
            elif choice_graphic == "4":
                fct.linear_display()
            elif choice_graphic == "5":
                fct.circular_display()
            elif choice_graphic == "6":
                break
            else:
                print("Please enter a number between 1-6!")

        #menu advanced functions
        elif choice_start == "3":
            print(""""
                                        ====================================
                                        (1): ETF - Saving Plan Calculator
                                        (2): Currency Exchange
                                        (3): Quit
                                        ====================================""")
            choice_advanced = input("Please choose an option (1-4):\n")

            if choice_advanced == "1":
                fct.etf_saving()
            elif choice_advanced == "2":
                fct.currency_exchange()
            elif choice_advanced == "3":
                break
            else:
                print("Please enter a number between 1-3!")
        elif choice_start == "4":
            break
    else:
        break
