#import sys

liData = ['Boss', 'Apple', 'Tree', 'Sea']
liData.sort()

indata = input()
if indata in liData:
  idata = liData.index(indata)
  print("Yes, '" + indata + "' found in List : ", idata)
else:
  print("No, Specific data '" + indata + "' not found in the List")