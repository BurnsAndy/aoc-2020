def BSP(finput, frange):
	#print(finput[0])
	
	if(finput[0] == 'F' or finput[0] == 'L'):
		frange = frange[:int(len(frange)/2)]
	if(finput[0] == 'B' or finput[0] == 'R'):
		frange = frange[int(len(frange)/2):]
		
	#print(frange)
	
	if (len(finput) != 1):
		out = BSP(finput[1:], frange)
		return out
	else:
		return frange[0]
	
def FindSeatID(finput):
	return (int(BSP(input[:-3], rows)) * 8 + int(BSP(input[-3:], columns)))

#get input
with open("input.txt", "r") as file:
	inputs = [line.strip() for line in file]

rows = []
columns = []	
seat_list = []

#fill out row array
for i in range(128):
	rows.append(i)
#fill out column array
for i in range(8):
	columns.append(i)

#get highest seat id
highest_seat_id = 0
for input in inputs:
	#print(input + " - " + str(FindSeatID(input)))
	seat_list.append(FindSeatID(input))
	
#find missing seat
seat_list.sort()
for i in range(len(seat_list)):
	if(i != (len(seat_list) - 1)):
		if((seat_list[i] + 1) != (seat_list[i+1])):
			print(seat_list[i] + 1)
