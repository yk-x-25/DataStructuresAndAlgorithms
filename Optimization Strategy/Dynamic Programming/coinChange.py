import sys
coins = [1,2,5,10]
number = 25

'''
      1     2   3     4   5     6   7     8   9     10  11   12    13     14    15 
1     1     2   3     4   5     6   7     8   9     10  11   12    13     14    15
2     1     1   2      
5
10
'''
dp = [ [ sys.maxsize for _ in range(number+1)] for _ in range(len(coins)) ]

dp =  [ sys.maxsize for _ in range(number+1)]
dp[0]=0
for i in range(len(coins)):
    for j in range(1,number+1):
        # if j % coins[i] ==0: j // coins[i] else:  dp[j - j//coins]
        if j-coins[i]>=0:
            dp[j]= min (dp[j] ,dp[j-coins[i]]+1)

        


for i in range(len(dp)):
    
    print(dp[i],end=" ")

'''
if dp[i-1][j]:
            dp[i][j]=(dp[i-1][j])
        if j%coins[i]==0:
            dp[i][j]= min( dp[i][j] , j//coins[i] )
        
        if i>0 and j-coins[i]>0 and j- j//coins[i]>0 and  dp[i-1][j-coins[i]]: 
            print("here",j, coins[i])
            v = j//coins[i]
            v2 = j- v

            coin = dp[i-1][v2]+1

            coin = min(coin,dp[i-1] [j-coins[i]] + 1)
            
            dp[i][j]=min(coin,dp[i][j])
   '''     


