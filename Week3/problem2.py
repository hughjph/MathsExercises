import math


def start():
    number = int(input("Input a number to check below: "))
    prime_list = list(range(2, number))

    k = 2

    while k < math.sqrt(number):
        if k in prime_list:
            for integer in prime_list:
                if integer%k == 0 and integer!=k:
                    prime_list.remove(integer)
        k+=1
    print(prime_list)

start()