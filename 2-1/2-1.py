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
	minMax = conditions[0].split("-")
	#print(str(minMax[0]) + str(minMax[1]) + str(requiredCharacter) + str(password))
	#Check conditions
	counter = password.count(requiredCharacter)
	if counter >= int(minMax[0]) and counter <= int(minMax[1]):
		validCounter += 1
print(validCounter)