import random

# This function prints out the current layout of the card table.
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

# Check whether 2 x non-picture cards add up to 12
def checkTwelve(curTable):
	for x in range(len(curTable)):
		if isinstance(curTable[x][0], int):
			for y in range (x+1, len(curTable)):
				if isinstance(curTable[y][0], int):
					if curTable[x][0] + curTable[y][0] == 12:
						return(x, y)
	return(99,99)

# Check whether the table has 4 of the same picture cards (e.g. 4 x jacks)
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

# Check whether there is a picture card straight (i.e. jack, queen, king, ace) in the same suit
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

# Create a pack of cards and shuffle
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

# Start playing...
winCount = 0
games = 0
maxAttempts = 0
attempts = 0
while games < 100000:
	games += 1
	thisPack = createPack()
	attempts += 1
	table = [0] * 12
	for x in range(12):
		table[x] = thisPack[0]
		del thisPack[0]
	while len(thisPack) > 0:
		cardOne, cardTwo = checkTwelve(table)
		foundFour = checkFourOfKind(table)
		foundStraight = checkStraight(table)

		if (foundFour[0] != 99) & (len(thisPack) > 2):
			for i in range (len(foundFour)):
				table[foundFour[i]] = thisPack[0]
				del thisPack[0]
		elif (foundStraight[0] != 99) & (len(thisPack) > 2):
			for i in range (len(foundStraight)):
				table[foundStraight[i]] = thisPack[0]
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
		winRatio = winCount / games * 100
		if (winCount % 100) == 0:
			print(str(winCount) + ' wins')
		attempts = 0
	if attempts > maxAttempts:
		maxAttempts = attempts

print('The success rate was : ' + '{:.2f}'.format(winRatio) + ' %')
print('Maximum attempts between wins: ' + str(maxAttempts))
print('Games played: ' + str(games))
