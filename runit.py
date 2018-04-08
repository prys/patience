import random

def tablePrint(curTable):
	print('')
	print('Table layout: ')
	print('')
	for x in range(12):
		if (x +1) % 4 == 0:
			print(curTable[x])
		else:
			print(curTable[x], end='')
	print()

def checkTwelve(curTable):
	for x in range(len(curTable)):
		if isinstance(curTable[x][0], int):
			for y in range (x+1, len(curTable)):
				if isinstance(curTable[y][0], int):
					if curTable[x][0] + curTable[y][0] == 12:
						return(x, y)
	return(99,99)

def checkFourOfKind(curTable):
	for x in range(len(curTable)):
		found = 1
		arrFound = [99] * 4
		if isinstance(curTable[x][0], str):
			arrFound[found-1] = x
			for y in range (x+1, len(curTable)):
				if isinstance(curTable[y][0], str):
					if curTable[x][0] == curTable[y][0]:
						found += 1
						arrFound[found-1] = y
				if found == 4:
					return(arrFound)
	return([99,99,99,99])

def checkStraight(curTable):
	for x in range(len(curTable)):
		arrFound = [99] * 4
		if isinstance(curTable[x][0], str):
			found = 1
			suitFound = curTable[x][1]
			arrFound[found-1] = x
			for y in range (x+1, len(curTable)):
				if isinstance(curTable[y][0], str):
					if curTable[y][1] == suitFound:
						found += 1
						arrFound[found-1] = y
						if found == 4:
							return(arrFound)
	return([99,99,99,99])

def createPack():
	curCard = 0
	pack = [[]]
	suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
	picCards = ['Jack', 'Queen', 'King', 'Ace']
	for x in range(len(suits)):
		for deck in range(2, 15):
			if curCard == 0:
				pack[curCard] = [deck, suits[x]]
			else:
				if deck >= 11:
					pack.append([picCards[deck-11], suits[x]])
				else:
					pack.append([deck, suits[x]])
			curCard += 1
	random.shuffle(pack)
	return(pack)

winCount = 0
attempts = 0
while winCount < 10000:
	attempts += 1
	thisPack = createPack()
	table = [0] * 12
	for x in range(12):
		table[x] = thisPack[0]
		del thisPack[0]
	while len(thisPack) > 0:
		cardOne, cardTwo = checkTwelve(table)
		foundFour = checkFourOfKind(table)
		foundStraight = checkStraight(table)

		if (foundFour[0] != 99) & (len(thisPack) > 2):
			table[foundFour[0]] = thisPack[0]
			del thisPack[0]
			table[foundFour[1]] = thisPack[0]
			del thisPack[0]
			table[foundFour[2]] = thisPack[0]
			del thisPack[0]
			table[foundFour[3]] = thisPack[0]
			del thisPack[0]
		elif (foundStraight[0] != 99) & (len(thisPack) > 2):
			table[foundStraight[0]] = thisPack[0]
			del thisPack[0]
			table[foundStraight[1]] = thisPack[0]
			del thisPack[0]
			table[foundStraight[2]] = thisPack[0]
			del thisPack[0]
			table[foundStraight[3]] = thisPack[0]
			del thisPack[0]
		elif cardOne != 99:
			table[cardOne] = thisPack[0]
			del thisPack[0]
			table[cardTwo] = thisPack[0]
			del thisPack[0]
		else:
			break
	if len(thisPack) == 0:
		winCount += 1
		winRatio = winCount / attempts * 100
		if (winCount % 100) == 0:
			print(winCount)

print('The success rate was : ' + str(winRatio) + '')
