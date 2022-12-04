input_file = open("input3.txt", "r")

all_data = []

for line in input_file:
  line = line.strip()
  half_length = int(len(line)/2)
  part_1 = set(list(line[0:half_length]))
  part_2 = set(list(line[half_length::]))
  all_data.append([part_1, part_2])


total = 0

for line in all_data:
  part_1 = line[0]
  for letter in part_1:
    if letter in line[1]:
      if letter.isupper():
        total += ord(letter) - 38
      else:
        total += ord(letter) - 96

print(total)
