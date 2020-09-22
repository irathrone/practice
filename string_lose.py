def string(s):
        new_s = []
        for x in s:
            if x not in new_s:
                new_s.append(x)
        print(new_s)

    
if __name__=='__main__':
    s=input()
    slist=s.split(",")
    slist=[int(slist[i])for i in range(len(slist))]
    y=string(slist)
   
