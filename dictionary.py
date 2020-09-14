# dictionary

d={}
# dictionary with integer keys
d1={1: 'pen', 2: 'pencil'}
print('printing using for loop')
for i in d1:
    print(i)
print('printing using items() in a for loop')
for i in d1.items():
    print(i)
print('printing only keys using for loop')
for i in d1.keys():
    print(i)
print('printing only values using for loop')
for i in d1.values():
    print(i)

# using mixed keys
d2={'name': 'Bindu', 1: '[2,4,3]'}

# using dict()
d4=dict([(1, 'pen'), (2, 'pencil')])

# creating nested dictionary
d5={'roll no':1219007,'name':'James Bond','details':{'Age':43,'Gender':'Male'},'personality':{'height':'5"10','determination':'strong'}}

# example of dictionary comprehension
squares={}
for i in  range(1,11):
    squares[i]=i*i
print(squares) 
# shortcut of the above code
squares={x:x*x for x in range(1,11)}
print(squares) 


