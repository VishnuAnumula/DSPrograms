# functions

def jarvis(name,bio,*v):
    print(name)
    print(bio)
    print(*v)
def priority(**p):
    for keys,values in p.items():
        print("%s=%s" %(keys,values))
def times():
    return 3000,1
n='Tony Stark Jr.'
b="You'll know who I am."
jarvis(n,b,'Genius','Billionaire','Playboy','Philanthropist')
priority(first='Pepper', second='Morgan', third='Kid!')
l,v=times()
lv=lambda l:l*v
print(lv(l))