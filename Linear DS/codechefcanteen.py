import sys
'''

e = n
h = m


cm  = 3h
cc   = e+h
om  =2e

maximize qty.
       e
       0    1       2                       3      4                           5
h   0  0    0       om                      om    2om                         2om
    1  0    0       om                      om+cc mincost (2om or 1om+1cc)    2om+1cc
    2  
    3
    4
    5  1cm 1cm+1cc  (1cm+1om)|(2cc+1cm)  (1cm+1om+1cc)|(3cc)|87
    -----------------------
    6
    7
    8
    9
    10 



    3
5 4 4 2 2 2
4 5 5 1 2 3
4 5 5 3 2 1
'''
cost_om = 0
cost_cc = 0
cost_cm = 0
def getMinDict(dictA,dictB):
    om_A = dictA["om"] 
    cc_A = dictA["cc"]
    cm_A = dictA["cm"]  
    totalA = om_A+cc_A+cm_A

    costA = om_A*cost_om + cc_A*cost_cc + cm_A*cost_cm

    om_B = dictB["om"]
    cc_B = dictB["cc"] 
    cm_B = dictB["cm"] 
    totalB = om_B+cc_B+cm_B

    costB = om_B*cost_om + cc_B*cost_cc + cm_B*cost_cm
    if totalA ==totalB:
        if costA>costB:
            return dictB
        else:
            return dictA
    
    elif totalA>totalB:
        return dictA

    return dictB

def getMaxAtCurrentDict(eggs,choco):
    om = eggs//2
    ms = choco//3
    cc = min(choco,eggs)

    d= {"om":om ,"cm":0 , "cc":0 ,"re":eggs-2*om,"rh":choco}
    d1= {"om":0 ,"cm":ms , "cc":0 ,"re":eggs,"rh":choco-3*ms}
    d2= {"om":0 ,"cm":0 , "cc":cc ,"re":eggs-cc,"rh":choco-cc}

    return getMinDict(getMinDict(d,d1),d2)
def updateDict(dictA,dictB):
    
    dictA["om"]+=dictB["om"] 
    dictA["cm"]+=dictB["cm"] 
    dictA["cc"]+=dictB["cc"] 
    dictA["rh"] = dictB["rh"]
    dictA["re"] = dictB["re"]

    return dictA


def optimalSol(dictionary):
    rh = dictionary["rh"]
    re = dictionary["re"]
    remainingoptimal =  (re,rh)
    return updateDict(dictionary,remainingoptimal)

test = int(input())
for _ in range(test):

    N , eggs, chocolates,  a,b,c  = list(map(int,input().split()))
    cost_om,cost_cm, cost_cc = a,b,c

    dictionary ={"om":0 , "cm":0,"cc":0,"rh":0,"re":0}
    dp = [  [dictionary for _ in range(eggs+1)] for _ in range(chocolates+1) ]
    
    for j in range(chocolates+1):
        for i in range(eggs+1):

            curr_max = getMaxAtCurrentDict(i,j)
          
         
            left_max = optimalSol(dp[j][i-1]) 

          
            top_dict = dp[j-1][i].copy()
            top_dict["rh"]+=1
            top_max = optimalSol(top_dict)

            

            dp[j][i] =  getMinDict( getMinDict(curr_max,top_max),left_max )           
    for i in dp:
        print (i,end="\n***\n")





        '''
      [{'om': 0, 'cm': 0, 'cc': 0, 're': 0, 'rh': 0}, {'om': 0, 'cm': 0, 'cc': 0, 're': 1, 'rh': 0}, {'om': 1, 'cm': 0, 'cc': 0, 're': 0, 'rh': 0}, {'om': 1, 'cm': 0, 'cc': 0, 're': 1, 'rh': 0}, {'om': 2, 'cm': 0, 'cc': 0, 're': 0, 'rh': 0}, {'om': 2, 'cm': 0, 'cc': 0, 're': 1, 'rh': 0}]
***
[{'om': 0, 'cm': 0, 'cc': 0, 're': 0, 'rh': 1}, {'om': 0, 'cm': 0, 'cc': 1, 're': 0, 'rh': 0}, {'om': 0, 'cm': 0, 'cc': 1, 're': 1, 'rh': 0}, {'om': 1, 'cm': 0, 'cc': 1, 're': 0, 'rh': 0}, {'om': 1, 'cm': 0, 'cc': 1, 're': 0, 'rh': 0}, {'om': 2, 'cm': 0, 'cc': 1, 're': 0, 'rh': 0}]
***
[{'om': 0, 'cm': 0, 'cc': 0, 're': 0, 'rh': 2}, {'om': 0, 'cm': 0, 'cc': 1, 're': 0, 'rh': 1}, {'om': 0, 'cm': 0, 'cc': 2, 're': 0, 'rh': 0}, {'om': 0, 'cm': 0, 'cc': 2, 're': 1, 'rh': 0}, {'om': 1, 'cm': 0, 'cc': 2, 're': 0, 'rh': 0}, {'om': 1, 'cm': 0, 'cc': 2, 're': 0, 'rh': 0}]
***
[{'om': 0, 'cm': 1, 'cc': 0, 're': 0, 'rh': 0}, {'om': 0, 'cm': 0, 'cc': 1, 're': 0, 'rh': 2}, {'om': 0, 'cm': 0, 'cc': 2, 're': 0, 'rh': 1}, {'om': 0, 'cm': 0, 'cc': 3, 're': 0, 'rh': 0}, {'om': 0, 'cm': 0, 'cc': 3, 're': 1, 'rh': 0}, {'om': 0, 'cm': 0, 'cc': 3, 're': 2, 'rh': 0}]
***
[{'om': 0, 'cm': 1, 'cc': 0, 're': 0, 'rh': 1}, {'om': 0, 'cm': 1, 'cc': 1, 're': 0, 'rh': 0}, {'om': 0, 'cm': 0, 'cc': 2, 're': 0, 'rh': 2}, {'om': 0, 'cm': 0, 'cc': 3, 're': 0, 'rh': 1}, {'om': 0, 'cm': 0, 'cc': 4, 're': 0, 'rh': 0}, {'om': 0, 'cm': 0, 'cc': 4, 're': 1, 'rh': 0}]
***
[{'om': 0, 'cm': 1, 'cc': 0, 're': 0, 'rh': 2}, {'om': 0, 'cm': 1, 'cc': 1, 're': 0, 'rh': 1}, {'om': 0, 'cm': 1, 'cc': 2, 're': 0, 'rh': 0}, {'om': 0, 'cm': 0, 'cc': 3, 're': 0, 'rh': 2}, {'om': 0, 'cm': 0, 'cc': 4, 're': 0, 'rh': 1}, {'om': 0, 'cm': 0, 'cc': 5, 're': 0, 'rh': 0}]
***
        '''