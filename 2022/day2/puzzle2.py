file = open("input.txt")

# A for Rock, B for Paper, and C for Scissors.
# X for lose, Y for draw, and Z for win


sum = 0

for l in file:
    score = 0
    print(l)
    help = l.split()
    print(help)


    match help[1]:
        case "X": #lose
            score += 0
        case "Y": #draw
            score += 3
        case "Z": #win
            score += 6

    # bepalen welke keuze zelf
    choose = ""
    match help[0]:
        case "A":
            match help[1]:
                case "X":
                    choose = "C"
                case "Y":
                    choose = "A"
                case "Z":
                    choose = "B"

        case "B":
             match help[1]:
                case "X":
                    choose = "A"
                case "Y":
                    choose = "B"
                case "Z":
                    choose = "C"
        case "C":
             match help[1]:
                case "X":
                    choose = "B"
                case "Y":
                    choose = "C"
                case "Z":
                    choose = "A"
    # punten per keuze A(steen)=1, B(Blad)=2 and C(schaar)=3
    match choose:
        case "A":
            score += 1 
        case "B":
            score += 2 
        case "C":
            score += 3
    sum += score

print(sum)
file.close()