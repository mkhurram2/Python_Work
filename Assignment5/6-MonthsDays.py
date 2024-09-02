#Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.

month = int(input("Enter a Month: " ))

match month:
    case 1:
        print("31 Days in Jan")
    case 2:
        print("28 Days in Feb")
    case 3:
        print("31 Days in Mar")
    case 4:
        print("30 Days in Apr")
    case 5:
        print("31 days in May")
    case 6:
        print("30 Jun in Jun")
    case 7:
        print("31 Days in Jul")
    case 8:
        print("31 Days in Aug")
    case 9:
        print("30 Days in Sep")
    case 10:
        print("31 Days in Oct")
    case 11:
        print("30 Days in Nov")
    case 12:
        print("31 Days in Dec")
    case _:
        print("Invaild Year Entered")