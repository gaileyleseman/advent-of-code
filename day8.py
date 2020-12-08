code = open('input/day8_input.txt', "r").read().split('\n')

# Part 1 -------------------------------------------------#
checked_lines = []
acc = 0
i = 0

while i < (len(code)-1):
    if i in checked_lines:
        print("Final accumulator value before infinite loop:", acc)
        break
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
