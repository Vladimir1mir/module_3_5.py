def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1 and first == 0:
        return 1
    elif len(str_number) == 1 and first != 0:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))
result = get_multiplied_digits(40420) #0420 выдает 0
print(result)
