n = set(range(1*10**4))
g = set(range(1*10**9))
b = g.intersection(n)
a = g.difference(b)

print(len(a))


#2

s1 = {1,2,4,54,6,57,78,345,456,23,5645,6575,76}
s2 = {1,2,3,4,5,6,7768,89,9,45,12,98,56,34,2232,342,45,67,8234,66}
print((len(s1)) + (len(s2)))

#3

s3 = input(':')
s4 = set()
s3 = ''.join(s3.split())
for i in s3:
    if i not in s4:
        s4.add(i)
        print('Yes')
    else:
        print('NO')