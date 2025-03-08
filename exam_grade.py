def check(a):
    if 90 <= a <= 100:
        print("A")
    elif 80 <= a <= 89:
        print("B")
    elif 70 <= a <= 79:
        print("C")
    elif 60 <= a <= 69:
        print("D")
    else:
        print("F")

grade = int(input("시험 성적을 입력해주세요."))
 
check(grade)