
try:
    a = [int(i) for i in input("Input number A: ")]
    b = int(input("Input number B: "))
    if b <= 0:
        raise Exception
except:
    print("Inputs should be positive integers")
    exit()


q_array = []
r = 0

for i in range(len(a)):
    count = 0
    while a[i] >= b:
        a[i] -= b
        count += 1

    if i == (len(a) - 1):
        r = a[i]
        q_array.append(count)
    else:
        a[i+1] = int(str(a[i]) + str(a[i+1]))
        q_array.append(count)


q = 0

for i in range(len(q_array)):
    q = q*10 + q_array[i]


print("Quotient of A divided by B: " + str(q))
print("Remainder of A divided by B: " + str(r))
