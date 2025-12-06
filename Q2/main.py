from add import add
from subtract import subtract
from multiply import multiply

while True:
    answer = 0

    n = int(input("Choose an option: \n1. add \n2. subtract \n3. multiply \n4.exit\n: "))
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    L = []
    L.append(a)
    L.append(b)

    if n == 1:
        ans = add(L)
    elif n == 2:
        ans = subtract(a,b)
    elif n == 3:
        ans = multiply(a,b)
    else:
        break
    print(f"ans = {ans}")