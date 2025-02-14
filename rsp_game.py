import random
r = ["가위","바위","보"]

while True:
    user = input("가위 바위 보 중 입력하세요.")
    if user in r:
        break
    print("잘못된 입력입니다. 다시 입력하세요.")

computer = random.choice(r)

print(f"컴퓨터가 낸 값={computer}")
if computer == r[0] and user == r[1] or computer == r[1] and user == r[2] or computer == r[2] and user == r[0]:
    print("이겼습니다.")

elif computer == r[0] and user == r[0] or computer == r[1] and user == r[1] or computer == r[2] and user == r[2]:
    print("비겼습니다.")

else: 
    print("졌습니다.")
