def GetTreeCountBySlope(slope_x, slope_y):
	#Get info from file
	with open("input.txt", "r") as file:
		fieldTemplate = [line.strip() for line in file]

	field = fieldTemplate	
	sledPos = [0, 0]
	slope = [slope_x, slope_y]
	treeCount = 0


	while True:
		if (sledPos[1] >= len(field) - 1):
				break
		sledPos[0] += slope[0]
		sledPos[1] += slope[1]
		if(sledPos[0] >= len(field[0])):
			for x in range (0,len(field)):
				field[x] += fieldTemplate[x]
		if (field[sledPos[1]][sledPos[0]] == "#"):
			hitMarker = 'X'
			treeCount += 1
		else:
			hitMarker = 'O'
		field[sledPos[1]] = field[sledPos[1]] = field[sledPos[1]][:sledPos[0]] + hitMarker + field[sledPos[1]][sledPos[0] + 1:]
		#print(field[sledPos[1]])
		
		
	print(treeCount)
	return treeCount


print(GetTreeCountBySlope(1,1) * GetTreeCountBySlope(3,1) * GetTreeCountBySlope(5,1) * GetTreeCountBySlope(7,1) * GetTreeCountBySlope(1,2))
# GetTreeCountBySlope(1,1)
# GetTreeCountBySlope(3,1)
# GetTreeCountBySlope(5,1)
# GetTreeCountBySlope(7,1)
# GetTreeCountBySlope(1,2)
	