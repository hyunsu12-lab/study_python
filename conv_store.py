sale_list = {'삼각김밥': 1200, '샌드위치': 2500, '도시락': 4500, '콜라': 1800, '과자': 2000}
total = 0

while True:
    user = input("구매할 상품을 입력하세요 (끝 입력 시 종료)")
    if user == '끝':
        break
    total += sale_list[user]
print(f"총 구매 금액 {total}원")
if total >= 20000 and total < 50000:
    print("할인 적용 (10%)")
    print(f"최종 구매 금액: {int(total * 0.9)}원")
elif total >= 50000:
    print("할인 적용 (20%)")
    print(f"최종 구매 금액: {int(total * 0.8)}원")
else:
    print("할인 없음")
