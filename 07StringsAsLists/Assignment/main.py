def is_alliteration(wrd1,wrd2) :
    firstletter = wrd1[0]
    if wrd2[0] == firstletter :
        return True
    return False

print("Hey, Hi -->", is_alliteration("Hey","Hi"))
print("Yes, No -->", is_alliteration("Yes","No"))

