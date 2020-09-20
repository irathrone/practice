def ran ():
    import random
    x=input()
    xlist=x.split(",")
    xlist=[int(xlist[i])for i in range(len(xlist))]
    some = random.sample(xlist , 1)
    print(some[-1])
if __name__=='__main__':
    y=ran()
