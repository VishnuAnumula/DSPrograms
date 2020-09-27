# program to print the following format depending on the value of n
# I/p
# n=2
# O/p
# 2 2 2
# 2 1 2
# 2 2 2

# I/p
# N=3
# 3 3 3 3 3
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3
# 3 3 3 3 3

# N=5
# 5 5 5 5 5 5 5 5 5 
# 5 4 4 4 4 4 4 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 2 1 2 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 4 4 4 4 4 4 5 
# 5 5 5 5 5 5 5 5 5

n=int(input('limit : '))
for i in range(1,(n*2)):
    for j in range(1,(n*2)):
        print(n,end=' ')
    print("")
              
