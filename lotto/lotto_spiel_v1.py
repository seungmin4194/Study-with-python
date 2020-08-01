#자동, 수동 구매
#자동구매하면 자동으로 번호획득
#수동 구매하면 직접 7번째 자리까지 입력
#로또 추첨은 구매후 3초 후 카운트다운
#추첨 번호당 차례대로 4초씩 걸림
#재구매 질문은 예스 또는 노
#로또 회차 표시
"""Lotto Spiel"""
import random

lotto = []
random_number = random.randint(1, 100)
for i in range(6):
    while random_number in lotto:
        random_number = random.randint(1, 100)
    lotto.append(random_number)

lottoNumber = list(map(int, input("Geben Sie 6 Zahlen: ").split()))

if len(lottoNumber) == 6 and lotto == lottoNumber:
    print("Sie haben Lotto gewinnen!")
    print("Deine Nummer sind: {}".format(lottoNumber))
    print("Lotto Nummer sind: {}".format(lotto))

elif len(lottoNumber) == 6 and lotto != lottoNumber:
    print("Nachstes Mal...")
    print("Deine Nummer sind: {}".format(lottoNumber))
    print("Lotto Nummer sind: {}".format(lotto))

else:
    lottoNumber = list(map(int, input("Geben Sie 6 Zahlen: ").split()))
