play_points = {
  "A": 1,
  "B": 2,
  "C": 3,
}

outcomes = {
  "X": 0,
  "Y": 3,
  "Z": 6,
}

input_file = open("input2.txt", "r")

all_data = []

for line in input_file:
  all_data.append(line.strip().split(' '));

score = 0

for round in all_data:
  op_play = play_points[round[0]]
  outcome = round[1]

  score += outcomes[outcome]

  if outcome == "Y":
    score += op_play
  if outcome == "X":
    if op_play == 1:
      score += 3
    else:
      score += op_play-1
  if outcome == "Z":
    if op_play == 3:
      score += 1
    else:
      score += op_play+1

print(score)
