#Get info from file
with open("input.txt", "r") as file:
	input_lines = [line.strip() for line in file]
	
#Go through each line, break apart line to get relevant data, then check conditions, counting valid passwords
validCounter = 0
for line in input_lines:
	#Break apart line
	halves = line.split(": ")
	password = halves[1]
	conditions = halves[0].split(" ")
	requiredCharacter = conditions[1]
	firstSecond = conditions[0].split("-")
	first = int(firstSecond[0]) - 1
	second = int(firstSecond[1]) - 1
	#Check conditions
	if (password[first] == requiredCharacter) != (password[second] == requiredCharacter):
		validCounter += 1
print(validCounter)