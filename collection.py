# Collections

# 1.List
l1=[1,2,3,4,5]
l2=['hbd',3000,'ps','pk',2.9]
print('length of l2 is',len(l2))
print('printing one specific value')
print(l2[0])
print(l2[2])
print(l2[-2])

# ":" indicates starting value
print('printing some of the values')
print(l2[:3])
print(l2[:-3])

l3=l1
print('values of l3',l3)
#l1=[143,3000]
print('values of l3 after modification',l3)

#l4=l1.copy()
l4=list([6,9,10])
l4.insert(0,77)
print('values of l4 after inserting',l4)
l4.pop()
print('values of l4 after using pop func.',l4)
l4.remove(77)
print('values of l4 after using remove  func.',l4)

#max, min and sum
print('the max value of l4 is',max(l4))
print('the min value of l1 is',min(l1))
print('the sum of all values of l1 is',sum(l1))

#count,sort
print('the count of 40 in the list is',l1.count(l1))
l5=[3000,1,150]
l5.sort()
print('afer sorting l5 :',l5)

l1.clear()
print('after clearing :',l1)
del(l1)


