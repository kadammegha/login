# 5. Write a Python program to find the average of all numbers in a range.
start = 1
end = 10
total = sum(range(start, end + 1))
count = end - start + 1
average = total / count
print(f"Average of numbers from {start} to {end} is: {average}")