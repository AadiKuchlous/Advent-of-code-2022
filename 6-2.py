input_file = open("input6.txt", "r")

data = ""

for line in input_file:
  data = line.strip()

for i in range(len(data)-14):
  chars = []
  for x in range(i, i+14):
    chars.append(data[x])
  if len(set(chars)) == 14:
    print(i+14)
    break
