input_file = open("input6.txt", "r")

data = ""

for line in input_file:
  data = line.strip()

for i in range(len(data)-4):
  chars = []
  for x in range(i, i+4):
    chars.append(data[x])
  if len(set(chars)) == 4:
    print(i+4)
    break
