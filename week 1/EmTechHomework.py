#AI HOMEWORK
#CUADERNO, DIOLIN, LANSANG, SEITON

#TASK: create a program that can compute the mean, median, and mode of 100 random numbers.

import statistics

data = [1,19,20,2,4,6,19,96,9,29,64,12,29,60,34,16,45,23,13,6,8,12,3,9,4,6,2,1,3,5,78,83,45,2,3,11,45,32,21,56,78,93,80,76,52,31,8,9,10,99,10,31,96,55,48,92,21,34,55,22,11,33,55,67,78,79,54,12,45,2,9,12,3,4,76,81,3,23,24,24,90,34,16,17,18,54,44,67,56,12,13,34,6,12,3,5,89,13,70,23]

#compute for mean
x = statistics.mean(data)

#compute for median
y = statistics.median(data)

#compute for mode
z = statistics.mode(data)

print('Mean:', x)
print('Median:', y)
print('Mode:', z)