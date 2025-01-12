"""l = list(eval(input('Enter a list of numbers: ')))
n = len(l)
count = 0
for i in range(n - 1):
    small = i
    for j in range(i+1, n):
        if l[j]< l[small]:
            small = j     
    l[i], l[small] = l[small], l[i]
    count+=1
print(l)
print(count) """

l = list(eval(input('Enter a list of numbers: ')))
n = len(l)
count = 0
for i in range(n - 1):
    for j in range(0, n-i-1):
        if l[j]>l[j + 1]:
            l[j], l[j + 1] = l[j+1], l[j]
    count+= 1
print(l)
print(count)
          

               
