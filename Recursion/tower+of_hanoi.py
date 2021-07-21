import sys
def toh(tow1,tow2,tow3,f=True,moveuntil=-1):

    if f and tow1[-1] == sys.maxsize and tow2[-1] != sys.maxsize:
        return toh(tow2,tow1,tow3)
    if not f and tow3[-1] == moveuntil:
        moveuntil-=1 
    if not f and tow1[-1] < moveuntil:
        return
     
    if tow1[-1]==sys.maxsize:
        return 

    if len(tow3)-2 == tow3[-1]-tow3[0]:
        return 
    
    print("intermediate  t1 : {}, t2 : {} t3 :{} ".format(tow1,tow2,tow3))

    if (len(tow1)-1) %2 ==0:
        if tow2[-1] > tow1[-1]:
            v = tow1.pop(-1)
            tow2.append(v)
        else:
            print("before  t1 : {}, t2 : {} t3 :{} ".format(tow1,[tow2],tow3))
            toh(tow2,tow1,tow3,False,moveuntil)
            print("after  t1 : {}, t2 : {} t3 :{} ".format(tow1,tow2,tow3))
    else:

        if tow3[-1] > tow1[-1]:
            v= tow1.pop(-1)
            tow3.append(v)
        else:
            print("before  t1 : {}, t2 : {} t3 :{} ".format(tow1,tow2,tow3))
            toh(tow3,tow1,tow2,False,moveuntil)
            print("after  t1 : {}, t2 : {} t3 :{} ".format(tow1,tow2,tow3))
    
    toh(tow1,tow2,tow3,f,moveuntil)
    
  
     
  
if __name__ == '__main__':
    t1 = [sys.maxsize,3]
    t2 = [sys.maxsize,2]
    t3 = [sys.maxsize,4,1]
    toh(t1,t2,t3,True,4)
    print(t1,t2,t3)