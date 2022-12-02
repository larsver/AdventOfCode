file = open("input.txt")

# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors


sum = 0

for l in file:
    score = 0
    print(l)
    help = l.split()
    print(help)
    match help[1]:
        case "X":
            score += 1 
        case "Y":
            score += 2 
        case "Z":
            score += 3

    if help[0] == help[1]:
        score += 3
    match help[1]:
        case "X":
            match help[0]:
                case "A":
                    score += 3
                case "B":
                    score += 0
                case "C":
                    score += 6
        case "Y":
            match help[0]:
                case "A":
                    score += 6
                case "B":
                    score += 3
                case "C":
                    score += 0
        case "Z":
            match help[0]:
                case "A":
                    score += 0
                case "B":
                    score += 6
                case "C":
                    score += 3
    sum += score

print(sum)
file.close()