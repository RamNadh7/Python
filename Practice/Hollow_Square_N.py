'''
You are given an integer n. 
Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. 
The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

EX:
Input: 3
Output: ['***', '* *', '***']

'''
n=int(input())
if n>1:
    edge=n*'*'
    mid='*'+(' '*(n-2))+'*'
    mylist=[]
    mylist.append(edge)
    for i in range(1,n-1):
        mylist.append(mid)
    mylist.append(edge)
else:
    mylist=['*']

print(mylist)

