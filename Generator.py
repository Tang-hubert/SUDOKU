def generateGrid():
	from random import sample

	def pattern(r,c):
		return (3*(r%3)+r//3+c)%9

	num=sample(range(1,10),9)
    
	row=[i*3+j for i in sample(range(1,4),3) for j in sample(range(1,4),3)]
	column=[i*3+j for i in sample(range(1,4),3) for j in sample(range(1,4),3)]
	board=[[num[pattern(r,c)] for c in column]for r in row]
    
	def checkValidity(list):
		numList=[]
		for i in range(9):
			for j in list[i]:
				if j not in numList:
					numList.append(j)
				else: return False
			numList.clear()
		return True

	if checkValidity(board) is True:
		print("Sodoku generate successfully.")
		return board
	else:
		print("Sodoku generate unsuccessfully.")
		generateGrid()

	return board

def displayBoard(list,lv):
	from random import sample,randint
	def difficulty(lv):
		if lv=='easy':
			return randint(20,30)
		if lv=='normal':
			return randint(30,60)
		if lv=='hard':
			return randint(60,75)
	for i in sample(range(1,81),difficulty(lv)):
		list[i//9][i%9]=0
	return list

board=generateGrid()
for i in range(9):
    print(board[i])
print("============================")
displayBoard=displayBoard(board,'hard')
for i in range(9):
	print(displayBoard[i])