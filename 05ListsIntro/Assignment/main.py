def make_abc() :
    abc = ["a","b","c"]
    return abc
print(make_abc())

def equal_edges(integers) :
    firstnum = integers[0]
    lastnum = integers[-1]

    if firstnum == lastnum :
        return True
    else :
        return False
    
print("[1,0,0,1] -->", equal_edges([1,0,0,1]))
print("[1,0,0,2] -->", equal_edges([1,0,0,2]))

def common_edge(list1, list2) :
    