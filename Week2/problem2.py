
alphanum = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def start():
    number = int(input("Input a natural number: "))
    old_base = int(input("Input the base of this number: "))
    new_base = int(input("Input the new base of the number: "))

    if old_base <= 1 or new_base <= 1 or number < 1:
        print("Bases should be greater than 1 and the number should be at least 1")
        exit()

    if old_base != 10:
        number = convert_to_base_10(number, old_base)

    remainder_array = []

    while number > 0:
        number, remainder = quotient_remainder(number, new_base)
        print(remainder)
        remainder_array.append(alphanum[remainder])

    result = ""
    remainder_array.reverse()
    for i in range(len(remainder_array)):
        result += remainder_array[i]

    print(result)

def convert_to_base_10(number, old_base):
    number = [int(x) for x in str(number)]

    result = 0
    for i in range(len(number)):
        result += number[i] * (old_base ** (len(number) - i))

    return result

def quotient_remainder(number, new_base):
    number = [int(x) for x in str(number)]
    quotient_array = []
    remainder = 0

    for i in range(len(number)):
        count = 0
        while number[i] >= new_base:
            number[i] -= new_base
            count += 1

        if i == (len(number) - 1):
            remainder = number[i]
            quotient_array.append(count)
        else:
            number[i + 1] = int(str(number[i]) + str(number[i + 1]))
            quotient_array.append(count)

    quotient = 0

    for i in range(len(quotient_array)):
        quotient = quotient * 10 + quotient_array[i]

    return quotient, remainder


start()