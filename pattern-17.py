n = int(input())
for i in range(1, n + 1):
   val1 = i
   val2 = 1
   for j in range(i):
       if i % 2 == 0:
           print(val1, end = " ")
           val1 = val1-1
       else:
           print(val2, end = " ")
           val2 =val2 + 1
   print()

# output
# 1
# 2 1
# 1 2 3
# 4 3 2 1
# 1 2 3 4 5
