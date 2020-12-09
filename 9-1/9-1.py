def SumExists(checkList, sum):
	for x in range(len(checkList)):
		for y in range(len(checkList)):
			if ((x != y) and (int(checkList[x]) + int(checkList[y]) == int(sum))):
				return True
	return False

with open("input.txt", "r") as file:
	inputs = [line.strip() for line in file]

preamble_length = 25
preamble = list()
vulnerability = 0

#build preamble
for x in range(preamble_length):
	preamble.append(int(inputs[x]))

#check sums and look for vulnerability
for x in range(preamble_length,len(inputs)):
	if (SumExists(preamble, inputs[x])):
		preamble.pop(0)
		preamble.append(inputs[x])
	else:
		vulnerability = inputs[x]
		break

print(vulnerability)
