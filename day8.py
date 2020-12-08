code = open('input/day8_input.txt', "r").read().split('\n')

# Part 1 -------------------------------------------------#

def checkInfinite(code):
    checked_lines = []
    acc = 0
    i = 0
    while i < (len(code)-1):
        if i in checked_lines:
            # print("Final accumulator value before infinite loop:", acc)
            return True
        else:
            checked_lines.append(i)
            [cmd, arg] = code[i].split(' ')
            if cmd == "acc":
                acc += int(arg)
                i += 1
            elif cmd == "jmp":
                i += int(arg)
            elif cmd == "nop":
                i += 1
            else:
                print("unknown command")
                break
    print("Final accumulator value before terminating:", acc)
    return False

checkInfinite(code)

# Part 2 -------------------------------------------------#

for j in range(0, len(code)-1):
    alt_code = code.copy()
    [cmd, arg] = alt_code[j].split(' ')
    if cmd == "acc":
        pass
    elif cmd == "jmp":
        alt_code[j] = "nop " + arg
    elif cmd == "nop":
        alt_code[j] = "jmp " + arg
    else:
        print("unknown command")
        break
    if checkInfinite(alt_code):
        j += 1