n=int(input())
v=1
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(i):
        print(v,end=" ")
        v=v+1
    print()

#output
    1 
   2 3 
  4 5 6 
 7 8 9 10 
