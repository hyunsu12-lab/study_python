while True:
    number = int(input("3 이상 홀수를 입력해주세요."))
    if number >= 3 and number %2 != 0:
        for i in range(number//2 + 1):
            print(' ' * i + '*' * (number - (2 * i)))
        for i in range(number//2 -1 , -1, -1):
            print(' ' * i + '*' * (number - (2 * i)))
        break
    else:
        print("다시 입력하세요.")