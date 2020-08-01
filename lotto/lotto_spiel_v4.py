import random
import time

class Lotto:
	def __init__(self):
		self.win = set()
		self.autoNum = set()
		self.myNum = set()

	def init(self):
		self.win.clear()
		self.myNum = set()
		self.autoNum = set()
		while len(self.win) < 6:
			self.win.add(random.randrange(1, 46)
		
	def auto(self):
		self.autoNum.clear()
		while len(self.autoNum) < 6:
			self.autoNum.add(random.randrange(1, 46)

	def insert(self):
		self.myNum.clear()
		while len(self.myNum) < 6:
			print(str([len(self.myNum) + 1]))
			n = int(input())
			if (n <= 0) or (n >= 46) or (n in self.myNum):
				print("중복된 번호를 넣었거나 잘못된 번호를 입력하였습니다. 다시 입력해주세요.")
				continue
			self.myNum.add(n)
			print("현재까지 번호: " + str(list(self.myNum)))

	def match(self):
		if len(self.myNum) != 6:
			print("2번을 선택하여 번호를 다시 입력해주세요")
			return

		matchingMyNum = len(self.win.intersection(self.myNum))
		if matchingMyNum == 6:
			print("Sie haben gewonnen!")
		else:
			print("Nächstes Mal...")

		matchingAutoNum = len(self.win.intersection(self.autoNum))
		if matchingAutoNum == 6:
			print("Sie haben gewonnen!")
		else:
			print("Nächstes Mal...")

	def printMyNum(self):
		print("Meine Nummer sind: ", end="")
		arr = list(self.win)
		arr.sort()

		print(arr, end="")
		
print("로또 프로그램을 실행합니다.")
lotto = Lotto()
lotto.init()
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
		lotto.init()
	elif num == 4:
		lotto.match()
	elif num == 5:
		break

