'''mylist = [7, 3, 5, 6, 9, 12, 8, 10]
mylist.sort()
print(mylist)
x = len(mylist)
y = sum(mylist)
z = y/x
print(z)'''

'''mylist = [7, 3, 5, 6, 9, 12, 8, 10] #Calculation for the mean deviation od a list
#x = int(input('Enter a numer: '))
#y = mylist.append(x)
#print(mylist)

a = sum(mylist)
b = len(mylist)
d = a/b
newlist = []
for x in mylist:
    c = abs(x - d)
    newlist.append(c)
    if len(newlist) == len(mylist):
        print(newlist)
        y = sum(newlist)
        z = len(newlist)
        w = y/z'''

'''mylist = [3, 9, 6, 8, 6, 5, 7, 4]
a = sum(mylist)
b = len(mylist)
c = a/b
print(c)
newlist = []
for x in mylist:
    d = abs(x - c)*abs(x - c) #OR d = pow(abs(x - c), 2)
    newlist.append(d)
    if len(newlist) == len(mylist):
        print(newlist)
        e = sum(newlist)
        f = (len(newlist)) - 1
        g = e/f
        import math as m
        h = m.sqrt(g)
        print(h)'''

list_x = [3, 5, 2, 8, 2, 6, 7, 1, 4, 2, 9, 6]
list_y = [487, 445, 272, 641, 187, 440, 346, 238, 312, 269, 655, 563]
N = len(list_x) #Number of observations, or years
c = list_x[0] * list_y[0]
d = list_x[1] * list_y[1]
e = list_x[2] * list_y[2]
f = list_x[3] * list_y[3]
g = list_x[4] * list_y[4]
h = list_x[5] * list_y[5]
i = list_x[6] * list_y[6]
j = list_x[7] * list_y[7]
k = list_x[8] * list_y[8]
l = list_x[9] * list_y[9]
m = list_x[10] * list_y[10]
n = list_x[11] * list_y[11]
nlist1 = [c, d, e, f, g, h, i, j, k, l, m, n]
A = sum(nlist1)
o = sum(list_x)
p = sum(list_y)
q = o * p
nlist2 = []
for x in list_x:
    B = pow(x, 2)
    nlist2.append(B)
    if len(nlist2) == len(list_x):
        print(nlist2)
        r = sum(nlist2)
        s = (N*A) - p
        t = (N*r) - r
        b = s/t
        print(b)
        a = (p -(b*o) )/N
        print(a)

Y = a + (b*9) # b=(N*Sum(XY)-Sum(X)*Sum(Y))/(N*Sum(X*X))-Sum(X*X); a = SUm(Y)-(b*Sum(X)/N
print(Y)