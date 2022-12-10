input_file = open("input9.txt", "r")

direction_vectors = {
  "D": (0, -1),
  "U": (0, 1),
  "L": (-1, 0),
  "R": (1, 0),
}

visited = {(0,0)}

current_tail_pos = [0, 0]
head_from_tail = [0, 0]


def updateHeadPosStraight(dir):
  head_from_tail[0] = direction_vectors[dir][0]
  head_from_tail[1] = direction_vectors[dir][1]


def updateHeadPosDiagonal(dir):
  head_from_tail[0] += direction_vectors[dir][0]
  head_from_tail[1] += direction_vectors[dir][1]


def updateTailPos():
  current_tail_pos[0] += head_from_tail[0]
  current_tail_pos[1] += head_from_tail[1]


for line in input_file:
  [dir, num_steps] = line.strip().split(" ")

  for i in range(int(num_steps)):
    # print(dir, i)
    # print(current_tail_pos, head_from_tail)

    # print(head_from_tail[0] + direction_vectors[dir][0], head_from_tail[1] + direction_vectors[dir][1])

    # If the head moves to a position where it is touching
    # Just update the head_from_tail and move on

    if (abs(head_from_tail[0] + direction_vectors[dir][0]) <= 1) and (abs(head_from_tail[1] + direction_vectors[dir][1]) <= 1):
      # print("skipped")

      # Check if head will overlap with tail after this move

      if (abs(head_from_tail[0] + direction_vectors[dir][0]) == 0) and (abs(head_from_tail[1] + direction_vectors[dir][1]) == 0):
        head_from_tail = [0, 0]

      # Check if head will be at a diagonal from tail after this move

      elif (abs(head_from_tail[0] + direction_vectors[dir][0]) == 1) and (abs(head_from_tail[1] + direction_vectors[dir][1]) == 1):
        # print("Is Diagonal")
        updateHeadPosDiagonal(dir)

      # Head is in U, D, L or R from tail after this move

      else:
        updateHeadPosDiagonal(dir)

    # Case where head moves away from tail
    # Move the tail position
    # Update the head_from_tail variable

    else:
      updateTailPos()

      visited.add(tuple(current_tail_pos))

      updateHeadPosStraight(dir)

print('\n'*2)
print(visited)
print('\n'*2)
print(len(visited))
