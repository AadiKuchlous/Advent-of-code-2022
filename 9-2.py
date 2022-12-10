import copy

input_file = open("input9.txt", "r")

direction_vectors = {
  "D": (0, -1),
  "U": (0, 1),
  "L": (-1, 0),
  "R": (1, 0),
}

visited = {(0,0)}

current_pos = []

# Initialize current_pos for head and 10 knots
# as a series of 10 * [0, 0]
# Position 1 will be knot 1, position 2, knot 2 and so on

for i in range(10):
  current_pos.append([0, 0])



def displacement(pos1, pos2):
  disx = pos2[0] - pos1[0]
  disy = pos2[1] - pos1[1]
  return((disx, disy))



for line in input_file:
  [dir, num_steps] = line.strip().split(" ")

  print(current_pos)
  print(len(visited))
  for i in range(int(num_steps)):
    # print(dir, i)
    # Update the position of the head

    old_head_pos = copy.copy(current_pos[0])

    current_pos[0][0] += direction_vectors[dir][0]
    current_pos[0][1] += direction_vectors[dir][1]

    # Calculate displacement vector between head and body
    head_from_body = displacement(current_pos[0], current_pos[1])

    # If new head touching body, move on
    if (abs(head_from_body[0]) <= 1) and (abs(head_from_body[1]) <= 1):
      continue

    # If head moves away from body
    # The body should follow the head

    temp = copy.copy(current_pos[1])
    move = displacement(current_pos[1], old_head_pos)
    current_pos[1][0] += move[0]
    current_pos[1][1] += move[1]
    for node_number in range(2, 10):
      diff = displacement(current_pos[node_number], current_pos[node_number-1])

      if (abs(diff[0]) <= 1) and (abs(diff[1]) <= 1):
        break

      elif (abs(diff[0]) > 1) and (abs(diff[1]) > 1):
        current_pos[node_number][0] += int(diff[0]/2)
        current_pos[node_number][1] += int(diff[1]/2)

      elif (abs(diff[0]) > 1):
        current_pos[node_number][0] += int(diff[0]/2)
        current_pos[node_number][1] += diff[1]

      elif (abs(diff[1]) > 1):
        current_pos[node_number][0] += diff[0]
        current_pos[node_number][1] += int(diff[1]/2)

      else:
        move = displacement(current_pos[node_number], temp)
        temp = copy.copy(current_pos[node_number])
        current_pos[node_number][0] += move[0]
        current_pos[node_number][1] += move[1]


    # Update the nodes visited set
    visited.add(tuple(current_pos[-1]))
    # print(current_pos[-1], dir, i)



print(current_pos)
print(len(visited))
