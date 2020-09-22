def prime():
    a=input()
    n=int(a)
    num=[];
    i=2
    for i in range(2,n):
       j=2
       for j in range(2,i):
          if(i%j==0):
             break
       else:
          num.append(i)
    print(num)
if __name__=='__main__':
    y=prime()
