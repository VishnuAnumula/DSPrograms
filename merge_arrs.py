a1=[1,3,7,9]
a2=[150,786,3000]
a=[]
l1=len(a1)
l2=len(a2)
i=0
j=0
while i<l1 and j<l2:
    if a1[i] < a2[j]:
        a.append(a1[i])
        i+=1
    else:
        a.append(a2[j])
while i<l1:
    a.append(a1[i])
    i+=1
while j<l2:
    a.append(a2[j])
    j+=1
print('Array after merging')
print(a)