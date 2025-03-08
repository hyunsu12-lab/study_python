def mul(a):
    for i in range(9):
        print(f"{a} x {i + 1} = {a * (i + 1)}")

user = int(input("자연수를 입력해주세요."))

mul(user)