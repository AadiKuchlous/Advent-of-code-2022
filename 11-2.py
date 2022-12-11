input_file = open("input11.txt", "r")

moves = []

this_move = []
for line in input_file:
  line = line.strip()

  if line == "":
    moves.append(this_move)
    this_move = []
  else:
    this_move.append(line)

all_items = [[] for i in range(len(moves))]
comparisons = [0 for i in range(len(moves))]

supermodulo = 1

for index in range(len(moves)):
  monkey = moves[index]
  items = list(map(lambda x: int(x), monkey[1].split(": ")[1].split(", ")))
  all_items[index] = all_items[index] + items

  div = int(monkey[3].split()[-1])
  supermodulo *= div


def oneCycle():
  for monkey in moves:
    index = int(monkey[0].split()[1][0:-1])

    operation = monkey[2].split("= ")[1]

    div = int(monkey[3].split()[-1])
    yes = int(monkey[4].split()[-1])
    no = int(monkey[5].split()[-1])

    for item in all_items[index]:
      comparisons[index] += 1
      old = item % supermodulo
      new = eval(operation)
      # print(new, div)
      if new % div == 0:
        all_items[yes].append(new)
      else:
        all_items[no].append(new)

    all_items[index] = []


for i in range(10000):
  oneCycle()

comparisons = sorted(comparisons)
print(comparisons[-1] * comparisons[-2])
