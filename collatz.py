
def even(x):
  return int(x/2)

def odd(x):
  return 3 * x + 1

def step(x):
  if x % 2 == 0:
    return even(x)
  else:
    return odd(x)

def number(x,m):
  cn=0
  if x in m:
    return m[x]
  else:
    r = x
    while r != 1:
      r=step(r)     
      cn = cn + 1
    m[x] = cn
    return cn

def cn(end):
  memo = {}
  for x in range(1,end):
    if x % int(end/10) == 0:
      print(str(x) + " " + str(number(x,memo)))

cn(1000000000)
