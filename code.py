def alphabe_position(s2):
    s="abcdefghijklmnopqrstuvwxyz"
    s_={}
    for i,k in enumerate(s,1):
        s_[k]=i
    s1=""
    for i in s2.lower():
        if i in s: 
            s1+=str(s_[i])+" "
    return s1.strip()