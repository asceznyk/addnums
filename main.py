
def add(numbers:str) -> int:
  '''
  the function returns the sum of the numbers in input
  numbers: is a string of numbers seperated by comma and newline
  '''
  ans = 0
  pnums = numbers.split('\n')
  for x in pnums:
    if x == '': continue
    if ',' in x:
      ans += sum([int(y) for y in x.split(',')])
      continue
    ans += int(x)
  return ans

