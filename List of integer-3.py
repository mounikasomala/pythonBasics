# 3. Write a python program to accept a list of
#     integers and print total count of negative
#     numbers in the list 
 
# solution
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele < 0:
        result = result + 1 
print(result)
 
# input
# 1 2 -3 4 5 6 -7 8 9 10 -15
# output
# 3
