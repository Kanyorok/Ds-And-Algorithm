'''
Find Number of Days Above Average Temperature

Exampe:
Question: How many day's Temperature?
Input: 2
Input: Day 1's high Temperature: 1
Input: Day 2's high Temperature: 2

Output:
Average = 1.5
1 day(s) above Average
'''
import array as arr

numDays = int(input("How many day's temperature? "))
total = 0
count = 0
records = arr.array('i')
for i in range(1, numDays+1):
    nextDay = int(input("Day " + str(i) + "'s temp: "))
    records.append(nextDay)
    total += nextDay

avg = round(total/numDays, 2)
for i in records:
    if i > avg:
       count += 1 
print("\n Average = "+ str(avg))
print(f'\n The number of days above recommended temp levels were {count}')
