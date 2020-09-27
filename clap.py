# replacing with clap

for i in range(1,21):
    if i%3==0:
        print('clap')
    else:
        v=i
        t=0
        while v!=0:
            r=v%10
            if r==3 or r==6 or r==9:
                t=1
                break
            v//=10
        if t==1:
            print('clap')
        else:
            print(i)