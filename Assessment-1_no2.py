
str_comma=""
for n in range(2000, 3201):
      if n % 7 == 0 and n % 5 != 0:
        print(str_comma,n,sep="",end="")
        str_comma="," 