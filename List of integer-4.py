# 4. Write a python program to accept a list of 
#     integers and print the average of these 
#     numbers 

# solution
nums = list(map(int, input().split()))
#temp = sum(nums)
sumOfElements = 0 
for ele in nums:
    sumOfElements = sumOfElements + ele 
print(sumOfElements // len(nums))

# input
# 1 2 3 4 5 6 7 8 9 10
# output
# 5
