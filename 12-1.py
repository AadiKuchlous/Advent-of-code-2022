input_file = open("input12.txt", "r")

grid = []

start = []
end = []

visited = set()

for line in input_file:
  line = list(line.strip())
  for i in range(len(line)):
    if line[i] == "S":
      start = [i, len(grid)]
      line[i] = "a"
    if line[i] == "E":
      end = [i, len(grid)]
      line[i] = "z"

  grid.append(line)


def getNeighbors(pos):
  x = 0
  y = 1
  valid = []
  if pos[x] > 0:
    if not((pos[x]-1, pos[y]) in visited):
      valid.append([pos[x]-1, pos[y]])
  if pos[y] > 0:
    if not((pos[x], pos[y]-1) in visited):
      valid.append([pos[x], pos[y]-1])
  if pos[x] < len(grid[0]) - 1:
    if not((pos[x]+1, pos[y]) in visited):
      valid.append([pos[x]+1, pos[y]])
  if pos[y] < len(grid) - 1:
    if not((pos[x], pos[y]+1) in visited):
      valid.append([pos[x], pos[y]+1])
  return(valid)


queue = [[start, 0]]

while True:
  pos = queue[0][0]
  depth = queue[0][1]
  this_value = ord(grid[pos[1]][pos[0]])

  found = False

  for neighbor in getNeighbors(pos):
    neighbor_value = ord(grid[neighbor[1]][neighbor[0]])
    if neighbor_value - this_value > 1:
      continue

    if neighbor == end:
      print(depth+1)
      found = True
      break
    else:
      queue.append([neighbor, depth+1])
      visited.add(tuple(neighbor))

  if found:
    break

  queue = queue[1::]
