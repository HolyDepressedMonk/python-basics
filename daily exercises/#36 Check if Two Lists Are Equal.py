# Write a function to Check if Two Lists Are Equal and Don't simply use list1 == list2.

def checkEqualList(list1, list2):
    if len(list1) == len(list2):
        for i in list1:
            for j in list2:
                if list[i] == list[j]:
                    return True
                else:
                    return False

list1 = [1,2,3]
list2 = [3,2,1]
print(checkEqualList(list1, list2))