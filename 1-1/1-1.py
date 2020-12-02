#Get info from file
with open("input.txt", "r") as file:
	input_lines = [line.strip() for line in file]

for line1 in input_lines:
	for line2 in input_lines:
		if(int(line1) + int(line2) == 2020):
			print(line1)
			print(line2)
			print((int(line1) * int(line2)))