# Match
# Similar to Swtch in Java
number = int(input("Enter a number \n"))

match number:
    case 1:
        print("you have entered 1")
    case 2:
        print("you have entered 2")

    case 3:
        print("you have enteredn 3")

    case _:  # Nothing is matching . I will run

        print("no idea")
