input_file = open("input4.txt", "r")

all_data = []

for line in input_file:
  line = line.strip()
  line = line.split(",")
  line_array = []
  for area in line:
    area = area.split("-")
    area_array = []
    area_array.append(int(area[0]))
    area_array.append(int(area[1]))
    line_array.append(area_array)
  all_data.append(line_array)


count = 0

for line in all_data:
  area1 = line[0]
  area2 = line[1]

  if area1[0] <= area2[1] and area1[0] >= area2[0]:
    count += 1
    print(area1, area2)
  elif area1[1] >= area2[0] and area1[1] <= area2[1]:
    count += 1
    print(area1, area2)
  elif area2[0] <= area1[1] and area2[0] >= area1[0]:
    count += 1
    print(area1, area2)

print(count)

