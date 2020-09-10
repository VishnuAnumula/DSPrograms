# pattern 1
# Hello
# Hell
# Hel
# He
# H
s="Hello"
l=len(s)
i=l
while i!=0:
    print(s[0:i])
    i-=1
print("")

# pattern 2
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
k=1
for i in range(1,6):
    for j in range(1,6):
        r=k%2
        print(r,end=' ')
        k+=1
    print("")
print("")

# pattern 3
# 1 2 3 4 5 
# 6 7 8 9 0
# 1 2 3 4 5 
# 6 7 8 9 0
# 1 2 3 4 5
k=1
for i in range(1,6):
    if k>10:
        k=1
    for j in range(1,6):
        if k!=10:
            print(k,end=' ')
            k+=1
        else:
            print('0',end='')
            k+=1
    print("")
              




