import math

inVal = input()
C = 50
H = 30
li_rsl = []
try:
  nums = inVal.split(',')
  for i in nums:
    int(i)
except:
  print("Please enter numbers in the format of 1,2,3")
else:
  for i in nums:
    D = float(i)
    Q = math.sqrt((2 * C * D)/H)
    li_rsl.append(round(Q))

  
  str_comma=""
  for rsl in li_rsl:
      print (str_comma,rsl,sep="",end="")
      str_comma="," 
