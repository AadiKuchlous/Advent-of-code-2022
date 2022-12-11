input_file = open("input10.txt", "r")

register_vals = [1]

for line in input_file:
  if line[0] == "n":
    register_vals.append(register_vals[-1])
  else:
    increment = int(line.strip().split(" ")[1])

    register_vals.append(register_vals[-1])

    register_vals.append(register_vals[-1] + increment)


sprite = []
screen = [[] for i in range(6)]
cycle = 1


def draw():
  row_number = (cycle-1)//40

  print(cycle, row_number, sprite)

  if (cycle-1)%40 in sprite:
    screen[row_number].append('#')
  else:
    screen[row_number].append('.')



print(len(register_vals))

for i in range(len(register_vals)-1):
  sprite = [register_vals[i]-1, register_vals[i], register_vals[i]+1]
  draw()
  cycle += 1


for line in screen:
  print(''.join(line))

