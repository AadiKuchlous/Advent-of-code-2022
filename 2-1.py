game_rules = {
  "A": 1,
  "B": 2,
  "C": 3,
  "X": 1,
  "Y": 2,
  "Z": 3,
}

input_file = open("input2.txt", "r")

all_data = []

for line in input_file:
  all_data.append(line.strip().split(' '));

score = 0

for round in all_data:
  op_play = game_rules[round[0]]
  my_play = game_rules[round[1]]

  score += my_play

  if my_play == op_play:
    score += 3
  else:
    if (my_play - op_play == 1) or (my_play - op_play == -2):
      score += 6
    else:
      score += 0

print(score)
