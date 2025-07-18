ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]#1
ages.sort()
print("\n","Here is the list: ",ages)
min_age=min(ages)
max_age=max(ages)
print("\n","Here is the minimum age in the list: ",min_age)
print("\n","Here is the maximum age in the list: ",max_age)
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2])/2
else:
    median = ages[n//2]
print("\n","The madian age is:",median)
average=sum(ages)/len(ages)
print("\n","The average in the list is: ",average)
age_range=max_age-min_age
print("\n","The range in the list is: ",age_range)
min_diff = abs(min_age-average)
max_diff = abs(max_age-average)
print("\n","abs(min - average):", min_diff,"abs(max - average):", max_diff)
