import string

#get input
with open("input.txt", "r") as file:
	lines = [line.strip() for line in file]

raw_input = ""
	
for line in lines:
	if (line == ""):
		raw_input += " "
	else:
		raw_input += line
print(raw_input)
inputs = raw_input.split()
reduced_inputs = []
for input in inputs:
	reduced = ""
	for letter in list(string.ascii_lowercase):
		if (input.find(letter) != -1):
			reduced += letter
	reduced_inputs.append(reduced)
	
yeses = 0
for input in reduced_inputs:
	yeses += len(input)
	
print(yeses)