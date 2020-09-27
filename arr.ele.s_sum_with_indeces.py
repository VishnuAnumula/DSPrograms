# Adding the array elements with their respective index values

Arr=[1,7,150,786,3000]
n=len(Arr)
for i in range(n):
    Arr[i]+=i
print(Arr)
#method 2
A1=[]
for i in range(6):
    A1.append(int(input())+i)
print(A1)
a=[]
for i in range(1,5):
    a.insert(i)
print(a)