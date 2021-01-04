# Fibonacci seguence in 8 lines. 
numbers = []
for i in range(99):
    if i < 2:
        numbers.insert(i,i)
    else:
        numbers.insert(i, numbers[i-1] + numbers[i-2])
print (numbers)

# Sample visualization. 
for i in range(13):
    for x in range(numbers[i]):
        print(".", end="")
    print()
print(numbers[len(numbers)-3])