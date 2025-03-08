import random

ran_num = random.sample(range(1,10), 3)

while True:
    user = list(map(int, input("1~9 숫자를 3개 입력하시오.").split())) 
    if len(user) != 3 or type(user[0]) != int or type(user[1]) != int or type(user[2]) != int or all(num > 9 for num in user) or all(num < 1 for num in user):
        print("잘못된 입력입니다.")
        continue
    
    for i in range(3):
        if user[i] == ran_num[i]:
            print("strike")
        else:
            print("ball")

    if user == ran_num:
        print("게임 성공")
        break    