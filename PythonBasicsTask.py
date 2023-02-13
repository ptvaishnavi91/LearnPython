import random
#Generating 100 random numbers between 0 to 1000
randomlist = random.sample(range(0, 1000), 100)
print("randomlist")
print(randomlist)

#sort list from min to max
sortlist = []
while randomlist:
    min = randomlist[0]
    for x in randomlist:
        if x < min:
            min = x
    sortlist.append(min)
    randomlist.remove(min)
print("sortlist")
print(sortlist)

#calculate average for even and odd numbers
#Printing even list and odd list
evenlist = []
oddlist = []

for x in sortlist:
    if x % 2 == 0:
        evenlist.append(x)
    else:
        oddlist.append(x)
print("evenlist")
print(evenlist)
print("oddlist")
print(oddlist)

# printing average of even and odd list
sum_even = 0
sum_odd = 0
for i in range(0, len(evenlist)):
    sum_even = sum_even+evenlist[i]
print(sum_even)
for j in range(0, len(oddlist)):
    sum_odd = sum_odd+oddlist[j]
print(sum_odd)
#evenlist.clear()
#print(len(evenlist))
try:
    print("Average of even numbers:")
    print(sum_even/len(evenlist))
except: ZeroDivisionError

try:
    print("Average of odd numbers:")
    print(sum_odd/len(oddlist))
except: ZeroDivisionError
