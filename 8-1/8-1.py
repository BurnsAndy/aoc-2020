with open("input.txt", "r") as file:
			inputs = [line.strip() for line in file]
			
acc = 0
instructions = []
exc_instr = []
for line in inputs:
	t_instr = line.split()
	instructions.append(t_instr)

x = 0
while(x >= 0 and x < len(instructions)):
	
	#test if instruction has been visited before
	if(x in exc_instr):
		print(x)
		print(acc)
		print(exc_instr)
		break
	else:
		exc_instr.append(x)
	
	#get instruction
	instr = instructions[x]
	
	#acc
	if(instr[0] == "acc"):
		if(instr[1][0] == '+'):
			acc += int(instr[1][1:])
		else:
			acc -= int(instr[1][1:])
	
	#jmp
	if(instr[0] == "jmp"):
		if(instr[1][0] == '+'):
			x += int(instr[1][1:])
		else:
			x -= int(instr[1][1:])
	else:
		x += 1

print(acc)