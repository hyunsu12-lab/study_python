number = int(input("줄의 개수를 입력해주세요."))

for i in range(1, number + 1):
    print(' ' * (number - i) + '*' * i)