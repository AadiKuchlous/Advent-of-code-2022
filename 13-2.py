import functools

input_file = open("input13.txt", "r")

all = [[[2]], [[6]]]


def checkOrder(signal_1, signal_2):
  print(signal_1, signal_2)

  index = 0

  if type(signal_1) == int and type(signal_2) == int: 
    return([signal_1 < signal_2, signal_1 == signal_2, True])

  elif type(signal_1) == list and type(signal_2) == int:
    return(checkOrder(signal_1, [signal_2]))

  elif type(signal_1) == int and type(signal_2) == list:
    return(checkOrder([signal_1], signal_2))

  in_order = True
  confirm = False
  while True:
    new_signal_1 = False
    new_signal_2 = False
    try:
      new_signal_1 = signal_1[index]
    except:
      pass
    try:
      new_signal_2 = signal_2[index]
    except:
      pass

    if not (type(new_signal_1) == bool) and not (type(new_signal_2) == bool):
      
      recurse = checkOrder(new_signal_1, new_signal_2)
      if recurse[2] == True:
        less = recurse[0]
        equal = recurse[1]
        print([less, equal])
        in_order = less or equal
        if less:
          confirm = True
          break
        if not less and not equal:
          print("Not less and not equal")
          in_order = False
          confirm = True
          break
      else:
        confirmed = recurse[0]
        if confirmed:
          confirm = True
          in_order = recurse[1]
          break
        
        
    elif (type(new_signal_1) == bool and type(new_signal_2) != bool):
      in_order = True
      confirm = True
      break
    elif (type(new_signal_1) != bool and type(new_signal_2) == bool):
      in_order = False
      confirm = True
      break
    else:
      break

    print(in_order)

    if not in_order:
      print("Found not in order")
      confirm = True
      break

    index += 1

  return([confirm, in_order, False])



def customSort(signal_1, signal_2):
  [confirm, in_order, base_case] = checkOrder(signal_1, signal_2)

  if in_order:
    return(-1)
  else:
    return(1)



for line in input_file:
  print(line)
  if line.strip() == "":
    continue
  all.append(eval(line.strip()))

all.sort(key=functools.cmp_to_key(customSort))

print((all.index([[2]]) + 1) * (all.index([[6]]) + 1))
