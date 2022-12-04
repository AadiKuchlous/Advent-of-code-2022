input_file = open("input3.txt", "r")

all_data = [[]]
current_set = 0

for line in input_file:
  line = line.strip()
  line = set(list(line))
  if len(all_data[current_set]) == 3:
    all_data.append([])
    current_set += 1
  all_data[current_set].append(line)


total = 0

for line in all_data:
  part_1 = line[0]
  for letter in part_1:
    if letter in line[1] and letter in line[2]:
      if letter.isupper():
        total += ord(letter) - 38
      else:
        total += ord(letter) - 96

print(total)

