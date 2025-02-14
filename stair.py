number = int(input("줄을 입력해요"))

# for i in range(1, number + 1):
#     print(' ' * ((i - 2) + 1) + '*' * ((number + 1) - i))

for i in range(number, 0, -1):
    print(' ' * (number - i) + '*' * i)