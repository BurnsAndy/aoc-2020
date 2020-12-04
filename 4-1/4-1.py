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
	
for line in passport_inputs:
	if line == "":
		#end of this passport, eval for validity
		segments = passport.split(":")
		for i in range(0, (len(segments) - 1)):
				#print(segments[i][-3:])
				if(segments[i][-3:] == "byr"):
					byr_flag = True
				if(segments[i][-3:] == "iyr"):
					iyr_flag = True
				if(segments[i][-3:] == "eyr"):
					eyr_flag = True
				if(segments[i][-3:] == "hgt"):
					hgt_flag = True
				if(segments[i][-3:] == "hcl"):
					hcl_flag = True
				if(segments[i][-3:] == "ecl"):
					ecl_flag = True
				if(segments[i][-3:] == "pid"):
					pid_flag = True
		#print(segments)
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
		passport += (" " + line)

print(valid_passports)
