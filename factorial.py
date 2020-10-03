# finding the factorial of a given number

# a. Without using a Function
s=1
n=int(input('No. to which factorial is to be calculated: '))
for i in range(1,n+1):
    s=s*i
print(s)
print("")

# b. Uing a function
def fact(n):
    v=1
    for i in range(1,n+1):
        v=v*i
    return s
print(fact(n=int(input('No. to which factorial is to be calculated: '))))
print("")

# c. using a recursive function
def fact1(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact1(n-1)
print(fact1(n=int(input('No. to which factorial is to be calculated: '))))
