class Bag:
	bag = ""
	subBags = []
	def __init__(self, bagName):
		self.bag = bagName
		self.subBags = []
	def __str__(self):
		output = self.bag + " can contain: \n"
		for bag in self.subBags:
			output += "\t" + str(bag) + "\n"
		return output

def InputBags():	
	with open("test-input.txt", "r") as file:
			inputs = [line.strip() for line in file]

	for line in inputs:
		#setup top-level bag rules
		bagName = line.split(" bags ")[0]
		temp_BagRule = Bag(bagName)
		
		#sub bag rules
		line2 = line.split(" contain ")[1]
		subRule_input = line2.split(", ")
		for sRule in subRule_input:
			subBag = []
			if(sRule.find("no") == -1):
				subBag.append(sRule[0])
				subBag.append(sRule[2:].split(" bag")[0])
				temp_BagRule.subBags.append(subBag)
		Bags.append(temp_BagRule)
		temp_BagRule = None

def CountBags(bagToCheck, level):
	for bag in filter(lambda x: x.bag == bagToCheck, Bags):
		for subBag in bag.subBags
			factor = subBag[0]
			
			

def CheckIfBagIsContained(searchQuery, bagToCheck, level):
	flag = False
	for bag in filter(lambda x: x.bag == bagToCheck, Bags):
		for subBag in bag.subBags:
			
			#debug output
			output = ""
			for i in range(level):
				if (i == (level - 1)):
					output += "|->\t"
				else:
					output +="\t"
			output += str(level) + " " + subBag
			print(output)
			
			if(subBag == searchQuery):
				flag = True
			else:
				flag = (flag or CheckIfBagIsContained(searchQuery, subBag, (level + 1)))
	return flag

Bags = []
counter = 0
InputBags()
# containFlag = False

	
for bag in Bags:
	print(bag)
	# print("0 " + bag.bag)
	# containFlag = False
	# containFlag = CheckIfBagIsContained("shiny gold", bag.bag, 1)
	# if (containFlag):
		# counter += 1

# print(counter)
