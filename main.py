
def add(numbers:str) -> int:
  '''
  the function returns the sum of the numbers in input
  numbers: is a string of POSITIVE numbers in the following format
  "//[delimiter]\n[numbers..]" seperated by the
  specified delimiter and newline
  '''
  try:
    if numbers == '': return 0
    ans = 0
    pnums = numbers.split('\n')
    start = pnums[0]
    delimiter = ','
    if start[0] == '/':
      delimiter = pnums[0][2]
      pnums = pnums[1:]
    for x in pnums:
      if x == '': continue
      if delimiter in x:
        ans += sum([int(y) for y in x.split(delimiter)])
        continue
      ans += int(x)
    return ans
  except:
    pass
    return -1
    

