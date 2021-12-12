a=[[1,2,3,4],[5,4,6,7],[7,8,9,0],[1,2,3,4]]
b=[]
for i in range(0,len(a)):
    b.append([])
    for j in range(0,len(a[i])):
        b[i].append(a[j][i])
        
        
print(a)
print(b)
