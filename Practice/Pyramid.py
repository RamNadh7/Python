n = int(input('Enter the number: '))  # Define n with the desired number of pyramid levels
mylist = []
for i in range(n):
    pat = ''
    for j in range(n - i - 1):
        pat = pat + ' '
    for k in range(2 * i + 1):
        pat = pat + '*'
    for l in range(n - i - 1):
        pat = pat + ' '
    mylist.append(pat)