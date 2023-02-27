
def start():
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))

    hcf = calc_hcf(a,b)
    lcm = calc_lcm(a,b,hcf)
    print("HCF: " + str(hcf))
    print("LCM: " + str(lcm))


def calc_hcf(a, b):
    while a!=0 and b!=0:
        if a>b:
            a = a%b
        else:
            b = b%a

    return a if a!=0 else b

def calc_lcm(a,b,hcf):
    return (a*b)/hcf

start()