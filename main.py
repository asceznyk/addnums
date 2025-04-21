
def add(numbers:str) -> int:
  '''
  the function returns the sum of the numbers in input
  numbers: is a string of comma seperated numbers
  '''
  ans = 0
  for x in numbers.split(','):
    if x == '': continue
    ans += int(x)
  return ans

