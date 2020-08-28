def order(ns):
    t=ns.split()
    t1=len(t)
    num="123456789"
    nl=[i for i in range(t1)]
    for j in t:
        for k in j:
            if k in num:
                nl[int(k)-1]=j

    nl1=" ".join(nl)
    return nl1.strip()
