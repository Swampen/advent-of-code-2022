def get_input(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
        return [line.split() for line in lines]


def second_star(rounds):
    totalScore = 0
    for round in rounds:
        opponentMove = round[0]
        outcome = round[1]
        if outcome == "X":
            if opponentMove == "A":
                totalScore += get_score(round[0], "Z")
            if opponentMove == "B":
                totalScore += get_score(round[0], "X")
            if opponentMove == "C":
                totalScore += get_score(round[0], "Y")
        elif outcome == "Y":
            if opponentMove == "A":
                totalScore += get_score(round[0], "X")
            if opponentMove == "B":
                totalScore += get_score(round[0], "Y")
            if opponentMove == "C":
                totalScore += get_score(round[0], "Z")
        elif outcome == "Z":
            if opponentMove == "A":
                totalScore += get_score(round[0], "Y")
            if opponentMove == "B":
                totalScore += get_score(round[0], "Z")
            if opponentMove == "C":
                totalScore += get_score(round[0], "X")

    return totalScore


def first_star(rounds):
    totalScore = 0
    for round in rounds:
        totalScore += get_score(round[0], round[1])

    return totalScore


def get_score(move1, move2):
    score = 0
    if move2 == "X":
        score += 1
        if move1 == "C":
            score += 6
        elif move1 == "A":
            score += 3
    elif move2 == "Y":
        score += 2
        if move1 == "A":
            score += 6
        elif move1 == "B":
            score += 3
    elif move2 == "Z":
        score += 3
        if move1 == "B":
            score += 6
        elif move1 == "C":
            score += 3
    return score


if __name__ == "__main__":
    problem = get_input('input.txt')
    print("First star:", first_star(problem))
    print("Second star:", second_star(problem))
