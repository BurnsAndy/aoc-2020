import re
#Get info from file
with open("input.txt", "r") as file:
	passport_inputs = [line.strip() for line in file]
passport_inputs.append("")
passport = ""
byr_flag = False
iyr_flag = False
eyr_flag = False
hgt_flag = False
hcl_flag = False
ecl_flag = False
pid_flag = False
valid_passports = 0
pattern = re.compile("[a-f0-9]+")
	
for line in passport_inputs:
	if line == "":
		#end of this passport, eval for validity
		segments = passport.split(" ")
		for item in segments:
			data = item.split(":")
			if(data[0] == "byr" and (int(data[1]) >= 1920 and int(data[1]) <= 2002)):
				byr_flag = True
			if(data[0] == "iyr" and (int(data[1]) >= 2010 and int(data[1]) <= 2020)):
				iyr_flag = True
			if(data[0] == "eyr" and (int(data[1]) >= 2020 and int(data[1]) <= 2030)):
				eyr_flag = True
			if(data[0] == "hgt"):
				if(data[1][-2:] == "cm" and (int(data[1][:-2]) >= 150 and int(data[1][:-2]) <= 193)):
					hgt_flag = True
				if(data[1][-2:] == "in" and (int(data[1][:-2]) >= 59 and int(data[1][:-2]) <= 76)):
					hgt_flag = True
			if(data[0] == "hcl" and data[1][0] == '#' and (pattern.fullmatch(str(data[1][1:])) is not None)):
				hcl_flag = True
			if(data[0] == "ecl"):
				if(data[1] == "amb" or data[1] == "blu" or data[1] == "brn" or data[1] == "gry" or data[1] == "grn" or data[1] == "hzl" or data[1] == "oth"):    
					ecl_flag = True
			if(data[0] == "pid" and len(data[1]) == 9):
				pid_flag = True

		#validate
		if(byr_flag and iyr_flag and eyr_flag and hgt_flag and hcl_flag and ecl_flag and pid_flag):
					valid_passports += 1
		#reset
		byr_flag = False
		iyr_flag = False
		eyr_flag = False
		hgt_flag = False
		hcl_flag = False
		ecl_flag = False
		pid_flag = False
		passport = ""
	else:
		#passport continues
		passport += (line + " ")

print(valid_passports)
