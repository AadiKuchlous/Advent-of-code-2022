input_file = open("input8.txt", "r")

all_data = []

for line in input_file:
  all_data.append(list(line.strip()))

total = (len(all_data) + (len(all_data[0]) - 2)) * 2

def is_visible(x, y, data):
  height = data[y][x]

  # check up
  visible = True
  for y_to_check in range(y):
    if data[y_to_check][x] >= height:
      visible = False
      break
  if visible == True:
    print(height, x, y, "visible up")
    return(True)

  # check down
  visible = True
  for y_to_check in range(y+1, len(data)):
    if data[y_to_check][x] >= height:
      visible = False
      break
  if visible == True:
    print(height, x, y, "visible down")
    return(True)

  # check left
  visible = True
  for x_to_check in range(x):
    if data[y][x_to_check] >= height:
      visible = False
      break
  if visible == True:
    print(height, x, y, "visible left")
    return(True)

  # check right
  visible = True
  for x_to_check in range(x+1, len(data[0])):
    if data[y][x_to_check] >= height:
      visible = False
      break
  if visible == True:
    print(height, x, y, "visible right")
    return(True)

  return(False)


for y in range(1, (len(all_data) - 1)):
  for x in range(1, (len(all_data[0]) - 1)):
    if is_visible(x, y, all_data):
      total += 1

print(total)
