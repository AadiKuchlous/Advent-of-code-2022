import copy

input_file = open("input7.txt", "r")

def add_path(path, cur_dir):
  next_dir_name = path[0]
  if next_dir_name in cur_dir:
    next_dir = cur_dir[next_dir_name]

    dir_rest = copy.deepcopy(cur_dir)
    dir_rest.pop(next_dir_name)

    return({**{next_dir_name: add_path(path[1::], next_dir)}, **dir_rest})

  else:
    return({**{next_dir_name: {'size': 0}}, **cur_dir})

def add_value(value, path, cur_dir):
  if len(path) > 1:
    next_dir_name = path[0]
    next_dir = cur_dir[next_dir_name]

    next_dir['size'] = next_dir['size'] + value

    dir_rest = copy.deepcopy(next_dir)
    dir_rest.pop(path[1])

    return( {next_dir_name: {**add_value(value, path[1::], next_dir), **dir_rest}} )

  elif len(path) == 1:
    next_dir_name = path[0]
    next_dir = cur_dir[next_dir_name]

    next_dir['size'] = next_dir['size'] + value

    dir_rest = cur_dir
    dir_rest.pop(path[0])

    return( {**{next_dir_name: add_value(value, path[1::], next_dir)}, **dir_rest} )
    

  elif len(path) == 0:
    return(cur_dir)


data = {}

cur_path = []

for line in input_file:
  line = line.strip().split(' ')

  if line[0] == "$":
    cmd_name = line[1]
    if cmd_name == "cd":
      if line[2] == "..":
        cur_path = cur_path[0:-1]
      else:
        cur_path.append(line[2])
        data = add_path(cur_path, data)

  elif line[0] == "dir":
    pass
  else:
    data = add_value(int(line[0]), cur_path, data)
    pass



min_size = 30000000 - (70000000 - data['/']['size'])
to_delete = [70000000];
print('min to delete', min_size)
def find_total(data):
  if len(data) == 1 and 'size' in data:
    print(data['size'])
    if data['size'] >= min_size and data['size'] < to_delete[0]:
      to_delete[0] = data['size']
    return
  else:
    data_copy = copy.deepcopy(data)
    for key in data_copy:
      if type(data_copy[key]) == type({}):
        find_total(data_copy[key])
      else:
        print(data['size'])
        if data['size'] > min_size and data['size'] < to_delete[0]:
          to_delete[0] = data['size']

find_total(data)
print(to_delete)
