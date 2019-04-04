from module import sub, add, mul, div, rt

print("  Menu \n \n --------\n 1: add \n 2: sub\n 3: multiply\n 4: divide \n 5: root\n 6:stop\n ")
user=int(input(": "))
if user == 6:
    print("프로그램을 종료합니다.")
elif user == 5:
    r_first=int(input("num1: "))
    print(rt(r_first))
elif user not in range(1, 7):
    print("Beep!")
else:
    first=int(input("num1: ")) 
    second=int(input("num2: "))
    if user ==1:
        print(add(first, second))
    if user == 2:
        print(sub(first, second))
    if user == 3:
        print(mul(first, second))
    if user ==4:
        print(mul(first, second))