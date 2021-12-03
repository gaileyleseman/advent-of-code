import re


def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n\n')
    return data

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
ecl_options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_fields(passport, req_fields):
    for req_field in req_fields:
        if passport.find(req_field) < 0:
            return True  # required field missing


def check_field_validity(field):
    code = field[0:3]  # three letter code
    data = field[4:]  # everything after :
    if code == 'cid':
        return True
    elif code == 'byr':
        return 1920 <= int(data) <= 2002
    elif code == 'iyr':
        return 2010 <= int(data) <= 2020
    elif code == 'eyr':
        return 2020 <= int(data) <= 2030
    elif code == 'hgt':
        hgt = re.findall(r'\d+', data)  # find all decimals
        if data[-2:] == 'cm':
            return 150 <= int(hgt[0]) <= 193
        elif data[-2:] == 'in':
            return 59 <= int(hgt[0]) <= 76
        else:
            return False
    elif code == 'hcl':
        return re.search('^#(?:[0-9a-f]{6})$', data)  # check hex color validity
    elif code == 'ecl':
        try:
            return ecl_options.index(data) >= 0
        except:
            return False
    elif code == 'pid':
        return re.search('^(?:[0-9]{9})$', data)
    else:
        return False


def part1(input_txt):
    passports = parse_text(input_txt)
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    not_valid = 0

    for passport in passports:
        for field in req_fields:
            if passport.find(field) < 0:
                not_valid += 1
                break

    valid = len(passports) - not_valid
    return valid


def part2(input_txt):
    passports = parse_text(input_txt)
    valid = 0
    i = 0
    for passport in passports:
        i += 1
        if check_fields(passport, req_fields):  # check for required fields
            continue
        else:
            fields = re.split('\n| ', passport)  # split passport fields
            for field in fields:
                if not check_field_validity(field):  # check validity
                    # print(' || Field not valid: ', field)
                    break
            else:
                valid += 1
    return valid


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
