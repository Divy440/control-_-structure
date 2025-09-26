'''Task 2: Sum of Integers from 1 to 50 Using a Loop

Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
'''

a = int(input("Enter a number: "))     #let a = 1
b = int(input("Enter a number: "))     #let b = 51
total_sum = a + b
total_sum = 0
for number in range(a, b):
    total_sum += number

print(f"Total sum from a to b is : {total_sum}")