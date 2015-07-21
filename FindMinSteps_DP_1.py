'''
Created on Jul 20, 2015

@author: ljiang

https://www.codechef.com/wiki/tutorial-dynamic-programming
q1:
Problem Statement: On a positive integer, you can perform any one of the following 3 steps. 1.) Subtract 1 from it. ( n = n - 1 )  , 2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1
eg: 1.)For n = 1 , output: 0       2.) For n = 4 , output: 2  ( 4  /2 = 2  /2 = 1 )    3.)  For n = 7 , output: 3  (  7  -1 = 6   /3 = 2   /2 = 1 )
'''

#dynamic programming way - bottom up, iteration
def find_min_step(n):
    pass
    steps=[]
    steps.append(None)
    steps.append(0)
    for i in xrange(2,n+1):
        steps.append(steps[i-1]+1)
        if i%2==0:
            steps[i]=min(steps[i],1+steps[i/2])
        if i%3==0:
            steps[i]=min(steps[i],1+steps[i/3])
            
    return steps[n]

#memorization way - top down, recursion
def find_min_step_2(n):
    pass
    if n ==1:
        step=0
    else:
        step=find_min_step_2(n-1)+1
        if n%2==0:
            step=min(step,find_min_step(n/2)+1)
        if n%3==0:
            step=min(step,find_min_step(n/3)+1)
    
    return step
        
        

