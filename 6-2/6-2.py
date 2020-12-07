import string

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

#get input
with open("input.txt", "r") as file:
	lines = [line.strip() for line in file]

raw_input = ""
	
#set up inputs
for line in lines:
	if (line == ""):
		raw_input += " "
	else:
		raw_input += (line + '-')

inputs = raw_input.split()

#get yeses count
yeses = 0
for input in inputs:
	people = input.split('-')
	people.pop() #get rid of dumb empty element
	#count yeses
	if(len(people) == 1):
		#nothing fancy for one person groups
		yeses += len(people[0])
	else:
		#for multiple person groups, get intersetion of answer lists
		answers = list(people[0])
		for person in people:
			answers = intersection(answers, list(person))
		yeses += len(answers)
print(yeses)