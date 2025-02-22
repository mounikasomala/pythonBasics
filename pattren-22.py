# using for loop
n=int(input())
v=1
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(v,end=" ")
            v=v+1
    print()

# using while loop

n=int(input())
v=1
i=0
while i<n:
    j=0
    while j<n:
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(v,end=" ")
            v=v+1
        j=j+1
    print()
    i=i+1
# output
# * * * * 
# * 1 2 * 
# * 3 4 * 
# * * * * 
