def Tri_a_bulles(L):
    for _ in range(len(L)-1):
        for i in range(len(L)-1):
            if L[i]>L[i+1]:
                T,T2=L[i],L[i+1]
                L[i],L[i+1]=T2,T    
    return L