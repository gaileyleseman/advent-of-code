input = open('input/day6_input.txt', "r").read().split('\n\n')

# Part 1
n_total = 0
for group in input:
    questions = set(group)
    if '\n' in questions:
        questions.remove('\n')
    n_total += len(questions)
print("Answered at least once: ", n_total)

# Part 2
n_total = 0
for group in input:
    n_persons = len(group.split('\n'))
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        n_answered = group.count(letter)
        if n_answered == n_persons:
            n_total += 1

print("Answered by all persons in group: ", n_total)
