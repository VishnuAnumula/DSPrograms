# printing pairs of a given array whose difference is a given specific key 

avv = [1,2,3,4,5,7,8,9]
key = int(input('Enter the key'))
for i in avv:
    for j in avv:
        if j-i==key:
            print("(",i,",",j,")", end =' ')