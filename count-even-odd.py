'''Write a Python program to count the number of even
and odd numbers from a series of numbers.'''
num =[1, 2, 3, 4, 5, 6,7,8,9,0,11,12,13,14,16]
count_even = 0
count_odd = 0
for i in num:
    if i % 2 :
        count_odd=count_odd +1
    else:
        count_even=count_even+1
print('The Even number is ',count_even)
print('The Odd number is ',count_odd)


