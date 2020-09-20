import random
x=input()
xlist=x.split(",")
xlist=[int(xlist[i])for i in range(len(xlist))]
some = random.sample(xlist , 1)
print(some)
