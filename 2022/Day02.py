with open("Day02Input.txt") as file:
    games = file.read()

rps = games.split("\n")

# The winner of the whole tournament is the player with the highest score.
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

scores_dict1 = {"A X": 4,
                "A Y": 8,
                "A Z": 3,
                "B X": 1,
                "B Y": 5,
                "B Z": 9,
                "C X": 7,
                "C Y": 2,
                "C Z": 6,
}

scores_dict2 = {"A X": 3,
                "A Y": 4,
                "A Z": 8,
                "B X": 1,
                "B Y": 5,
                "B Z": 9,
                "C X": 2,
                "C Y": 6,
                "C Z": 7,
}

total1 = 0
total2 = 0

for each in rps:
    total1 += scores_dict1[each]
    total2 += scores_dict2[each]

print(total1)
print(total2)