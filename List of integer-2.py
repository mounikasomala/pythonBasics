# 2. Write a python program to accept a list of 
#     integers and print the total count of numbers 
#     which are divisible by 5 
 
# solution:    
nums = list(map(int, input().split()))
result = 0 
for ele in nums:
    if ele % 5 == 0:
        result = result + 1 
print(result)

# input
# 1 2 3 4 5 6 7 8 9 10
# output
# 2
