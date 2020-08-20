def iq_test(a):
    print("Welocme to my program")
    a=[int(i) for i in a.split(" ")]
    a=['e' if i%2==0 else 'o' for i in a]
    if a.count('o')==1:
        return a.index('o')+1
    else:
        return a.index('e')+1