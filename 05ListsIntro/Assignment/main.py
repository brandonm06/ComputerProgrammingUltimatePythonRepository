def make_abc() :
    abc = ["a","b","c"]
    return abc

print("Make ABC")
print(make_abc())

def equal_edges(integers) :
    firstnum = integers[0]
    lastnum = integers[-1]

    if firstnum == lastnum :
        return True
    else :
        return False

print("Equal Edges")
print("[1,0,0,1] -->", equal_edges([1,0,0,1]))
print("[1,0,0,2] -->", equal_edges([1,0,0,2]))

def common_edge(list1, list2) :
    first1 = list1[0]
    first2 = list2[0]
    last1 = list1[-1]
    last2 = list2[-1]
    
    if first1 == first2 or first1 == last2 or last1 == first2 or last1 == last2 :
        return True
    else:
        return False
print("Common Edge")
print("[1,2,3], [3,2,1] -->", common_edge([1,2,3], [3,2,1]))
print("[1,2,1], [4,2,5] -->", common_edge([1,2,1], [4,2,5]))
print("[1,2,3], [3,4,5] -->", common_edge([1,2,3], [3,4,5]))

def all_the_same(list) :
    int1 = list[0]
    int2 = list[1]
    int3 = list[2]

    if int1 == int2 and int2 == int3 :
        return True
    else:
        return False
print("All the Same")
print("[1,2,3] -->", all_the_same([1,2,3]))
print("[3,3,3] -->", all_the_same([3,3,3]))
print("[1,3,3] -->", all_the_same([1,3,3]))
print("[3,3,1] -->", all_the_same([3,3,1]))

def all_unique(list) :
    int1 = list[0]
    int2 = list[1]
    int3 = list[2]

    if int1 == int2 or int1 == int3 or int2 == int3 :
        return False
    else:
        return True
print("All Unique")
print("[1,2,3] -->", all_unique([1,2,3]))
print("[3,3,3] -->", all_unique([3,3,3]))
print("[1,3,3] -->", all_unique([1,3,3]))
print("[3,3,1] -->", all_unique([3,3,1]))

def increasing(list):
    int1 = list[0]
    int2 = list[1]
    int3 = list[2]

    if int3 > int2 and int2 > int1 :
        return True
    else:
        return False
print("Increasing")
print("[1,2,3] -->", increasing([1,2,3]))
print("[4,3,7] -->", increasing([4,3,7]))
print("[3,3,1] -->", increasing([3,3,1]))
print("[10,24,46] -->", increasing([10,24,46]))

def all_true(list) :
    word1 = list[0]
    word2 = list[1]
    word3 = list[2]

    if word1 == True and word2 == True and word3 == True :
        return True
    else: 
        return False
print("All True")
print("[False, False, True] -->", all_true([False,False,True]))
print("[True, True, True] -->", all_true([True,True,True]))
print("[False, True, True] -->", all_true([False,True,True]))
print("[False, False, False] -->", all_true([False,False,False]))

def mostly_true(list) :
    word1 = list[0]
    word2 = list[1]
    word3 = list[2]

    if (word1 == True and word2 == True) or (word1 == True and word3 == True) or (word2 == True and word3 == True) or (word1 == True and word2 == True and word3 == True):
        return True
    else: 
        return False
print("Mostly True")
print("[False, False, True] -->", mostly_true([False,False,True]))
print("[True, True, True] -->", mostly_true([True,True,True]))
print("[False, True, True] -->", mostly_true([False,True,True]))
print("[False, False, False] -->", mostly_true([False,False,False]))

def make_copy(list) :
    return list 
print("Make Copy")
print("[1,2,3] -->", make_copy([1,2,3]))

def repeat_thrice(num) :
    numlist = [num, num, num]
    return numlist
print("Repeat Thrice")
print("[3] -->", repeat_thrice(3))

def make_reversed_copy(list) :
    num1 = list[0]
    num2 = list[1]
    num3 = list[2]
    reverselist = [num3, num2, num1]
    return reverselist
print("Make Reversed Copy")
original_list = [3, 5, 1]
new_list = make_reversed_copy(original_list)
print("original list: ", original_list)
print("new list: ", new_list)

def reverse_in_place(list) :
    listold3 = list[0]
    listold1 = list[2]
    list[0] = listold1
    list[2] = listold3
    return list
print("Reverse In Place")
original_list = [3, 5, 1]
new_list = reverse_in_place(original_list)
print("original list: ", original_list)
print("new list: ", new_list)