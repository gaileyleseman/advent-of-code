passports = open('day4_input.txt', "r").read().split('\n\n')

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
not_valid = 0

for passport in passports:
    for field in req_fields:
        if passport.find(field) < 0:
            not_valid += 1
            break

valid = len(passports) - not_valid
print(valid)