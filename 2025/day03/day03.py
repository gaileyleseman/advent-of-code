import re 

def parse_text(input_txt):
    with open(input_txt, "r") as f:
        return f.read().split('\n')
        

def solve(data):
    parts = (2, 12)
    for part, n_batteries in enumerate(parts):
        solution = []

        for bank in data:
            joltage = ""
            remaining_batteries = n_batteries
            i = 9
            min_index = 0

            while remaining_batteries > 0:
                sub_bank = bank[min_index:]
                if not re.findall(str(i), sub_bank):
                    i -= 1
                    continue
                for n in re.finditer(str(i), sub_bank):
                    remaining_space = len(sub_bank) - n.span()[0]
                    if remaining_space < remaining_batteries:
                        i -= 1
                        break
                    joltage += n.group()
                    remaining_batteries = n_batteries - len(joltage)
                    min_index += n.span()[1] # .span() position  is relative to sub_bank! 
                    i = 9
                    break
            solution.append(int(joltage[:n_batteries]))

        print(f"part{part+1} ({n_batteries} batteries) = {sum(solution)}")


if __name__ == "__main__":
    print("TEST")
    solve(parse_text("test.txt"))

    print("INPUT")
    solve(parse_text("input.txt"))
