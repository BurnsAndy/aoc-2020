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

print("Vulnerability: " + str(vulnerability))

#look for consecutive series to find weakness range
start_range = 0
end_range = 0
for x in range(len(inputs)):
	sum = 0
	for y in range(x,len(inputs)):
		if(int(sum) < int(vulnerability) and start_range == 0):
			sum += int(inputs[y])
			if(sum == int(vulnerability)):
				print("Weakness Range: (" + str(x) + "," + str(y) + ")")
				start_range = x
				end_range = y

#find smallest/largest numbers in weakness range and sum them
low = int(inputs[start_range])
high = int(inputs[start_range])
for x in range(start_range,end_range):
	if(int(inputs[x]) < low):
		low = int(inputs[x])
	if(int(inputs[x]) > high):
		high = int(inputs[x])
print("Weakness Number: " + str(int(low) + int(high)))