def alphabet_position(s2):
    s="abcdefghijklmnopqrstuvwxyz"
    s_={}
    for i,j in enumerate(s,1):
        s_[j]=i
    s1=""
    for i in s2.lower():
        if i in s: 
            s1+=str(s_[i])+" "
    return s1.strip()