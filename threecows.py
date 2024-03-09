def solulu(positions):
  o = []

  def maxmoves(pos1, pos2, pos3):
      # find the max
      lst = [pos2 - pos1, pos3 - pos2]
      max_diff = max(lst)
      maxmoves = max_diff - 1
      return maxmoves

  if (positions[0] + 2) == positions[1] or (positions[1] + 2) == positions[2]:
      o.append(1)
  else:
      o.append(2)

  o.append(maxmoves(positions[0], positions[1], positions[2]))

  return o

with open('herding.in', 'r') as f:
  positions = list(map(int, f.readline().split()))

tmo = positions[1] - positions[0]
thmt = positions[2] - positions[1]

if (positions[0] + 1) == positions[1] and positions[1] == (positions[2] - 1):
  with open('herding.out', 'w') as f:
      f.write('0\n')
else:
  out = solulu(positions)
  with open('herding.out', 'w') as f:
      for o in out:
          f.write(str(o) + '\n')
