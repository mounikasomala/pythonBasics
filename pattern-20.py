n=int(input())
def print_pattern(n):
    for i in range(1,n+1):
        if i%2==0:
            print("@" * i)
        else:
            print(str(i)*i)
print_pattern(n)


# output
# 1
# @@
# 333
# @@@@
# 55555
# @@@@@@
