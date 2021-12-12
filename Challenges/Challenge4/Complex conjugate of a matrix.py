a=[[complex(2,3),complex(3,-4)],[complex(4,5),complex(6,2)]]
b=[]
for i in range(0,len(a)):
    b.append([])
    for j in range(0,len(a[i])):
        b[i].append(complex(a[j][i].imag,a[j][i].real))
        
        
print(a)
print(b)
