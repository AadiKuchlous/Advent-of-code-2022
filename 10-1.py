input_file = open("input10.txt", "r")

register_vals = [1]

for line in input_file:
  if line[0] == "n":
    register_vals.append(register_vals[-1])
  else:
    increment = int(line.strip().split(" ")[1])

    register_vals.append(register_vals[-1])

    register_vals.append(register_vals[-1] + increment)


total = 0

for i in range(20, 221, 40):
  total += register_vals[i-1] * i

print(total)
