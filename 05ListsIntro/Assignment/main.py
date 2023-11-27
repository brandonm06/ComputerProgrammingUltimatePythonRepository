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
    