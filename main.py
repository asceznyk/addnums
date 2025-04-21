from typing import List, Tuple

def handle_delimiter(numbers:str) -> Tuple[List[str],int]:
  i = 2
  delimiters = []
  if numbers[i] != '[':
    return [numbers[i]], i
  while numbers[i] != '\n':
    if numbers[i] == '[':
      d = ''
      i += 1
      while numbers[i] != ']':
        d += numbers[i]
        i += 1
      delimiters.append(d)
      i += 1
  return delimiters, i 

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
  delimiters = [',']
  if numbers[:2] == '//':
    delimiters, i = handle_delimiter(numbers)
    numbers = numbers[(i+1):]
  for d in delimiters:
    numbers = numbers.replace(d, "\n")
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
    x = int(x)
    if x > 1000: continue
    ans += x
  return ans
    

