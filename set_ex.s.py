s1={'hi',"hello",'namaste'}
l1=[1,2,3000]
s2=set(l1)
print( 'data type is',type(s2))
for x in s1:
    print('for',x)
print(s1)

# adding an element to the set
s1.add('students')
print('add',s1)

# add multiple items to a set using update
s1.update(['pen','pencil','eraser'] )
print('update',s1)

# Deleting a element from the set
#s1.remove('good') # generates an error
s1.discard('pen') # does not
print('discard',s1)
s1.pop()
print('pop',s1)

# joining two sets
s3=s1.union(s2)
print('union',s3)