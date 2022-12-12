input_file = open("input1.txt", "r")

all_data = []

for line in input_file:
  all_data.append(line.strip())


highest = [0, 0, 0]

current_high = 0

for data in all_data:
  if data == '':
    if current_high > highest[0]:
      highest[2] = highest[1]
      highest[1] = highest[0]
      highest[0] = current_high
    elif current_high > highest[1]:
      highest[2] = highest[1]
      highest[1] = current_high
    elif current_high > highest[2]:
      highest[2] = current_high
    current_high = 0
  else:
    current_high += int(data)

print(highest[0] + highest[1] + highest[2])
