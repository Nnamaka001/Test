'''Dict1 = {'Name': 'Nigeria', 'State': 'Rivers', 'Year': 2022}
print(Dict1['Name'])
print(type(Dict1))'''

'''list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)'''

'''list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
x = [list1[0]+list2[0], list1[1]+list2[1], list1[2]+list2[2], list1[3]+list2[3]]
print(x)'''

'''numbers = [1, 2, 3, 4, 5, 6, 7]
x = []
for a in numbers:
    b = pow(a, 2)
    x.append(b)
    if len(numbers) == len(x):
        print(x)'''

'''list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = [list1[0]+list2[0], list1[0]+list2[1], list1[1]+list2[0], list1[1]+list2[1]]
print(list3)'''

'''list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.sort(reverse=True)
print(list2)
#for x in list1:
    #for y in list2:
        #print(x,y)
for x,y in zip(list1, list2): #You can also use for x,y in zip(list1, list2[::-1]) to solve it.
    print(x,y)'''

'''list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = list(filter(None, list1))
print(list2)'''

