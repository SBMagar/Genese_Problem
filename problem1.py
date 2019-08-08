def get_sum():
  sum = 0
  for NUM in range(1, 10):
    if NUM % 3 == 0 or NUM % 5 == 0:
      sum += NUM
  return sum