number = int(input("줄 개수를 입력하세요."))

# for i in range(1, number + 1):
#     print('*' * (number + 1 - i))

for i in range(number, 0, -1):
    print('*' * i)