'''
You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).
Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']

'''
n=int(input('Enter n value:'))
m=int(input('Enter m value: '))
mylist=[m*'*']*n
print(mylist)