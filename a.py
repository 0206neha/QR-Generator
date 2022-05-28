def isAnagram(s,t):
    l1=list(s)
    l2=list(t)
    print(l1,l2)
    for i in s:
        if i in t:
            a=True
        else:
            a=False
    print(a)


isAnagram("rat","car")
    