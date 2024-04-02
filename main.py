def print_number(number):
    number_str = str(number)
    last_letter = number_str[-1]
    for i in number_str:
        if i != last_letter:
            print(i, ", ", sep="", end="")
        else:
            print(last_letter)


number = int(input("Введите число: "))
print_number(number)
