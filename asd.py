list1 = ['a','b','c']
list2 = ['a1','b1','c1']
list3 = ['a2','b2','c2']
def abc():
    for i in list1:
        for j in list2:
            for k in list3:
                print(i+j+k)
    return ()

abc()