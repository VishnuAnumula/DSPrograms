# tuples

t=(1,2,3,4)
t1=tuple([1,2,3,4])
t2=(1,2,3,[2,5,9],"hlo")
t3=1,2,3,"hlo"
for i in t:
    print(i)
t4=(t2,t3)
print(t4)
print(t2[1:])
print(t2[:-1])
st=("hlo")*5
print(st)
print(min(t1))
l=[3000,7,1]
print(tuple(l))