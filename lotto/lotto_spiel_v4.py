import random
import time

class Lotto:
	def __init__(self):
		self.lottoNum = set()
		self.autoNum = set()
		self.manualNum = set()

	def new(self):
		self.lottoNum.clear()
		self.manualNum = set()
		self.autoNum = set()
		while len(self.lottoNum) < 6:
			self.lottoNum.add(random.randrange(1, 46)
		
	def auto(self):
		self.autoNum.clear()
		while len(self.autoNum) < 6:
			self.autoNum.add(random.randrange(1, 46)

	def insert(self):
		self.manualNum.clear()
		while len(self.manualNum) < 6:
			n = int(input())
			if (n <= 0) or (n >= 46) or (n in self.manualNum):
				print("중복된 번호를 넣었거나 잘못된 번호를 입력하였습니다. 다시 입력해주세요.")
				continue
			self.manualNum.add(n)
			print("현재까지 번호: " + str(list(self.manualNum)))

	def match(self):
		if len(self.manualNum) != 6:
			print("2번을 선택하여 번호를 다시 입력해주세요")
			return

		matchingMyNum = len(self.lottoNum.intersection(self.manualNum))
		if matchingMyNum == 6:
			print("Sie haben gewonnen!")
		else:
			print("Nächstes Mal...")

		matchingAutoNum = len(self.lottoNum.intersection(self.autoNum))
		if matchingAutoNum == 6:
			print("Sie haben gewonnen!")
		else:
			print("Nächstes Mal...")

print("로또 프로그램을 실행합니다.")
lotto = Lotto()
lotto.new()
while True:
	print("1. 로또 번호 자동")
	print("2. 로또 번호 수동")
	print("3. 새로운 로또 번호")
	print("4. 로또 당첨 확인")
	print("5. 종료")

	num = int(input())
	if num == 1:
		lotto.auto()
	elif num == 2:
		lotto.insert()
	elif num == 3:
		lotto.new()
	elif num == 4:
		lotto.match()
	elif num == 5:
		break

