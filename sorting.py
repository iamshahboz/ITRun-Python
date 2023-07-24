numbers = [12,0,48, 14,-4,-6,77,100]
numbers.sort() 
#print(numbers)

#print(sorted(numbers))

#buble sort
n = len(numbers)
for i in range(n):
    already_sorted = True 
    for j in range(n-1-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
            already_sorted = False 

        if already_sorted:
            break 

print(numbers)


