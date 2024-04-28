# 5. Write a python program to accept a list of
#     integers and print sum of 2nd greatest 
#      element and 2nd smallest element from list

#  solution
n=int(input()) 
nums = list(map(int, input().split()))
result = 0 
nums = sorted(nums)
result = nums[1] + nums[n - 2]
print(result)

# Input
# 4
# 12 3 56 78
# Output
# [3, 12, 56, 78]
# 68
