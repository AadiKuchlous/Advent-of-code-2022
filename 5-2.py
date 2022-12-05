class stack:
  def __init__(self, arr):
    self.data = arr
    self.length = len(arr)

  def load(self, data):
    for val in data:
      self.data.append(val)
    return(self.data)

  def unload(self, num):
    end_index = num*-1
    removed_data = self.data[end_index::]
    self.data = self.data[0:end_index]
    return([self.data, removed_data])


stack_indices = [1, 5, 9, 13, 17, 21, 25, 29, 33]
# stack_indices = [1, 5, 9] for testcase

input_file = open("input5.txt", "r")

stack_data = []
move_data = []

for i in range(9):
  new_stack = stack([])
  stack_data.append(new_stack)

for line in input_file:
  if line.strip() == "":
    continue

  if line[0] == "m":
    line_split = line.strip().split(" ")
    num_to_move = int(line_split[1])
    move_from = int(line_split[3])
    move_to = int(line_split[5])

    move_data.append([num_to_move, move_from, move_to])

  elif line[1] != "1":
    for stack_no in range(len(stack_indices)):
      index = stack_indices[stack_no]
      val = line[index]
      if val != " ":
        stack_data[stack_no].load([val])


for stack in stack_data:
  stack.data.reverse()

for move in move_data:
  [num_to_move, move_from, move_to] = move
  [new, removed] = stack_data[move_from-1].unload(num_to_move)
  stack_data[move_to-1].load(removed)

final_string = ""
for stack in stack_data:
  final_string += stack.data[-1]

print(final_string)

