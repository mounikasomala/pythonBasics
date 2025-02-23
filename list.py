animal_len=[len(animal)
            for animal in ["dog", "cat", "elephant", "giraffe", "rhinoceros"]
            if len(animal) > 3]
print(animal_len)

def count_char(string,char):
    count=0
    for i in string:
        if i==char:
            count+=1
    return count
print(count_char("elephant","e"))


def concatenate_list(list1,list2):
    result=[]
    for i in range(min(len(list1),len(list2))):
        result.append(list1[i]+list2[i])
    return result
print(concatenate_list(['h','f','y'],['i','i']))


#output
# [8, 7, 10]
# 2
# ['hi', 'fi']

