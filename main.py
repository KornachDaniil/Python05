def print_number_with_multi(number):
    while number > 0:
        num = number % 10
        number //= 10
        if number:
            print(num, ", ", sep="", end="")
        else:
            print(num)


number = int(input("Введите число: "))
print_number_with_multi(number)
