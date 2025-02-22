characters = input()

for i in range(len(characters)):
    for j in range(i, len(characters)):
        print(characters[i:j+1], end=" ")
    print()

# output
# abcd
# a ab abc abcd 
# b bc bcd
# c cd
# d
