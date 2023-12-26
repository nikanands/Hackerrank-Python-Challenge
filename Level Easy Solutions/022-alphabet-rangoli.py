def print_rangoli(size):
    space=''
    n=0
    c=''
    d=''
    z=[]
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
                                         't','u','v','w','x','y','z']
    for j in range(1,size+1):
        b=letters[size-j]
        c=c+'-'+b
        d=b+'-'+d
        x=(2*size-2-n)*'-'+c[1:]+d[1:].rstrip('-')+(2*size-2-n)*'-'
        z.append(x)
        n+=2

    for i in range(len(z)):
        print(z[i])

    z.reverse()

    for k in range(1,len(z)):
            print(z[k])