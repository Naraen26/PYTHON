#MATCH (match statement selects one of many code blocks to be executed)

day = 7

match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")

#SAMPLE 2

day = 3

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("weekdays")

    case 6 | 7:
        print("weekends")

    case _:
        print("Invalid day")