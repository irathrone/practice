def bs():
    x=input()
    xl=x.split(",")
    xl=[int(xl[i])for i in range(len(xl))]
    for i in range(len(xl)-1):
        for j in range(len(xl)-1-i):
            if xl[j]>xl[j+1]:
                xl[j],xl[j+1]=xl[j+1],xl[j]
    print(xl)
if __name__=='__main__':
    y=bs()
