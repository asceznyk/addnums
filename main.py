
def add(numbers:str) -> int:
  '''
  the function returns the sum of the numbers in input
  numbers: is a string of POSITIVE numbers in the following format
  "//[delimiter]\n[numbers..]" seperated by the
  specified delimiter and newline
  '''
  if numbers == '':
    return 0
  if len(numbers) == 1:
    return int(numbers[0])
  ans = 0
  delimiter = ','
  if numbers[:2] == '//':
    delimiter = numbers[2]
    numbers = numbers[3:]
  numbers = numbers.replace(delimiter, "\n")
  pnums = numbers.split('\n')
  negs = []
  for x in pnums: 
    if x == '': continue
    x = int(x)
    if x < 0:
      negs.append(x)
  if len(negs) > 0:
    raise Exception(f"negative numbers not allowed {','.join([str(x) for x in negs])}")
  for x in pnums:
    if x == '': continue
    if delimiter not in x:
      ans += int(x)
      continue
    for y in x.split(delimiter):
      ans += int(y)
  return ans
    

