input_file = open("input8.txt", "r")

all_data = []

for line in input_file:
  all_data.append(list(line.strip()))

def tree_score(x, y, data):
  height = data[y][x]

  # check up
  score_up = 0
  if y != 0:
    for y_to_check in range(y-1, -1, -1):
      score_up += 1
      if data[y_to_check][x] >= height:
        break

  # check down
  score_down = 0
  for y_to_check in range(y+1, len(data)):
    score_down += 1
    if data[y_to_check][x] >= height:
      break

  # check left
  score_left = 0
  if x != 0:
    for x_to_check in range(x-1, -1, -1):
      score_left += 1
      if data[y][x_to_check] >= height:
        break

  # check right
  score_right = 0
  for x_to_check in range(x+1, len(data[0])):
    score_right += 1
    if data[y][x_to_check] >= height:
      break

  total_score = score_up * score_down * score_left * score_right

  return(total_score)


highest = 0

for y in range(len(all_data)):
  for x in range(len(all_data[0])):
    score = tree_score(x, y, all_data)
    if score > highest:
      highest = score

print(highest)
