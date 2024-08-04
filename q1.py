import random

x = random.randint(1, 50)
print(x)
for w in range(5):
    y = int(input("請猜一個數字"))
    if x == y:
        print("猜對了")
        break
    else:
        if x > y:
            print("猜高一點")
        else:
            print("猜錯了 ~~~~")
if x != y:
    print(f"答案為:{x}")
else:
    print("以上皆非")
